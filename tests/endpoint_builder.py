import unittest

from pyradios.radios import EndPointBuilder


class TestEndPoint(unittest.TestCase):
    def setUp(self):
        self.builder = EndPointBuilder(fmt="json")

    def test_countries(self):
        expected = "json/countries"
        result = self.builder.produce_endpoint(endpoint="countries")
        self.assertEqual(result, expected)

    def test_countries_with_filter(self):
        expected = "json/countries/Brazil"
        result = self.builder.produce_endpoint(endpoint="countries", filter="Brazil")
        self.assertEqual(result, expected)

    def test_codecs(self):
        expected = "json/codecs"
        result = self.builder.produce_endpoint(endpoint="codecs")
        self.assertEqual(result, expected)

    def test_codecs_with_filter(self):
        expected = "json/codecs/mp3"
        result = self.builder.produce_endpoint(endpoint="codecs", filter="mp3")
        self.assertEqual(result, expected)

    def test_states(self):
        expected = "json/states"
        result = self.builder.produce_endpoint(endpoint="states")
        self.assertEqual(result, expected)

    def test_states_with_filters(self):
        # falha quando params ñ são nomeados
        expected = "json/states/German/ber"
        result = self.builder.produce_endpoint(
            endpoint="states", filter="ber", country="German"
        )
        self.assertEqual(result, expected)

    def test_languages(self):
        expected = "json/languages"
        result = self.builder.produce_endpoint(endpoint="languages")
        self.assertEqual(result, expected)

    def test_languages_with_param(self):
        expected = "json/languages/ger"
        result = self.builder.produce_endpoint(endpoint="languages", filter="ger")
        self.assertEqual(result, expected)

    def test_tags(self):
        expected = "json/tags"
        result = self.builder.produce_endpoint(endpoint="tags")
        self.assertEqual(result, expected)

    #
    def test_tags_with_param(self):
        expected = "json/tags/jazz"
        result = self.builder.produce_endpoint(endpoint="tags", filter="jazz")
        self.assertEqual(result, expected)

    #
    def test_stations(self):
        expected = "json/stations"
        result = self.builder.produce_endpoint(endpoint="stations")
        self.assertEqual(result, expected)

    def test_stations_byid(self):
        expected = "json/stations/byid/0000"
        result = self.builder.produce_endpoint(
            endpoint="stations", by="byid", search_term="0000"
        )
        self.assertEqual(result, expected)

    def test_stations_byuuid(self):
        expected = "json/stations/byuuid/0000"
        result = self.builder.produce_endpoint(
            endpoint="stations", by="byuuid", search_term="0000"
        )
        self.assertEqual(result, expected)

    def test_stations_byname(self):
        expected = "json/stations/byname/jazz"
        result = self.builder.produce_endpoint(
            endpoint="stations", by="byname", search_term="jazz"
        )
        self.assertEqual(result, expected)

    def test_playable_station(self):
        expected = "v2/json/url/123"
        result = self.builder.produce_endpoint(
            endpoint="playable_station", station_id=123, ver="v2"
        )
        self.assertEqual(result, expected)

    def test_station_search(self):
        expected = "json/stations/search"
        result = self.builder.produce_endpoint(endpoint="station_search")
        self.assertEqual(result, expected)
