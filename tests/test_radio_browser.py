import re

import httpx
import pytest
import random

from pyradios import RadioBrowser
from pyradios.radios import version


BASE_URL = "https://nl1.api.radio-browser.info/"


def pick_random_station(rb, **params):
    stations = rb.search(**params)
    return random.choice(stations)


def test_version():
    assert version == '2.1.0'


@pytest.fixture
def rb():
    _rb = RadioBrowser()
    _rb.base_url = BASE_URL
    return _rb


def test_request_station_click_counter(rb, mocker):
    expected = {
        "ok": True,
        "message": "retrieved station url",
        "stationuuid": "a726a172-4cc2-4076-b283-a950218ed0c2",
        "name": "BBC Radio 1",
        "url": "https://stream.live.vc.bbcmedia.co.uk/bbc_radio_one",
    }

    with mocker.patch.object(rb.client, 'get', return_value=expected):

        resp = rb.click_counter("a726a172-4cc2-4076-b283-a950218ed0c2")

        assert "ok" in resp
        assert "message" in resp
        assert "stationuuid" in resp
        assert "name" in resp
        assert "url" in resp
        assert resp == expected


def test_request_countrycodes(rb, mocker):
    expected = [{"name": "AD", "stationcount": 5}]

    with  mocker.patch.object(rb.client, 'get', return_value=expected):
        resp = rb.countrycodes()

        assert len(resp) > 0, "at least one country should be in the response"
        assert "name" in resp[0]
        assert "stationcount" in resp[0]
        assert resp == expected


@pytest.mark.vcr()
def test_request_countrycodes_with_filters(rb):
    resp = rb.countrycodes(code="BR")

    assert len(resp) > 0, "at least one country should be in the response"
    assert resp[0]["name"] == "BR"


@pytest.mark.vcr()
def test_request_codecs(rb):
    resp = rb.codecs()

    assert len(resp) > 0, "at least one codec should be in the response"
    assert "name" in resp[0]
    assert "stationcount" in resp[0]


@pytest.mark.vcr()
def test_request_codecs_with_filters(rb):
    """
    This test runs against a subset of the API response, with the sole
    purpose of ensuring the behavior of the filter mechanism of the
    tested method.
    """
    resp = rb.codecs(codec="mp3")

    assert len(resp) == 2
    assert resp[0]["name"] == "MP3", "only one codec should be in the response"


@pytest.mark.vcr()
def test_request_states_with_filters(rb):
    # Note: `country` and `state` should be provided in "titlecased",
    # like so: `str().title()`
    resp = rb.states(country="Brazil", state="Paraná")

    assert len(resp) > 0, "at least one state should be in the response"
    assert "name" in resp[0]
    assert "country" in resp[0]
    assert "stationcount" in resp[0]


@pytest.mark.vcr()
def test_request_languages_with_filters(rb):
    resp = rb.languages(language="portuguese")

    assert len(resp) > 0, "at least one language should be in the response"
    assert "name" in resp[0]
    assert "stationcount" in resp[0]


@pytest.mark.vcr()
def test_request_tags_with_filters(rb):
    resp = rb.tags(tag="Drum and Bass")

    assert len(resp) > 0, "at least one tag should be in the response"
    assert "name" in resp[0]
    assert "stationcount" in resp[0]


@pytest.mark.vcr()
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
