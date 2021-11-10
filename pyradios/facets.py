from pyradios.radios import RadioBrowser


class RadioFacets:
    FACETS = ["tags", "countrycodes", "languages", "states", "codecs"]

    def __init__(self, rb, **params):
        assert rb is not None, "facets requires a RadioBrowser service to call"
        assert isinstance(rb, RadioBrowser), "RadioBrowser service wrong type"
        self.rb = rb
        self.filter = params
        self._exec()

    def _exec(self):
        self.result = self.rb.search(**self.filter)
        # todo - calculate counts and histograms on everything

    def __len__(self):
        return len(self.result)

    def _derived(self, **filter):
        return RadioFacets(self.rb, **filter)

    def narrow(self, **extra_params):
        filter = dict(self.filter)
        filter.update(extra_params)
        return self._derived(**filter)

    def broaden(self, *keys_to_remove):
        filter = dict(self.filter)
        for k in keys_to_remove:
            filter.pop(k, None)
        return self._derived(**filter)

    # todo implement ideas expressed in https://github.com/andreztz/pyradios/issues/32
    #     fb = rb.facets(**query)
    #     fb.result       # yielding the equivalent of rb.search(**kwargs)
    #     fb.filter       # remembering the **kwargs used to filter
    #     fb.tags         # yielding a similar list({"name": "..", "stationcount": ".."}) as rb.tags() but narrowed to the tags still in this resultset
    #     fb.coutries     #  similarly so, as well as for languages, codecs, tags, ...
    #     fb2 = fb.add(tag="extra filter tag", countrycode="be")    # an more constrained similar facets object
    #     fb3 = fb.remove("tag", "language")                        # a less constrained one, removing he passed filter-items
