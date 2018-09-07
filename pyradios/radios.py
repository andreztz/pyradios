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

    headers = {"content-type": content_type, "User-Agent": "pyradios/dev"}
    params = kwargs.get("params", {})

    resp = requests.get(url, headers=headers, params=params)
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
    def countries(self, name, **kwargs):
        url = build_endpoint(endpoint="countries", filter=name, **kwargs)
        return request(url, **kwargs)

    def codecs(self, name, **kwargs):
        url = build_endpoint(endpoint="codecs", filter=name, **kwargs)
        return request(url, **kwargs)

    def states(self, name, country=None, **kwargs):
        url = build_endpoint(
            endpoint="states", filter=name, coutry=country, **kwargs
        )
        return request(url, **kwargs)

    def languages(self, name, **kwargs):
        url = build_endpoint(endpoint="languages", filter=name, **kwargs)
        return request(url, **kwargs)

    def tags(self, name, **kwargs):
        url = build_endpoint(endpoint="tags", filter=name, **kwargs)
        return request(url, **kwargs)

    def stations(self, **kwargs):
        url = build_endpoint(endpoint="stations", **kwargs)
        return request(url, **kwargs)

    def stations_byid(self, stationid, **kwargs):
        url = build_endpoint(endpoint="stations/byid", by=stationid, **kwargs)
        return request(url, **kwargs)

    def stations_byuuid(self, uuid, **kwargs):
        url = build_endpoint(endpoint="stations/byuuid", by=uuid, **kwargs)
        return request(url, **kwargs)

    def stations_byname(self, name, **kwargs):
        url = build_endpoint(endpoint="stations/byname", by=name, **kwargs)
        return request(url, **kwargs)

    def stations_bynameexact(self, nameexact, **kwargs):
        url = build_endpoint(
            endpoint="stations/bynameexact", by=nameexact, **kwargs
        )
        return request(url, **kwargs)

    def stations_bycodec(self, codec, **kwargs):
        url = build_endpoint(endpoint="stations/bycodec", by=codec, **kwargs)
        return request(url, **kwargs)

    def stations_bycodecexact(self, codecexact, **kwargs):
        url = build_endpoint(
            endpoint="stations/bycodecexact", by=codecexact, **kwargs
        )
        return request(url, **kwargs)

    def stations_bycountry(self, country, **kwargs):
        url = build_endpoint(
            endpoint="stations/bycountry", by=country, **kwargs
        )
        return request(url, **kwargs)

    def stations_bycountryexact(self, countryexact, **kwargs):
        url = build_endpoint(
            endpoint="stations/bycountryexact", by=countryexact, **kwargs
        )
        return request(url, **kwargs)

    def stations_bystate(self, state, **kwargs):
        url = build_endpoint(endpoint="stations/bystate", by=state, **kwargs)
        return request(url, **kwargs)

    def stations_bystateexact(self, stateexact, **kwargs):
        url = build_endpoint(
            endpoint="stations/bystateexact", by=stateexact, **kwargs
        )
        return request(url, **kwargs)

    def stations_bylanguage(self, language, **kwargs):
        url = build_endpoint(
            endpoint="stations/bylanguage", by=language, **kwargs
        )
        return request(url, **kwargs)

    def stations_bylanguageexact(self, languageexact, **kwargs):
        url = build_endpoint(
            endpoint="stations/bylanguageexact", by=languageexact, **kwargs
        )
        return request(url, **kwargs)

    def stations_bytag(self, tag, **kwargs):
        url = build_endpoint(endpoint="stations/bytag", by=tag, **kwargs)
        return request(url, **kwargs)

    def stations_bytagexact(self, tagexact, **kwargs):
        url = build_endpoint(
            endpoint="stations/bytagexact", by=tagexact, **kwargs
        )
        return request(url, **kwargs)

    def playable_station(self, stationid, **kwargs):
        url = build_endpoint(endpoint="url", by=stationid, ver="v2", **kwargs)
        return request(url, **kwargs)

    def station_search(self, params, **kwargs):
        assert isinstance(params, dict), "params is not a dict"
        kwargs["params"] = params
        url = build_endpoint(endpoint="stations", by="search", **kwargs)
        return request(url, **kwargs)


def main():
    rb = RadioBrowser()
    print(rb.codecs(format="xml"))
    print(rb.playable_stations(stationid="87019", format="json"))
    # print(rb.stations())
    print(rb.stations_byid(stationid="87019"))
    print(rb.stations_byid("87019"))
    print(rb.stations_byname("TrancePulse FM"))


if __name__ == "__main__":
    main()
