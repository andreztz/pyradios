import unittest
from collections import OrderedDict
from unittest import mock
from urllib import response

from pyradios.radios import RadioBrowser, build_endpoint, build_mask


class TestRadioBrowser(unittest.TestCase):
    def setUp(self):
        self.url_base = "http://www.radio-browser.info/webservice/"
        self.headers = {
            "content-type": "application/json",
            "User-Agent": "pyradios/dev",
        }
        self.rb = RadioBrowser()
        self.mock_response = mock.Mock(status_code=200)

    def test_build_mask_one(self):
        kwargs = {
            "searchterm": "100",
            "format": "json",
            "endpoint": "stations/byid",
        }
        ordered = OrderedDict()
        ordered["format"] = kwargs.get("format")
        ordered["endpoint"] = kwargs.get("endpoint")
        ordered["searchterm"] = kwargs.get("searchterm")

        expected_result = "{format}/{endpoint}/{searchterm}/"
        self.assertEqual(build_mask(ordered), expected_result)

    def test_build_mask_two(self):
        kwargs = {"format": "xml", "filter": "aac", "endpoint": "codecs"}
        ordered = OrderedDict()
        ordered["format"] = kwargs.get("format")
        ordered["endpoint"] = kwargs.get("endpoint")
        ordered["filter"] = kwargs.get("filter")
        expected_result = "{format}/{endpoint}/{filter}/"

        self.assertEqual(build_mask(ordered), expected_result)

    """ tests build endpoins """

    def test_build_endpoint_with_codecs(self):
        expected_result = self.url_base + "json/codecs"
        url = build_endpoint(endpoint="codecs")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_languages(self):
        expected_result = self.url_base + "xml/languages"
        url = build_endpoint(endpoint="languages", format="xml")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_codecs_filter_format(self):
        expected_result = self.url_base + "xml/codecs/aac"
        url = build_endpoint(endpoint="codecs", format="xml", filter="aac")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_codecs_filter(self):
        expected_result = self.url_base + "json/codecs/mp3"
        url = build_endpoint(endpoint="codecs", filter="mp3")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_states(self):
        expected_result = self.url_base + "json/states"
        url = build_endpoint(endpoint="states")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_states_format(self):
        expected_result = self.url_base + "xml/states"
        url = build_endpoint(endpoint="states", format="xml")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_states_fomat_country(self):
        expected_result = self.url_base + "xml/states/brasil/"
        url = build_endpoint(endpoint="states", format="xml", country="brasil")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_states_filter_coutry(self):
        expected_result = self.url_base + "json/states/brazil/parana"
        url = build_endpoint(
            endpoint="states", country="brazil", filter="parana"
        )
        self.assertEqual(url, expected_result)

    """ stations by """

    def test_build_endpoint_stations(self):
        expected_result = self.url_base + "json/stations"
        url = build_endpoint(endpoint="stations")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_stations_byid(self):
        expected_result = self.url_base + "json/stations/byid/87019"
        url = build_endpoint(endpoint="stations/byid", by="87019")
        self.assertEqual(url, expected_result)

    """ playable station url """

    def test_build_endpoint_playable_stations_url(self):
        expected_result = self.url_base + "v2/json/url/87019"
        url = build_endpoint(endpoint="url", by="87019", ver="v2")
        self.assertEqual(url, expected_result)

    @mock.patch("pyradios.radios.requests.get")
    def test_countries_response(self, mget):
        expected_result = [
            {"name": "58", "value": "58", "stationcount": "1"},
            {"name": "AAA", "value": "AAA", "stationcount": "6"},
            {
                "name": "Afghanistan",
                "value": "Afghanistan",
                "stationcount": "3",
            },
            {"name": "Albania", "value": "Albania", "stationcount": "12"},
            {"name": "Alberta", "value": "Alberta", "stationcount": "1"},
            {"name": "Algeria", "value": "Algeria", "stationcount": "58"},
            {
                "name": "American Samoa",
                "value": "American Samoa",
                "stationcount": "1",
            },
        ]
        self.mock_response.json.return_value = expected_result
        mget.return_value = self.mock_response

        response = self.rb.countries()
        url = build_endpoint(endpoint="countries")
        mget.assert_called_once_with(url, headers=self.headers, params={})
        self.assertEqual(response, expected_result)

    @mock.patch("pyradios.radios.requests.get")
    def test_countries_response(self, mget):
        expected_result = [
            {"name": "Brazil", "value": "Brazil", "stationcount": "382"}
        ]
        self.mock_response.json.return_value = expected_result
        mget.return_value = self.mock_response

        response = self.rb.countries("Brazil")
        url = build_endpoint(endpoint="countries", filter="Brazil")
        mget.assert_called_once_with(url, headers=self.headers, params={})
        self.assertEqual(response, expected_result)

    @mock.patch("pyradios.radios.requests.get")
    def test_states_response(self, mget):
        expected_result = [
            {
                "name": "Alberta",
                "value": "Alberta",
                "country": "Canada",
                "stationcount": "111",
            },
            {
                "name": "Baden-Württemberg",
                "value": "Baden-Württemberg",
                "country": "Deutschland",
                "stationcount": "3",
            },
            {
                "name": "Baden-Württemberg",
                "value": "Baden-Württemberg",
                "country": "Germany",
                "stationcount": "76",
            },
            {
                "name": "Bergdietikon",
                "value": "Bergdietikon",
                "country": "Switzerland",
                "stationcount": "1",
            },
            {
                "name": "Bergen",
                "value": "Bergen",
                "country": "Norway",
                "stationcount": "2",
            },
            {
                "name": "Berkshire",
                "value": "Berkshire",
                "country": "United Kingdom",
                "stationcount": "1",
            },
            {
                "name": "Berlin",
                "value": "Berlin",
                "country": "Deutschland",
                "stationcount": "1",
            },
            {
                "name": "Berlin",
                "value": "Berlin",
                "country": "Germany",
                "stationcount": "233",
            },
            {
                "name": "Berlin-Brandenburg",
                "value": "Berlin-Brandenburg",
                "country": "Germany",
                "stationcount": "1",
            },
            {
                "name": "Berlin/Brandenburg",
                "value": "Berlin/Brandenburg",
                "country": "Deutschland",
                "stationcount": "1",
            },
            {
                "name": "Bern",
                "value": "Bern",
                "country": "Switzerland",
                "stationcount": "21",
            },
            {
                "name": "Brandenburg Oberhavel",
                "value": "Brandenburg Oberhavel",
                "country": "Deutschland",
                "stationcount": "1",
            },
            {
                "name": "Humberside",
                "value": "Humberside",
                "country": "United Kingdom",
                "stationcount": "2",
            },
            {
                "name": "Kronoberg",
                "value": "Kronoberg",
                "country": "Sweden",
                "stationcount": "3",
            },
            {
                "name": "La Libertad",
                "value": "La Libertad",
                "country": "El Salvador",
                "stationcount": "1",
            },
            {
                "name": "Oberoesterreich",
                "value": "Oberoesterreich",
                "country": "Austria",
                "stationcount": "1",
            },
            {
                "name": "Szabolcs-Szatmár-Bereg",
                "value": "Szabolcs-Szatmár-Bereg",
                "country": "Hungary",
                "stationcount": "4",
            },
            {
                "name": "Tønsberg",
                "value": "Tønsberg",
                "country": "Norway",
                "stationcount": "1",
            },
            {
                "name": "Vorarlberg",
                "value": "Vorarlberg",
                "country": "Austria",
                "stationcount": "7",
            },
            {
                "name": "Красноярский край, Шушенское, Siberia",
                "value": "Красноярский край, Шушенское, Siberia",
                "country": "Russia",
                "stationcount": "1",
            },
        ]

        self.mock_response.json.return_value = expected_result
        mget.return_value = self.mock_response
        response = self.rb.states("ber")
        url = build_endpoint(endpoint="states", filter="ber")
        mget.assert_called_once_with(url, headers=self.headers, params={})
        self.assertEqual(response, expected_result)

    @mock.patch("pyradios.radios.requests.get")
    def test_states_with_country_response(self, mget):
        expected_result = [
            {
                "name": "Bavaria",
                "value": "Bavaria",
                "country": "Germany",
                "stationcount": "180",
            }
        ]
        self.mock_response.json.return_value = expected_result
        mget.return_value = self.mock_response

        response = self.rb.states("Bavaria", country="Germany")

        url = build_endpoint(
            endpoint="states", filter="Bavaria", coutry="Germany"
        )
        mget.assert_called_once_with(url, headers=self.headers, params={})
        self.assertEqual(response, expected_result)

    @mock.patch("pyradios.radios.requests.get")
    def test_search_response(self, mget):
        expected_result = [
            {
                "id": "87019",
                "changeuuid": "9615f296-0601-11e8-ae97-52543be04c81",
                "stationuuid": "9615f293-0601-11e8-ae97-52543be04c81",
                "name": "TrancePulse FM",
                "url": "http://sirius.shoutca.st:8878/stream",
                "homepage": "http://www.trancepulsefm.com/",
                "favicon": "http://www.trancepulsefm.com/files/theme/favicon.ico",
                "tags": "edm,electronic,dance,trance",
                "country": "Ireland",
                "state": "",
                "language": "English",
                "votes": "46",
                "negativevotes": "0",
                "lastchangetime": "2017-11-15 11:04:06",
                "ip": "195.39.210.66",
                "codec": "MP3",
                "bitrate": "160",
                "hls": "0",
                "lastcheckok": "1",
                "lastchecktime": "2018-09-06 11:04:53",
                "lastcheckoktime": "2018-09-06 11:04:53",
                "clicktimestamp": "2018-09-06 23:52:29",
                "clickcount": "6",
                "clicktrend": "5",
            }
        ]
        self.mock_response.json.return_value = expected_result
        mget.return_value = self.mock_response

        params = {"name": "TrancePulse FM"}
        response = self.rb.station_search(params=params)

        url = build_endpoint(endpoint="stations/search")
        mget.assert_called_once_with(url, headers=self.headers, params=params)

        self.assertEqual(response, expected_result)


if __name__ == "__main__":
    unittest.main()
