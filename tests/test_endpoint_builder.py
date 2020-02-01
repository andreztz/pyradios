import pytest

from pyradios.radios import EndPointBuilder

@pytest.fixture
def builder():
    return EndPointBuilder(fmt="json")

def test_countrycodes(builder):
    expected = "json/countrycodes"
    result = builder.produce_endpoint(endpoint="countrycodes")
    assert result == expected
    

def test_countrycodes_with_filter(builder):
    expected = "json/countrycodes/BR"
    result = builder.produce_endpoint(
        endpoint="countrycodes", filter="BR"
    )
    assert result == expected

def test_codecs(builder):
    expected = "json/codecs"
    result = builder.produce_endpoint(endpoint="codecs")
    assert result == expected

def test_codecs_with_filter(builder):
    expected = "json/codecs/mp3"
    result = builder.produce_endpoint(endpoint="codecs", filter="mp3")
    assert result == expected

def test_states(builder):
    expected = "json/states"
    result = builder.produce_endpoint(endpoint="states")
    assert result == expected

def test_states_with_filters(builder):
    # falha quando params ñ são nomeados
    expected = "json/states/German/ber"
    result = builder.produce_endpoint(
        endpoint="states", filter="ber", country="German"
    )
    assert result == expected

def test_languages(builder):
    expected = "json/languages"
    result = builder.produce_endpoint(endpoint="languages")
    assert result == expected

def test_languages_with_param(builder):
    expected = "json/languages/ger"
    result = builder.produce_endpoint(
        endpoint="languages", filter="ger"
    )
    assert result == expected

def test_tags(builder):
    expected = "json/tags"
    result = builder.produce_endpoint(endpoint="tags")
    assert result == expected

#
def test_tags_with_param(builder):
    expected = "json/tags/jazz"
    result = builder.produce_endpoint(endpoint="tags", filter="jazz")
    assert result == expected

#
def test_stations(builder):
    expected = "json/stations"
    result = builder.produce_endpoint(endpoint="stations")
    assert result == expected

def test_stations_byuuid(builder):
    expected = "json/stations/byuuid/0000"
    result = builder.produce_endpoint(
        endpoint="stations", by="byuuid", search_term="0000"
    )
    assert result == expected

def test_stations_byname(builder):
    expected = "json/stations/byname/jazz"
    result = builder.produce_endpoint(
        endpoint="stations", by="byname", search_term="jazz"
    )
    assert result == expected

def test_playable_station(builder):
    expected = "v2/json/url/123"
    result = builder.produce_endpoint(
        endpoint="playable_station", station_id=123, ver="v2"
    )
    assert result == expected

def test_station_search(builder):
    expected = "json/stations/search"
    result = builder.produce_endpoint(endpoint="station_search")
    assert result == expected

