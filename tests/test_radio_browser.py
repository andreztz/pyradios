import pytest
import responses

from pyradios import RadioBrowser


BASE_URL = "https://nl1.api.radio-browser.info/"


@pytest.fixture
def rb():
    return RadioBrowser(base_url=BASE_URL)


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
    assert "name" in resp[0]
    assert "stationcount" in resp[0]
    assert resp == expected


def test_request_countrycodes_with_filters(rb):

    # expected = [{"name": "BR", "stationcount": 607}]

    resp = rb.countrycodes(code="BR")
    assert resp[0]["name"] == "BR"


def test_request_codecs(rb):

    # expected = [{"name": "MP3", "stationcount": 16620}]

    resp = rb.codecs()
    assert "name" in resp[0]
    assert "stationcount" in resp[0]


def test_request_codecs_with_filters(rb):

    # expected = [{"name": "MP3", "stationcount": 16620}]

    resp = rb.codecs(codec="mp3")
    assert resp[0]["name"] == "MP3"


def test_request_states_with_filters(rb):

    # expected = [{"name": "Parana", "country": "Brazil", "stationcount": 23}]

    resp = rb.states(country="BRAZIL", state="Parana")

    assert "name" in resp[0]
    assert "country" in resp[0]
    assert "stationcount" in resp[0]


def test_request_languages_with_filters(rb):

    # expected = [
    #     {"name": "brazilian portuguese", "stationcount": 8,},
    #     {"name": "portuguese", "stationcount": 638,},
    # ]

    resp = rb.languages(language="portuguese")

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
    resp = rb.tags(tag="drum and bass")

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


def test_request_station_byuuid(rb):

    resp = rb.station_by_uuid("96062a7b-0601-11e8-ae97-52543be04c81")

    super_set = {
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
        "votes",
        "lastchangetime",
        "codec",
        "bitrate",
        "hls",
        "lastcheckok",
        "lastchecktime",
        "lastcheckoktime",
        "lastlocalchecktime",
        "clicktimestamp",
        "clickcount",
        "clicktrend",
    }
    response_keys = resp[0].keys()

    assert len(resp[0]) == len(response_keys)
    assert super_set.issuperset(response_keys)

