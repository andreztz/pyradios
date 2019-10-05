import unittest
from unittest.mock import patch

from pyradios.radios import RadioBrowser


class TestRadioBrowser(unittest.TestCase):
    def setUp(self):
        self.rb = RadioBrowser()

    def test_request_codecs(self):

        resp = self.rb.codecs()

