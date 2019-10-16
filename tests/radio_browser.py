import unittest
from unittest.mock import patch

from pyradios.radios import RadioBrowser


class TestRadioBrowser(unittest.TestCase):
    def setUp(self):
        self.rb = RadioBrowser()

    def test_request_countrycodes(self):
        expected = [{"name": "BR", "stationcount": 607}]
        response = self.rb.countrycodes()
        self.assertIsInstance(response, list)
        self.assertTupleEqual(
            tuple(expected[0].keys()), tuple(response[-1].keys())
        )

    def test_request_countrycodes_with_filters(self):
        expected = [{"name": "BR", "stationcount": 607}]
        response = self.rb.countrycodes(filter_by_code="BR")
        self.assertEqual(expected[0]["name"], response[0]["name"])

    def test_request_codecs(self):
        expected = [{"name": "MP3", "stationcount": 16620}]
        response = self.rb.codecs()
        self.assertIsInstance(response, list)
        self.assertTrue(response)
        self.assertTupleEqual(
            tuple(expected[0].keys()), tuple(response[0].keys())
        )

    def test_request_codecs_with_filters(self):
        expected = [{"name": "MP3", "stationcount": 16620}]
        response = self.rb.codecs(filter_by_codec="mp3")
        self.assertIsInstance(response, list)
        self.assertTrue(response)
        self.assertTupleEqual(
            tuple(expected[0].keys()), tuple(response[0].keys())
        )
        self.assertIn(expected[0]["name"], response[0].values())

    def test_request_states_with_filters(self):
        expected = [
            {"name": "Parana", "country": "Brazil", "stationcount": 23}
        ]
        response = self.rb.states(
            filter_by_country="BRAZIL", filter_by_state="Parana"
        )
        self.assertIsInstance(response, list)
        self.assertTupleEqual(
            tuple(expected[0].keys()), tuple(response[0].keys())
        )
        self.assertIn(expected[0]["name"], response[0].values())
        self.assertIn(expected[0]["country"], response[0].values())

    def test_request_languages_with_filters(self):
        expected = [
            {
                "name": "brazilian portuguese",
                "stationcount": 8,
                "stationcountworking": 0,
            },
            {
                "name": "portuguese",
                "stationcount": 638,
                "stationcountworking": 0,
            },
        ]
        response = self.rb.languages(filter_by_language="portuguese")
        self.assertIsInstance(response, list)
        self.assertTrue(response)
        self.assertTupleEqual(
            tuple(expected[0].keys()), tuple(response[0].keys())
        )

    def test_request_tags_with_filters(self):
        expected = [
            {
                "name": "drum and bass",
                "stationcount": 73,
                "stationcountworking": 0,
            }
        ]
        response = self.rb.tags(filter_by_tag="drum and bass")
        self.assertIsInstance(response, list)
        self.assertTrue(response)
        self.assertTupleEqual(
            tuple(expected[0].keys()), tuple(response[0].keys())
        )
        self.assertEqual(expected[0]["name"], response[0]["name"])
