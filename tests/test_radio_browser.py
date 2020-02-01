# test schema https://medium.com/grammofy/testing-your-python-api-app-with-json-schema-52677fe73351
# TODO Rename this file to test_radio_browser_schemas.py
# TODO https://github.com/kislyuk/ensure

import pytest

from pyradios import RadioBrowser


@pytest.fixture
def rb():
    return RadioBrowser()


def test_request_countrycodes(rb):
    """
    expected = [{"name": "AD", "stationcount": 5, {... ]
    """
    response = rb.countrycodes()
    assert len(response[0].keys()) == 2
    assert "name" in response[0]
    assert "stationcount" in response[0]

def test_request_countrycodes_with_filters(rb):
    """
    expected = [{"name": "BR", "stationcount": 607}]
    """
    response = rb.countrycodes(filter_by_code="BR")
    assert response[0]["name"] == "BR"

def test_request_codecs(rb):
    """
    expected = [{"name": "MP3", "stationcount": 16620}]
    """
    response = rb.codecs()
    assert isinstance(response, list)
    assert "name" in response[0]
    assert "stationcount" in response[0]

def test_request_codecs_with_filters(rb):
    """
    expected = [{"name": "MP3", "stationcount": 16620}]
    """
    response = rb.codecs(filter_by_codec="mp3")
    assert response[0]["name"] == "MP3"


def test_request_states_with_filters(rb):
    """
    expected = [
        {"name": "Parana", "country": "Brazil", "stationcount": 23}
    ]
    """
    response = rb.states(
        filter_by_country="BRAZIL", filter_by_state="Parana"
    )
    assert isinstance(response, list)
    assert "name" in response[0]
    assert "country" in response[0]
    assert "stationcount" in response[0]


def test_request_languages_with_filters(rb):
    """"
    expected = [
        {
            "name": "brazilian portuguese",
            "stationcount": 8,

        },
        {
            "name": "portuguese",
            "stationcount": 638,

        },
    ]
    """
    response = rb.languages(filter_by_language="portuguese")
    assert isinstance(response, list)
    assert "name" in response[0]
    assert "stationcount" in response[0]


def test_request_tags_with_filters(rb):
    """
    expected = [
        {
            "name": "drum and bass",
            "stationcount": 73,
        }
    ]
    """
    response = rb.tags(filter_by_tag="drum and bass")
    assert isinstance(response, list)
    assert "name" in response[0]
    assert "stationcount" in response[0]


def test_request_playable_station(rb):
    """
        expected = {'ok': True,
        'message': 'retrieved station url',
        'stationuuid': '96062a7b-0601-11e8-ae97-52543be04c81',
        'name': 'BBC Radio 1',
        'url': 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p'}

    """
    response = rb.playable_station('96062a7b-0601-11e8-ae97-52543be04c81')
    assert isinstance(response, dict)
    assert "ok" in response
    assert "message" in response
    assert "stationuuid" in response
    assert "name" in response
    assert "url" in response
    


def test_request_station(rb):
    """
        expected = [{'changeuuid': '4f7e4097-4354-11e8-b74d-52543be04c81',
        'stationuuid': '96062a7b-0601-11e8-ae97-52543be04c81',
        'name': 'BBC Radio 1',
        'url': 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p',
        'url_resolved': 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p',
        'homepage': 'http://www.bbc.co.uk/radio1/',
        'favicon': 'https://cdn-radiotime-logos.tunein.com/s24939q.png',
        'tags': 'bbc,indie,entertainment,music,rock,pop',
        'country': 'United Kingdom',
        'countrycode': 'GB',
        'state': '',
        'language': 'english',
        'votes': 5018,
        'lastchangetime': '2020-01-19 13:00:12',
        'codec': 'MP3',
        'bitrate': 128,
        'hls': 0,
        'lastcheckok': 1,
        'lastchecktime': '2020-02-02 19:49:00',
        'lastcheckoktime': '2020-02-02 19:49:00',
        'lastlocalchecktime': '2020-02-02 09:19:00',
        'clicktimestamp': '2020-02-02 21:29:26',
        'clickcount': 2735,
        'clicktrend': 4}]

    """
    response = rb.stations_byuuid("96062a7b-0601-11e8-ae97-52543be04c81")
    keys = ['changeuuid', 'stationuuid', 'name', 'url', 'url_resolved', 'homepage', 'favicon', 'tags', 'country', 'countrycode', 'state', 'language', 'votes', 'lastchangetime', 'codec', 'bitrate', 'hls', 'lastcheckok', 'lastchecktime', 'lastcheckoktime', 'lastlocalchecktime', 'clicktimestamp', 'clickcount', 'clicktrend']
    response_keys = response[0].keys()

    assert isinstance(response, list)
    assert len(response[0]) == len(keys)

    for key in keys:
        assert key in response_keys
    
