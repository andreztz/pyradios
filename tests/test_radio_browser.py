import pytest
import responses
import random
import re

from pyradios import RadioBrowser


BASE_URL = "https://nl1.api.radio-browser.info/"


@pytest.fixture
def rb():
    _rb = RadioBrowser()
    _rb.base_url = BASE_URL
    return _rb


@responses.activate
def test_request_countrycodes(rb):

    expected = [{"name": "AD", "stationcount": 5}]
    responses.add(
        responses.GET,
        BASE_URL + "json/countrycodes/",
        json=expected,
        status=200,
    )

    resp = rb.countrycodes()
    assert len(resp) > 0, "at least one country should be in the response"
    assert "name" in resp[0]
    assert "stationcount" in resp[0]
    assert resp == expected


def test_request_countrycodes_with_filters(rb):

    # expected = [{"name": "BR", "stationcount": 607}]

    resp = rb.countrycodes(code="BR")
    assert len(resp) > 0, "at least one country should be in the response"
    assert resp[0]["name"] == "BR"


def test_request_codecs(rb):

    # expected = [{"name": "MP3", "stationcount": 16620}]

    resp = rb.codecs()
    assert len(resp) > 0, "at least one codec should be in the response"
    assert "name" in resp[0]
    assert "stationcount" in resp[0]


def test_request_codecs_with_filters(rb):

    # expected = [{"name": "MP3", "stationcount": 16620}]

    resp = rb.codecs(codec="mp3")
    assert len(resp) > 0, "at least one codec should be in the response"
    assert resp[0]["name"] == "MP3"


def test_request_states_with_filters(rb):

    # expected = [{"name": "Parana", "country": "Brazil", "stationcount": 23}]

    resp = rb.states(country="BRAZIL", state="Parana")

    assert len(resp) > 0, "at least one state should be in the response"
    assert "name" in resp[0]
    assert "country" in resp[0]
    assert "stationcount" in resp[0]


def test_request_languages_with_filters(rb):

    # expected = [
    #     {"name": "brazilian portuguese", "stationcount": 8,},
    #     {"name": "portuguese", "stationcount": 638,},
    # ]

    resp = rb.languages(language="portuguese")

    assert len(resp) > 0, "at least one language should be in the response"
    assert "name" in resp[0]
    assert "stationcount" in resp[0]


# @responses.activate
def test_request_tags_with_filters(rb):

    # expected = [{"name": "drum and bass", "stationcount": 73,}]
    # responses.add(
    #     responses.GET,
    #     BASE_URL + "json/tags/drum%20and%20bass",
    #     json=expected,
    #     status=200,
    # )
    resp = rb.tags(tag="Drum and Bass")

    assert len(resp) > 0, "at least one tag should be in the response"
    assert "name" in resp[0]
    assert "stationcount" in resp[0]


@responses.activate
def test_request_station_click_counter(rb):

    expected = {
        "ok": True,
        "message": "retrieved station url",
        "stationuuid": "96062a7b-0601-11e8-ae97-52543be04c81",
        "name": "BBC Radio 1",
        "url": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p",
    }
    # mock responses
    responses.add(
        responses.GET,
        BASE_URL + "json/url/96062a7b-0601-11e8-ae97-52543be04c81",
        json=expected,
        status=200,
    )

    resp = rb.click_counter("96062a7b-0601-11e8-ae97-52543be04c81")

    assert "ok" in resp
    assert "message" in resp
    assert "stationuuid" in resp
    assert "name" in resp
    assert "url" in resp
    assert resp == expected


def pick_random_station(rb, **params):
    stations = rb.search(**params)
    return random.choice(stations)


def assert_expected_keys(station):
    # Note: this assertion is more about the API service implmentation,
    #       than it is about this py library
    expected_station_keys = {
        "changeuuid", "stationuuid", "name", "url",
        "url_resolved", "homepage", "favicon", "tags", "country",
        "countrycode", "state", "language", "votes", "lastchangetime",
        "codec", "bitrate", "hls", "lastcheckok", "lastchecktime",
        "lastcheckoktime", "lastlocalchecktime", "clicktimestamp",
        "clickcount", "clicktrend",
    }
    missingkeys = expected_station_keys - set(station.keys())
    assert len(missingkeys) == 0, "keys missing: %s" % missingkeys


def test_request_station_byuuid(rb):

    uuid = pick_random_station(rb, limit=100)['stationuuid']
    resp = rb.station_by_uuid(uuid)

    assert len(resp) == 1, "exactly one should match the uuid '%s'" % uuid
    assert_expected_keys(resp[0])


def test_request_station_tag_list(rb):

    tag_list = ["New York City", "Jazz"]
    resp = rb.stations_by_tag_list(tag_list)

    assert len(resp) > 0, "no match on tags [%s]" % ', '.join(tag_list)

    some_stations = random.choices(resp, k=5)  # just take some stations
    for station in some_stations:
        assert_expected_keys(station)  # check it has the expected fields

        # Note: this assertion is more about the API service implmentation,
        #       than it is about this py library
        # and be aware that tag search is token (or word) based
        #        meaning that searching 'jazz' will match 'smooth jazz'
        tagtokens = re.split(r"\s|,", station["tags"])
        queried_tokens = re.split(r"\s|,", ','.join(tag_list).lower())
        missing_tokens = set(queried_tokens) - set(tagtokens)
        assert len(missing_tokens) == 0,\
            "tokens missing %s in result-tag %s" % (missing_tokens, tagtokens)
