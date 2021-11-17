from pyradios.radios import RadioBrowser
from itertools import chain
from functools import reduce
from collections import defaultdict
import logging


log = logging.getLogger("pyradios")


class RadioFacets:
    FACETS = ["tags", "countrycode", "language", "state", "codec"]

    def __init__(self, rb, **params):
        assert rb is not None, "facets requires a RadioBrowser service to call"
        assert isinstance(rb, RadioBrowser), "RadioBrowser service wrong type"
        self.rb = rb
        self.filter = params if params is not None else dict()
        self._fetch_and_calc()

    def __repr__(self):
        typename = type(self).__name__
        args = ['{}={!r}'.format(k, v) for k, v in self.filter.items()]
        return "%s(%s)" % (typename, ', '.join(args))

    def _fetch_and_calc(self):
        self.result = self.rb.search(**self.filter)
        self.facets = dict()

        def facetcount(facets, item):
            for f in facets.keys():
                for fv in item[f].split(','):
                    facets[f][fv] += 1  # tracks empty facet-values as ''
            return facets

        init = {f: defaultdict(int) for f in RadioFacets.FACETS}
        captured_hist_per_facet = reduce(facetcount, self.result, init)
        for f in captured_hist_per_facet.keys():
            # unsorted facet histogram
            usf_hist = captured_hist_per_facet[f].items()
            # order histogram items from high to low
            sf_hist = sorted(usf_hist, key=lambda i: i[1], reverse=True)
            # pluralize the key if needed
            fpub = f if f[-1] == 's' else f + "s"
            self.facets[fpub] = [{"name": k, "count": v} for k, v in sf_hist]

    def __getattr__(self, key):
        if key in self.facets:
            return self.facets[key]
        # else
        return getattr(self, key)

    def __len__(self):
        return len(self.result)

    def _derived(self, **filter):
        return RadioFacets(self.rb, **filter)

    def narrow(self, **pars2add):
        log.debug("flatten ++ params(%s)" % pars2add)
        filter = dict(self.filter)  # clone the dict
        filter.update(pars2add)
        return self._derived(**filter)

    def broaden(self, *keys2rm, **pars2rm):
        log.debug("broaden -- keys(%s) and params(%s)" % (keys2rm, pars2rm))
        filter = dict(self.filter)
        for k in chain(keys2rm, pars2rm.keys()):
            filter.pop(k, None)
        return self._derived(**filter)
