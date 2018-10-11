import requests

from xml.etree import ElementTree
from urllib.parse import urljoin

from pyradios.api import EndPoints


base_url = "http://www.radio-browser.info/webservice/"


def request(url, **kwargs):

    fmt = kwargs.get("format", "json")

    if fmt == "xml":
        content_type = f"application/{fmt}"
    else:
        content_type = f"application/{fmt}"

    headers = {"content-type": content_type, "User-Agent": "pyradios/dev"}
    params = kwargs.get("params", {})

    resp = requests.get(url, headers=headers, params=params)
    if resp.status_code == 200:
        if fmt == "xml":
            return resp.text
        return resp.json()

    return resp.raise_for_status()


class RadioBrowser:
    def __init__(self, fmt="json"):
        self.fmt = fmt
        self.endpoints = EndPoints(fmt=self.fmt)

    def countries(self, filter_=""):
        url = self.endpoints.countries(filter_)
        return request(url)

    def codecs(self, filter_=""):
        url = self.endpoints.codecs(filter_)
        return request(url)

    def states(self, country="", filter_=""):
        url = self.endpoints.states(country, filter_)
        return request(url)

    def languages(self, filter_=""):
        url = self.endpoints.languages(filter_)
        return request(url)

    def tags(self, filter_=""):
        url = self.endpoints.tags(filter_)
        return request(url)

    def stations(self, **params):
        url = self.endpoints.stations()
        kwargs = {}
        if params:
            kwargs.update({"params": params})
        return request(url, **kwargs)

    def stations_byid(self, id):
        url = self.endpoints.stations_byid(term=id)
        return request(url)

    def stations_byuuid(self, uuid):
        url = self.endpoints.stations_byuuid(term=uuid)
        return request(url)

    def stations_byname(self, name):
        url = self.endpoints.stations_byname(term=name)
        return request(url)

    def stations_bynameexact(self, nameexact):
        url = self.endpoints.stations_bycodecexact(term=nameexact)
        return request(url)

    def stations_bycodec(self, codec):
        url = self.endpoints.stations_bycodec(term=codec)
        return request(url)

    def stations_bycodecexact(self, codecexact):
        url = self.endpoints.stations_bycodecexact(term=codecexact)
        return request(url)

    def stations_bycountry(self, country):
        url = self.endpoints.stations_bycountry(term=country)
        return request(url)

    def stations_bycountryexact(self, countryexact):
        url = self.endpoints.stations_bycountryexact(term=countryexact)
        return request(url)

    def stations_bystate(self, state):
        url = self.endpoints.stations_bystate(term=state)
        return request(url)

    def stations_bystateexact(self, stateexact):
        url = self.endpoints.stations_bystateexact(term=stateexact)
        return request(url)

    def stations_bylanguage(self, language):
        url = self.endpoints.stations_bylanguage(term=language)
        return request(url)

    def stations_bylanguageexact(self, languageexact):
        url = self.endpoints.stations_bylanguageexact(term=languageexact)
        return request(url)

    def stations_bytag(self, tag):
        url = self.endpoints.stations_bytag(term=tag)
        return request(url)

    def stations_bytagexact(self, tagexact):
        url = self.endpoints.stations_bytagexact(term=tagexact)
        return request(url)

    def playable_station(self, stationid):
        url = self.endpoints.playable_station(stationid=stationid)
        return request(url)

    # TODO
    def station_search(self, params, **kwargs):
        assert isinstance(params, dict), "params is not a dict"
        kwargs["params"] = params
        url = ""
        return request(url, **kwargs)
