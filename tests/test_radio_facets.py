import pytest

from pyradios import RadioBrowser, RadioFacets


BASE_URL = "https://nl1.api.radio-browser.info/"


@pytest.fixture
def rb():
    _rb = RadioBrowser()
    _rb.base_url = BASE_URL
    return _rb


def test_facet_init(rb):
    rf = RadioFacets(rb)
    assert rf.result is not None, "there should be a result-set"
    assert len(rf) > 0, "the no-query result-set should not be empty"
