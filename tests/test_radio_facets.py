import pytest
import sys
import logging

from pyradios import RadioBrowser, RadioFacets


log = logging.getLogger("pyradios")



@pytest.fixture
def rb():
    _rb = RadioBrowser()
    return _rb


def test_facet_init_and_narrow(rb):
    log.debug("started")
    rf = RadioFacets(rb)
    assert rf.result is not None, "expecting to have a result-set"
    assert len(rf) > 0, "expecting the no-query result-set to not be empty"


def test_facet_narrow_broaden(rb):
    log.debug("started")
    limit = 10
    qry_be = dict(countrycode="be")  # the center of the world
    qry_nl = dict(language="dutch")  # spoken in be as is french and german
    qry_lim = dict(limit=limit)    # size limit
    qry_klara = dict(name="klara", name_exact=False)  # radiostation in be
    qry_class = dict(tag="classical")

    # start off with a set of belgian stations
    rfbe = RadioFacets(rb, **qry_be)
    assert len(rfbe) > limit, f"execpting > {limit} stations in .be"
    log.debug(f"found {len(rfbe)} stations matching {rfbe.filter}")

    # narrow down to dutch speaking stations
    rfbenl = rfbe.narrow(**qry_nl)
    assert len(rfbenl) > limit, f"execpting > {limit} nl stations in .be"
    assert len(rfbenl) < len(rfbe), f"expecting set to be < {len(rfbe)}"
    log.debug(f"found {len(rfbenl)} stations matching {rfbenl.filter}")

    # add the size limit
    rfbenllim = rfbenl.narrow(**qry_lim)
    assert len(rfbenllim) == limit, f"expecting set to be size {limit}"
    log.debug(f"found {len(rfbenllim)} stations matching {rfbenllim.filter}")

    # further narrow to name-matches
    rfbenlklaralim = rfbenllim.narrow(**qry_klara)
    assert 0 < len(rfbenlklaralim) < limit, f"expecting size between 0 < {limit}"
    log.debug(f"found {len(rfbenlklaralim)} stations " +
        f"matching {rfbenlklaralim.filter}")

    rfklaralim = rfbenlklaralim.broaden(tuple({ **qry_be, **qry_nl}.keys()))
    assert len(rfbenlklaralim) <= len(rfklaralim) < limit
    log.debug(f"found {len(rfklaralim)} stations " +
        f"matching {rfklaralim.filter}")



def enable_stdout_logging():
    log.setLevel(logging.DEBUG)
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)


if __name__ == "__main__":
    enable_stdout_logging()
    print(
        "Running tests in ",
        __file__,
        "with -v(erbose) and -s(no stdout capturing) ",
        "and DEBUG logging")
    sys.exit(pytest.main(["-v", "-s",  __file__]))
