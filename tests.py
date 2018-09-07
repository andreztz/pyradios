import unittest

from pyradios.radios import RadioBrowser, build_mask, build_endpoint

from collections import OrderedDict


class TestRadioBrowser(unittest.TestCase):
    def setUp(self):
        self.url_base = "http://www.radio-browser.info/webservice/"

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


if __name__ == "__main__":
    unittest.main()
