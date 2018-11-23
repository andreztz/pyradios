from pyradios.constants import BASE_URL
from pyradios.constants import endpoints


class EndPoints:
    def __init__(self, fmt="json"):
        self.fmt = fmt

    def get_endpoint(self, endpoint, option):
        ep = endpoint[option]
        return ep

    def get_endpoints(self, endpoint):
        ep = endpoints[endpoint]
        return ep

    def build_url(self, **kwargs):
        endpoint = self.get_endpoints(kwargs.get("endpoint"))
        mask = self.get_endpoint(endpoint, len(kwargs))
        kwargs.update({"fmt": self.fmt})
        endpoint = mask.format(**kwargs)

        return BASE_URL + endpoint

    def countries(self, filter_=""):
        kwargs = {}
        kwargs.update({"endpoint": "countries"})

        if filter_:
            kwargs.update({"filter": filter_})

        url = self.build_url(**kwargs)
        return url

    def codecs(self, filter_=""):
        kwargs = {}
        kwargs.update({"endpoint": "codecs"})
        if filter_:
            kwargs.update({"filter": filter_})
        url = self.build_url(**kwargs)
        return url

    def states(self, country="", filter_=""):
        kwargs = {}
        kwargs.update({"endpoint": "states"})
        if filter_:
            kwargs.update({"filter": filter_})
        if country:
            kwargs.update({"country": country})
        url = self.build_url(**kwargs)
        return url

    def languages(self, filter_=""):
        kwargs = {}
        kwargs.update({"endpoint": "languages"})

        if filter_:
            kwargs.update({"filter": filter_})

        url = self.build_url(**kwargs)
        return url

    def tags(self, filter_=""):
        kwargs = {}
        kwargs.update({"endpoint": "tags"})

        if filter_:
            kwargs.update({"filter": filter_})

        url = self.build_url(**kwargs)
        return url

    def stations(self):
        kwargs = {}
        kwargs.update({"endpoint": "stations"})
        url = self.build_url(**kwargs)
        return url

    def stations_byid(self, term):
        kwargs = {}
        kwargs.update(
            {"endpoint": "stations", "by": "byid", "search_term": term}
        )

        url = self.build_url(**kwargs)
        return url

    def stations_byuuid(self, term):
        kwargs = {}
        kwargs.update(
            {"endpoint": "stations", "by": "byuuid", "search_term": term}
        )

        url = self.build_url(**kwargs)
        return url

    def stations_byname(self, term):
        kwargs = {}
        kwargs.update(
            {"endpoint": "stations", "by": "byname", "search_term": term}
        )

        url = self.build_url(**kwargs)
        return url

    def stations_bynameexact(self, term):
        kwargs = {}
        kwargs.update(
            {"endpoint": "stations", "by": "bynameexact", "search_term": term}
        )

        url = self.build_url(**kwargs)
        return url

    def stations_bycodec(self, term):
        kwargs = {}
        kwargs.update(
            {"endpoint": "stations", "by": "bycodec", "search_term": term}
        )

        url = self.build_url(**kwargs)
        return url

    def stations_bycodecexact(self, term):
        kwargs = {}
        kwargs.update(
            {"endpoint": "stations", "by": "bycodecexact", "search_term": term}
        )

        url = self.build_url(**kwargs)
        return url

    def stations_bycountry(self, term):
        kwargs = {}
        kwargs.update(
            {"endpoint": "stations", "by": "bycountry", "search_term": term}
        )

        url = self.build_url(**kwargs)
        return url

    def stations_bycountryexact(self, term):
        kwargs = {}
        kwargs.update(
            {
                "endpoint": "stations",
                "by": "bycountryexact",
                "search_term": term,
            }
        )

        url = self.build_url(**kwargs)
        return url

    def stations_bystate(self, term):
        kwargs = {}
        kwargs.update(
            {"endpoint": "stations", "by": "bystate", "search_term": term}
        )

        url = self.build_url(**kwargs)
        return url

    def stations_bystateexact(self, term):
        kwargs = {}
        kwargs.update(
            {"endpoint": "stations", "by": "bystateexact", "search_term": term}
        )

        url = self.build_url(**kwargs)
        return url

    def stations_bylanguage(self, term):
        kwargs = {}
        kwargs.update(
            {"endpoint": "stations", "by": "bylanguage", "search_term": term}
        )

        url = self.build_url(**kwargs)
        return url

    def stations_bylanguageexact(self, term):
        kwargs = {}
        kwargs.update(
            {
                "endpoint": "stations",
                "by": "bylanguageexact",
                "search_term": term,
            }
        )

        url = self.build_url(**kwargs)
        return url

    def stations_bytag(self, term):
        kwargs = {}
        kwargs.update(
            {"endpoint": "stations", "by": "bytag", "search_term": term}
        )

        url = self.build_url(**kwargs)
        return url

    def stations_bytagexact(self, term):
        kwargs = {}
        kwargs.update(
            {"endpoint": "stations", "by": "bytagexact", "search_term": term}
        )

        url = self.build_url(**kwargs)
        return url

    def playable_station(self, stationid):
        kwargs = {}
        kwargs.update(
            {
                "endpoint": "playable_station",
                "station_id": stationid,
                "ver": "v2",
            }
        )

        url = self.build_url(**kwargs)
        return url

    def station_search(self):
        kwargs = {"endpoint": "station_search"}
        url = self.build_url(**kwargs)
        return url

