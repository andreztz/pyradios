import requests

from xml.etree import ElementTree
from urllib.parse import urljoin

from collections import OrderedDict


base_url = "http://www.radio-browser.info/webservice/"


def request(url, **kwargs):

    fmt = kwargs.get("format", "json")

    if fmt == "xml":
        content_type = f"application/{fmt}"
    else:
        content_type = f"application/{fmt}"

    _headers = {"content-type": content_type, "User-Agent": "pyradios/dev"}
    _params = {}

    resp = requests.get(url, headers=_headers, params=_params)
    if resp.status_code == 200:
        if fmt == "xml":
            return resp.text
        return resp.json()

    return resp.raise_for_status()


def build_mask(ordered):
    mask = "".join("{" + key + "}/" for key in ordered if ordered[key])
    return mask


def build_endpoint(**kwargs):
    ordered = OrderedDict()
    ordered["ver"] = kwargs.get("ver", None)
    ordered["format"] = kwargs.get("format", "json")
    ordered["endpoint"] = kwargs.get("endpoint")
    ordered["country"] = kwargs.get("country", None)
    ordered["filter"] = kwargs.get("filter", None)
    ordered["by"] = kwargs.get("by", None)

    mask = build_mask(ordered)
    endpoint = mask.format(**ordered)

    if not ordered["filter"] and not ordered["country"]:
        endpoint = endpoint[:-1]

    if ordered["filter"]:
        endpoint = endpoint[:-1]

    url = urljoin(base_url, endpoint)
    return url


class RadioBrowser:
    def countries(self, **kwargs):
        url = build_endpoint(endpoint="countries", **kwargs)
        return request(url, **kwargs)

    def codecs(self, **kwargs):
        url = build_endpoint(endpoint="codecs", **kwargs)
        return request(url, **kwargs)

    def states(self, **kwargs):
        url = build_endpoint(endpoint="states", **kwargs)
        return request(url, **kwargs)

    def languages(self, **kwargs):
        url = build_endpoint(endpoint="tags", **kwargs)
        return request(url, **kwargs)

    def stations(self, **kwargs):
        url = build_endpoint(endpoint="stations", **kwargs)
        return request(url, **kwargs)

    def stations_byid(self, **kwargs):
        url = build_endpoint(endpoint="stations/byid", **kwargs)
        return request(url, **kwargs)

    def stations_byid(self, **kwargs):
        url = build_endpoint(endpoint="stations/byid", **kwargs)
        return request(url, **kwargs)

    def stations_byuuid(self, **kwargs):
        url = build_endpoint(endpoint="stations/byuuid", **kwargs)
        return request(url, **kwargs)

    def stations_byname(self, **kwargs):
        url = build_endpoint(endpoint="stations/byname", **kwargs)
        return request(url, **kwargs)

    def stations_bynameexact(self, **kwargs):
        url = build_endpoint(endpoint="stations/bynameexact", **kwargs)
        return request(url, **kwargs)

    def stations_bycodec(self, **kwargs):
        url = build_endpoint(endpoint="stations/bycodec", **kwargs)
        return request(url, **kwargs)

    def stations_bycodecexact(self, **kwargs):
        url = build_endpoint(endpoint="stations/bycodecexact", **kwargs)
        return request(url, **kwargs)

    def stations_bycountry(self, **kwargs):
        url = build_endpoint(endpoint="stations/bycountry", **kwargs)
        return request(url, **kwargs)

    def stations_bycountryexact(self, **kwargs):
        url = build_endpoint(endpoint="stations/bycountryexact", **kwargs)
        return request(url, **kwargs)

    def stations_bystate(self, **kwargs):
        url = build_endpoint(endpoint="stations/bystate", **kwargs)
        return request(url, **kwargs)

    def stations_bystateexact(self, **kwargs):
        url = build_endpoint(endpoint="stations/bystateexact", **kwargs)
        return request(url, **kwargs)

    def stations_bylanguage(self, **kwargs):
        url = build_endpoint(endpoint="stations/bylanguage", **kwargs)
        return request(url, **kwargs)

    def stations_bylanguageexact(self, **kwargs):
        url = build_endpoint(endpoint="stations/bylanguageexact", **kwargs)
        return request(url, **kwargs)

    def stations_bytag(self, **kwargs):
        url = build_endpoint(endpoint="stations/bytag", **kwargs)
        return request(url, **kwargs)

    def stations_bytagexact(self, **kwargs):
        url = build_endpoint(endpoint="stations/bytagexact", **kwargs)
        return request(url, **kwargs)

    ########
    def playable_stations(self, **kwargs):
        url = build_endpoint(endpoint="url", ver="v2", **kwargs)
        return request(url, **kwargs)


def main():
    rb = RadioBrowser()
    print(rb.codecs(format="xml"))
    print(rb.playable_stations("87019", format="json"))
    print(rb.stations(byid="1"))
    print(rb.stations_byid("87019", test="test"))


if __name__ == "__main__":
    main()
