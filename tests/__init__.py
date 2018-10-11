import unittest

from tests.api import TestEndPoint


def load_suit():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestEndPoint)
    return suite

