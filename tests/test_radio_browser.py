import re

import pytest
import random
import responses

from pyradios import RadioBrowser
from pyradios.radios import version


BASE_URL = "https://nl1.api.radio-browser.info/"


def pick_random_station(rb, **params):
    stations = rb.search(**params)
    return random.choice(stations)


def test_version():
    assert version == "1.0.2"


@pytest.fixture
def rb():
    _rb = RadioBrowser()
    _rb.base_url = BASE_URL
    return _rb


@pytest.fixture
def station_struct():
    """https://de1.api.radio-browser.info/#Struct_station"""
    return {
        "changeuuid",
        "stationuuid",
        "name",
        "url",
        "url_resolved",
        "homepage",
        "favicon",
        "tags",
        "country",
        "countrycode",
        "state",
        "language",
        "languagecodes",
        "votes",
        "lastchangetime",
        "lastchangetime_iso8601",
        "codec",
        "bitrate",
        "hls",
        "lastcheckok",
        "lastchecktime",
        "lastchecktime_iso8601",
        "lastcheckoktime",
        "lastcheckoktime_iso8601",
        "lastlocalchecktime",
        "lastlocalchecktime_iso8601",
        "clicktimestamp",
        "clicktimestamp_iso8601",
        "clickcount",
        "clicktrend",
        "ssl_error",
        "geo_lat",
        "geo_long",
        "serveruuid",
        "has_extended_info",
        "iso_3166_2",
    }


def test_station_struct(rb, station_struct):
    """
    Checks if the keys in the API response structure have changed.

    Note: This test is more about the API service implmentation, than
    it is about this python library.

    See details:
        https://de1.api.radio-browser.info/#Struct_station
    """
    stationuuid = "d97b5842-8e9b-46cc-85f0-d2dff6738c7c"
    resp = rb.station_by_uuid(stationuuid)
    response_keys = set(resp[0].keys())
    missing_keys = response_keys.difference(station_struct)
    assert len(missing_keys) == 0, f"Keys missing {missing_keys}"


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


@responses.activate
def test_request_codecs_with_filters(rb):
    """
    This test runs against a subset of the API response, with the sole
    purpose of ensuring the behavior of the filter mechanism of the
    tested method.
    """
    # subset of the API response for testing purposes
    payload = [
        {'name': 'AAC', 'stationcount': 2226},
        {'name': 'MP3', 'stationcount': 19678},
        {'name': 'MP3,H.264', 'stationcount': 6},
        {'name': 'OGG', 'stationcount': 265},
        {'name': 'UNKNOWN', 'stationcount': 1827},

    ]
    responses.add(
        responses.GET,
        BASE_URL + "json/codecs/",
        json=payload,
        status=200,
    )

    resp = rb.codecs(codec="mp3")
    assert len(resp) == 1
    assert resp[0]["name"] == "MP3", "only one codec should be in the response"


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


def test_request_stations_by_votes(rb):
    resp = rb.stations_by_votes(1)
    assert len(resp) == 1, "exactly one station should be in the response"


def test_request_station_byuuid(rb):
    uuid = pick_random_station(rb, limit=100)["stationuuid"]
    resp = rb.station_by_uuid(uuid)
    assert len(resp) == 1, "exactly one should match the uuid '%s'" % uuid


def test_request_station_tag_list(rb):
    tag_list = ["New York City", "Jazz"]
    resp = rb.stations_by_tag_list(tag_list)

    assert len(resp) > 0, "no match on tags [%s]" % ", ".join(tag_list)

    some_stations = random.choices(resp, k=5)  # just take some stations

    for station in some_stations:
        # Be aware that tag search is token (or word) based
        # meaning that searching 'jazz' will match 'smooth jazz'
        tagtokens = re.split(r"\s|,", station["tags"])
        queried_tokens = re.split(r"\s|,", ",".join(tag_list).lower())
        missing_tokens = set(queried_tokens) - set(tagtokens)
        assert (
            len(missing_tokens) == 0
        ), "tokens missing %s in result-tag %s" % (missing_tokens, tagtokens)
