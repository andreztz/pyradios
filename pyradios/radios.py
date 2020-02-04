"""
http://www.radio-browser.info/webservice
"""

from urllib.parse import urljoin
from xml.etree import ElementTree

import requests

from pyradios.base_url import pick_url
from pyradios.constants import endpoints


def request(endpoint, **kwargs):

    BASE_URL = pick_url(
        filename="data.cache", expire=kwargs.get("expire", 604800), **kwargs
    )

    fmt = kwargs.get("format", "json")

    if fmt == "xml":
        content_type = f"application/{fmt}"
    else:
        content_type = f"application/{fmt}"

    headers = {"content-type": content_type, "User-Agent": "pyradios/dev"}

    params = kwargs.get("params", {})

    url = BASE_URL + endpoint

    resp = requests.get(url, headers=headers, params=params)

    if resp.status_code == 200:
        if fmt == "xml":
            return resp.text
        return resp.json()

    return resp.raise_for_status()


class EndPointBuilder:
    def __init__(self, **kwargs):
        self.fmt = kwargs.get("fmt")
        self._option = None
        self._endpoint = None

    @property
    def endpoint(self):
        return endpoints[self._endpoint][self._option]

    def produce_endpoint(self, **parts):
        self._option = len(parts)
        self._endpoint = parts["endpoint"]
        parts.update({"fmt": self.fmt})
        return self.endpoint.format(**parts)


class RadioBrowser:
    """
    Supported output formats: JSON

    TODO:
        * XML support.
    """

    config = {}

    def __init__(self, fmt="json", **kwargs):
        self._fmt = fmt
        self.config.update(kwargs, fmt=fmt)
        self.builder = EndPointBuilder(**self.config)

    def countrycodes(self, filter_by_code=None):
        if filter_by_code:
            endpoint = self.builder.produce_endpoint(
                endpoint="countrycodes", filter=filter_by_code
            )
        else:
            endpoint = self.builder.produce_endpoint(endpoint="countrycodes")
        return request(endpoint, **self.config)

    def codecs(self, filter_by_codec=None):
        codec = filter_by_codec
        endpoint = self.builder.produce_endpoint(endpoint="codecs")

        if codec:
            response = request(endpoint, **self.config)
            return list(
                filter(
                    lambda codecs: codecs["name"].lower() == codec.lower(),
                    response,
                )
            )

        return request(endpoint, **self.config)

    def states(self, filter_by_country=None, filter_by_state=None):

        country = filter_by_country
        name = filter_by_state

        # endpoint = "{}/states".format(self._fmt)
        endpoint = self.builder.produce_endpoint(endpoint="states")

        if filter_by_country and filter_by_state:
            response = request(endpoint, **self.config)
            return list(
                filter(
                    lambda state: state["country"].lower() == country.lower()
                    and state["name"].lower() == name.lower(),
                    response,
                )
            )

        if filter_by_country:
            response = request(endpoint, **self.config)
            return list(
                filter(
                    lambda state: state["country"].lower() == country.lower(),
                    response,
                )
            )
        if filter_by_state:
            response = request(endpoint, **self.config)
            return list(
                filter(
                    lambda state: state["name"].lower() == name.lower(),
                    response,
                )
            )
        return request(endpoint, **self.config)

    def languages(self, filter_by_language=None):
        endpoint = self.builder.produce_endpoint(
            endpoint="languages", filter=filter_by_language
        )
        return request(endpoint, **self.config)

    def tags(self, filter_by_tag=None):
        endpoint = self.builder.produce_endpoint(endpoint="tags")
        name = filter_by_tag
        if name:
            response = request(endpoint, **self.config)
            return list(
                filter(
                    lambda tag: tag["name"].lower() == name.lower(), response
                )
            )
        return request(endpoint, **self.config)

    def stations_byuuid(self, uuid):
        endpoint = self.builder.produce_endpoint(
            endpoint="stations", by="byuuid", search_term=uuid
        )
        return request(endpoint, **self.config)

    def stations_byname(self, name):
        endpoint = self.builder.produce_endpoint(
            endpoint="stations", by="byname", search_term=name
        )
        return request(endpoint, **self.config)

    def stations_bynameexact(self, nameexact):
        endpoint = self.builder.produce_endpoint(
            endpoint="stations", by="bynameexact", search_term=nameexact
        )
        return request(endpoint, **self.config)

    def stations_bycodec(self, codec):
        endpoint = self.builder.produce_endpoint(
            endpoint="stations", by="bycodec", search_term=codec
        )
        return request(endpoint, **self.config)

    def stations_bycodecexact(self, codecexact):
        endpoint = self.builder.produce_endpoint(
            endpoint="stations", by="bycodecexact", search_term=codecexact
        )
        return request(endpoint, **self.config)

    def stations_bycountry(self, country):
        endpoint = self.builder.produce_endpoint(
            endpoint="stations", by="bycountry", search_term=country
        )
        return request(endpoint, **self.config)

    def stations_bycountryexact(self, countryexact):
        endpoint = self.builder.produce_endpoint(
            endpoint="stations", by="bycountryexact", search_term=countryexact
        )
        return request(endpoint, **self.config)

    def stations_bystate(self, state):
        endpoint = self.builder.produce_endpoint(
            endpoint="stations", by="bystate", search_term=state
        )
        return request(endpoint, **self.config)

    def stations_bystateexact(self, stateexact):
        endpoint = self.builder.produce_endpoint(
            endpoint="stations", by="bystateexact", search_term=stateexact
        )
        return request(endpoint, **self.config)

    def stations_bylanguage(self, language):
        endpoint = self.builder.produce_endpoint(
            endpoint="stations", by="bylanguage", search_term=language
        )
        return request(endpoint, **self.config)

    def stations_bylanguageexact(self, languageexact):
        endpoint = self.builder.produce_endpoint(
            endpoint="stations",
            by="bylanguageexact",
            search_term=languageexact,
        )
        return request(endpoint, **self.config)

    def stations_bytag(self, tag):
        # endpoint = self.builder.produce_endpoint(
        #     endpoint="stations", by="bytag", search_term=tag
        # )
        # return request(endpoint, **self.config)
        return self.station_search(tag=tag)

    def stations_bytagexact(self, tagexact):
        # endpoint = self.builder.produce_endpoint(
        #     endpoint="stations", by="bytagexact", search_term=tagexact
        # )
        # return request(endpoint, **self.config)
        return self.station_search(tagExact=tagexact)

    def playable_station(self, station_id):
        endpoint = self.builder.produce_endpoint(
            endpoint="playable_station", station_id=station_id, ver="v2"
        )

        return request(endpoint, **self.config)

    def stations(self, **params):
        endpoint = self.builder.produce_endpoint(endpoint="stations")
        if params:
            self.config.update({"params": params})
        return request(endpoint, **self.config)

    def station_search(self, params={}, **kwargs):
        #  http://www.radio-browser.info/webservice#Advanced_station_search
        assert isinstance(params, dict), "params must be a dictionary."
        endpoint = self.builder.produce_endpoint(endpoint="station_search")
        self.config.setdefault("params", params)
        if kwargs:
            self.config["params"].update(kwargs)
        return request(endpoint, **self.config)

