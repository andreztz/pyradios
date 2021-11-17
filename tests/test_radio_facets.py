import pytest
import sys
import logging
import random
import os
from functools import reduce


from pyradios import RadioBrowser, RadioFacets


log = logging.getLogger("pyradios")


@pytest.fixture
def rb():
    _rb = RadioBrowser()
    return _rb


def partition(predicate, iterable):
    """
    splits the items in iter into two partitions based on predicate() outcome
      True  --> into first list of returned tuple
      False --> into second list
    """
    def split(parts, item):
        parts[int(not predicate(item))].append(item)
        return parts
    return reduce(split, iterable, ([], []))


def test_facet_init(rb):
    log.info("test facet_init started")
    rf = RadioFacets(rb)
    assert rf.result is not None, "expecting to have a result-set"
    assert len(rf) > 0, "expecting the no-query result-set to not be empty"

    # split the set in stations with and without tags
    parts = partition(lambda s: len(s['tags']) == 0, rf.result)

    for part in parts:
        anystation = random.choice(part)
        log.debug(f"one rsult == {anystation}")

        assert rf.tags is not None, "expecting a tags histogram"
        anytag = random.choice(anystation['tags'].split(','))
        foundtags = list(filter(lambda t: t['name'] == anytag, rf.tags))
        assert len(foundtags) == 1, f"tag '{anytag}' not in the result-set"
        assert foundtags[0]['count'] > 1, f"not even one match '{anytag}'"

    assert rf.countrycodes is not None, "expecting a contrycode histogram"
    assert rf.languages is not None, "expecting a language histogram"
    assert rf.codecs is not None, "expecting a codec histogram"
    assert rf.states is not None, "expecting a state histogram"

    log.debug(f"facet repr == {rf}")
    log.debug(f"facet top tags == {rf.tags[:10]}")
    log.debug(f"facet top langs == {rf.languages[:10]}")
    log.debug(f"facet top codecs == {rf.codecs[:10]}")
    log.debug(f"facet top ctrys == {rf.countrycodes[:10]}")


def test_facet_narrow_broaden(rb):
    log.info("test facet_narrow_broaden started")
    limit = 10                         # not make this smaller then 5
    qry_be = dict(countrycode="be")    # the center of the world
    qry_nl = dict(language="dutch")    # spoken in .be, as is french and german
    qry_lim = dict(limit=limit)        # size limit
    qry_klara = dict(name="klara", name_exact=False)  # radiostation in be
    qry_clss = dict(tag="classical")   # tag that will fit radio klara

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
    assert 0 < len(rfbenlklaralim) < limit, f"expecting 0 < size < {limit}"
    log.debug(f"found {len(rfbenlklaralim)} stations " +
              f"matching {rfbenlklaralim.filter}")

    # broaden up by skipping the country and language constraint
    rfklaralim = rfbenlklaralim.broaden(**qry_be, **qry_nl)
    assert len(rfbenlklaralim) <= len(rfklaralim) < limit
    log.debug(f"found {len(rfklaralim)} stations " +
              f"matching {rfklaralim.filter}")

    # exchange the limit constraint with a tag constraint
    rfklaraclss = rfklaralim.broaden(tuple(qry_lim.keys())).narrow(**qry_clss)
    assert len(rfklaraclss) <= len(rfklaralim)
    log.debug(f"found {len(rfklaraclss)} stations " +
              f"matching {rfklaraclss.filter}")


def enable_stdout_logging():
    if 'PYTEST_LOG' in os.environ:
        loglevel = logging.getLevelName(os.environ['PYTEST_LOG'].upper())
        log.setLevel(loglevel)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(loglevel)
        msg_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(msg_fmt)
        handler.setFormatter(formatter)
        log.addHandler(handler)


if __name__ == "__main__":
    enable_stdout_logging()
    log.info(
        "Running tests in ",
        __file__,
        "with -v(erbose) and -s(no stdout capturing) ",
        "and logging to stdout, level controlled by env var ${PYTEST_LOG}")
    sys.exit(pytest.main(["-v", "-s",  __file__]))
