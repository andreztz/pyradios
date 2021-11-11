from pyradios.radios import RadioBrowser
from itertools import chain
import logging


log = logging.getLogger("pyradios")


class RadioFacets:
    FACETS = ["tags", "countrycodes", "languages", "states", "codecs"]

    def __init__(self, rb, **params):
        assert rb is not None, "facets requires a RadioBrowser service to call"
        assert isinstance(rb, RadioBrowser), "RadioBrowser service wrong type"
        self.rb = rb
        self.filter = params if params is not None else dict()
        self._fetch_and_calc()

    def __repr__(self):
        typename = type(self).__name__
        filter_repr = ['{}={!r}'.format(k, v) for k, v in self.filter.items()]
        return "%s(%s)" % (typename, ', '.join(filter_repr))

    def _fetch_and_calc(self):
        self.result = self.rb.search(**self.filter)
        # todo - calculate counts and histograms on everything

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

    # todo various ideas in https://github.com/andreztz/pyradios/issues/32
    #     fb = rb.facets(**query)
    #     fb.result       # yielding the equivalent of rb.search(**kwargs)
    #     fb.filter       # remembering the **kwargs used to filter
    #     fb.tags         # yielding a similar
    #                     # list({"name": "..", "stationcount": ".."})
    #                     # as rb.tags()
    #                     # but narrowed to the tags still in this resultset
    #     fb.coutries     # -- and idem for languages, codecs, ...
