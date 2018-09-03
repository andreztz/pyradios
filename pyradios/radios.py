import re
import requests

from xml.etree import ElementTree


_base = "http://www.radio-browser.info/webservice/"
_headers = {"content-type": "application/json", "User-Agent": "pyradios/dev"}


def request(url, **kwargs):
    _params = {}
    # https://stackoverflow.com/questions/18308529/python-requests-package-handling-xml-response
    formats = kwargs.get("formats")
    resp = requests.get(url, headers=_headers, params=_params)
    if resp.status_code == 200:
        if formats == "xml":  # TODO
            tree = ElementTree.fromstring(resp.content)
            return tree.text
        return resp.json()

    return resp.raise_for_status()


def build_url(endpoint=None, **kwargs):
    formats = kwargs.get("formats", "json")
    url = _base + formats + endpoint
    return url


class RadioBrowser:
    def codecs(self, filters=None, **kwargs):
        filters = kwargs.get("filters", filters)
        endpoint = f"/codecs/{filters}" if filters else "/codecs"
        url = build_url(endpoint, **kwargs)
        return request(url, **kwargs)

    def countries(self, filters=None, **kwrags):
        filters = kwargs.get("filters", filters)
        endpoint = f"/countries/{filters}" if filters else "/countries"
        url = build_url(endpoint)
        return request(url)

    def languages(self, filters=None, **kwargs):
        filters = kwargs.get("filters", filters)
        endpoint = f"/languages/{filters}" if filters else "/languages"
        url = build_url(endpoint)
        return request(url)

    def stations(self, searchterm=None, **kwargs):
        # TODO implementar advanced search params = {}
        endpoint = f"/stations"
        url = build_url(endpoint)
        return request(url, **kwargs)

    def stations_byid(self, id, **kwargs):
        id = kwargs.get("id", id)
        endpoint = f"/stations/byid/{id}"
        url = build_url(endpoint)
        return request(url)

    def stations_byuuid(self, uuid, **kwargs):
        name = kwargs.get("uuid", uuid)
        endpoint = f"/stations/byuuid/{uuid}"
        url = build_url(endpoint)
        return request(url)

    def stations_byname(self, name, **kwargs):
        name = kwargs.get("name", name)
        endpoint = f"/stations/byname/{name}"
        url = build_url(endpoint)
        return request(url)

    def stations_bynameexact(self, name, **kwargs):
        name = kwargs.get("name", name)
        endpoint = f"/stations/bynameexact/{name}"
        url = build_url(endpoint)
        return request(url)

    def stations_bycodec(self, name, **kwargs):
        name = kwargs.get("name", name)
        endpoint = f"/stations/bycodec/{name}"
        url = build_url(endpoint)
        return request(url)

    def stations_bycodecexact(self, name, **kwargs):
        name = kwargs.get("name", name)
        endpoint = f"/stations/bycodecexact/{name}"
        url = build_url(endpoint)
        return request(url)

    def stations_bycountry(self, name, **kwargs):
        name = kwargs.get("name", name)
        endpoint = f"/stations/bycountry/{name}"
        url = build_url(endpoint)
        return request(url)

    def stations_bycountryexact(self, name, **kwargs):
        name = kwargs.get("name", name)
        endpoint = f"/stations/bycountryexact/{name}"
        url = build_url(endpoint)
        return request(url)

    def stations_bystateexact(self, name, **kwargs):
        name = kwargs.get("name", name)
        endpoint = f"/stations/bystateexact/{name}"
        url = build_url(endpoint)
        return request(url)

    def stations_bylanguage(self, name, **kwargs):
        name = kwargs.get("name", name)
        endpoint = f"/stations/bylanguage/{name}"
        url = build_url(endpoint)
        return request(url)

    def stations_bylanguageexact(self, name, **kwargs):
        name = kwargs.get("name", name)
        endpoint = f"/stations/bylanguageexact/{name}"
        url = build_url(endpoint)
        return request(url)

    def stations_bytag(self, name, **kwargs):
        name = kwargs.get("name", name)
        endpoint = f"/stations/bytag/{name}"
        url = build_url(endpoint)
        print(url)
        return request(url)

    def stations_bytagexact(self, name, **kwargs):
        name = kwargs.get("name", name)
        endpoint = f"/stations/bytagexact/{name}"
        url = build_url(endpoint)
        return request(url)

    def tags(self, filters=None, **kwargs):
        filters = kwargs.get("filters", filters)
        endpoint = f"/tags/{filters}" if filters else "/tags"
        url = build_url(endpoint)
        return request(url)

    def playable_station(self, stationid, formats="json", **kwargs):
        stationid = kwargs.get("stationid")
        formats = kwargs.get("formats", formats)
        endpoint = f"/{formats}/url/{stationid}"
        url = build_url(endpoint)
        return request(url)


def main():
    from pprint import pprint

    rb = RadioBrowser()
    rb.stations_bytag("trance")
    pprint(rb.stations_bytag(name="trance"))


if __name__ == "__main__":
    main()
