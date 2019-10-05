import unittest

test_loader = unittest.defaultTestLoader
test_runner = unittest.TextTestRunner()
test_suite = test_loader.discover(".")
test_runner.run(test_suite)
