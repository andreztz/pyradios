import unittest

from tests.endpoint_builder import TestEndPoint


def load_suit():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestEndPoint)
    return suite
