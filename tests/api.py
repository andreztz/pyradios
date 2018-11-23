import unittest
from pyradios.api import EndPoints


class TestEndPoint(unittest.TestCase):
    def setUp(self):
        self.endpoints = EndPoints()

    def test_countries(self):
        expected_result = (
            "http://www.radio-browser.info/webservice/json/countries"
        )
        url = self.endpoints.countries()
        self.assertEqual(url, expected_result)

    def test_countries_with_param(self):
        expected_result = (
            "http://www.radio-browser.info/webservice/json/countries/Brazil"
        )
        filter_ = "Brazil"
        url = self.endpoints.countries(filter_)
        self.assertEqual(url, expected_result)

    def test_codecs(self):
        expected_result = "http://www.radio-browser.info/webservice/json/codecs"
        url = self.endpoints.codecs()
        self.assertEqual(url, expected_result)

    def test_codecs_with_param(self):
        expected_result = (
            "http://www.radio-browser.info/webservice/json/codecs/mp3"
        )
        filter_ = "mp3"
        url = self.endpoints.codecs(filter_)
        self.assertEqual(url, expected_result)

    def test_states(self):
        expected_result = "http://www.radio-browser.info/webservice/json/states"
        url = self.endpoints.states()
        self.assertEqual(url, expected_result)

    def test_states_with_params(self):
        # falha quando params ñ são nomeados
        expected_result = (
            "http://www.radio-browser.info/webservice/json/states/German/ber"
        )
        filter_ = "ber"
        country = "German"
        url = self.endpoints.states(filter_=filter_, country=country)
        self.assertEqual(url, expected_result)

    def test_languages(self):
        expected_result = (
            "http://www.radio-browser.info/webservice/json/languages"
        )
        url = self.endpoints.languages()
        self.assertEqual(url, expected_result)

    def test_languages_with_param(self):
        expected_result = (
            "http://www.radio-browser.info/webservice/json/languages/ger"
        )
        filter_ = "ger"
        url = self.endpoints.languages(filter_)
        self.assertEqual(url, expected_result)

    def test_tags(self):
        expected_result = "http://www.radio-browser.info/webservice/json/tags"
        url = self.endpoints.tags()
        self.assertEqual(url, expected_result)

    def test_tags_with_param(self):
        expected_result = (
            "http://www.radio-browser.info/webservice/json/tags/jazz"
        )
        filter_ = "jazz"
        url = self.endpoints.tags(filter_)
        self.assertEqual(url, expected_result)

    def test_stations(self):
        expected_result = (
            "http://www.radio-browser.info/webservice/json/stations"
        )
        url = self.endpoints.stations()
        self.assertEqual(url, expected_result)

    def test_stations_byid(self):
        expected_result = (
            "http://www.radio-browser.info/webservice/json/stations/byid/0000"
        )
        url = self.endpoints.stations_byid("0000")
        self.assertEqual(url, expected_result)

    def test_stations_byuuid(self):
        expected_result = (
            "http://www.radio-browser.info/webservice/json/stations/byuuid/0000"
        )
        url = self.endpoints.stations_byuuid("0000")
        self.assertEqual(url, expected_result)

    def test_stations_byname(self):
        expected_result = (
            "http://www.radio-browser.info/webservice/json/stations/byname/jazz"
        )
        url = self.endpoints.stations_byname("jazz")
        self.assertEqual(url, expected_result)

    # def test_stations_byid(self):
    #     expected_result = ""
    #     url = ""
    #     self.assertEqual(url, expected_result)

    # def test_stations_byid(self):
    #     expected_result = ""
    #     url = ""
    #     self.assertEqual(url, expected_result)

    # def test_stations_byid(self):
    #     expected_result = ""
    #     url = ""
    #     self.assertEqual(url, expected_result)

    # def test_stations_byid(self):
    #     expected_result = ""
    #     url = ""
    #     self.assertEqual(url, expected_result)

    def test_playable_station(self):
        expected_result = (
            "http://www.radio-browser.info/webservice/v2/json/url/123"
        )
        stationid = "123"
        url = self.endpoints.playable_station(stationid)
        self.assertEqual(url, expected_result)

    def test_station_search(self):
        expected_result = (
            "http://www.radio-browser.info/webservice/json/stations/search"
        )
        url = self.endpoints.station_search()
        self.assertEqual(url, expected_result)
