import requests

from pyradios.base_url import pick_base_url
from pyradios.utils import type_check

import pkg_resources


version = pkg_resources.get_distribution('pyradios').version


class Request:
    def __init__(self, headers=None, session=None):
        self._headers = headers
        self._session = self._init_session(session)

    def _init_session(self, session):
        if session is None:
            return requests.Session()
        return session

    def get(self, url, **kwargs):
        resp = self._session.get(url, headers=self._headers, params=kwargs)
        if resp.status_code == 200:
            return resp.json()
        return resp.raise_for_status()


class RadioBrowser:
    """This class implements the main interface for the Radio Browser API.

    Args:
        session (obj, optional): The `requests_cache.CachedSession` instance.

    Examples:

        >>> import pyradios
        >>> rb = pyradios.RadioBrowser()
        >>> rb.countries()

        To create an instance of the RadioBrowser class with cached session.

        >>> from pyradios import RadioBrowser
        >>> from requests_cache import CachedSession
        >>> import datetime
        >>> from datetime import timedelta
        >>> expire_after = timedelta(days=3)
        >>> session = CachedSession(
        ...     cache_name='cache',
        ...     backend='sqlite',
        ...     expire_after=expire_after)
        >>> rb = RadioBrowser(session=session)
        >>> rb.countries()

    Note:
        Run `pip install requests_cache` to use cached session.

    """

    headers = {"User-Agent": "pyradios/{}".format(version)}

    def __init__(self, session=None, **kwargs):
        self.base_url = pick_base_url()
        self._fmt = 'json'
        self.client = Request(headers=self.headers, session=session)

    def build_url(self, endpoint):
        url = self.base_url + endpoint
        return url

    @type_check
    def countries(self, code=None):
        """Lists all countries.

        Args:
            code (str, optional): Filter by country code. Defaults to None.

        Returns:
            list: Countries.

        See details:
            https://de1.api.radio-browser.info/#List_of_countries
        """

        if code:
            endpoint = "json/countries/{code}".format(
                code=code
            )
        else:
            endpoint = "json/countries/"
        url = self.build_url(endpoint)
        return self.client.get(url)

    @type_check
    def countrycodes(self, code=None):
        """Lists all countries.

        Args:
            code (str, optional): Filter by country code. Defaults to None.

        Returns:
            list: Countries.

        See details:
            https://de1.api.radio-browser.info/#List_of_countrycodes
        """

        if code:
            endpoint = "json/countrycodes/{code}".format(
                code=code
            )
        else:
            endpoint = "json/countrycodes/"
        url = self.build_url(endpoint)
        return self.client.get(url)

    @type_check
    def codecs(self, codec=None):
        """Lists all codecs.

        Args:
            codec (str, optional): Filter by codec. Defaults to None.

        Returns:
            list: Codecs.

        See details:
            https://de1.api.radio-browser.info/#List_of_codecs
        """

        endpoint = "json/codecs/"
        url = self.build_url(endpoint)

        if codec:
            response = self.client.get(url)
            return list(
                filter(
                    lambda _codecs: _codecs["name"].lower() == codec.lower(),
                    response,
                )
            )
        return self.client.get(url)

    @type_check
    def states(self, country=None, state=None):
        """Lists all states.

        Args:
            country (str, optional): Filter by country. Defaults to None.
            state (str, optionla): Filter by state.  Defaults to None.

        Returns:
            list: States.

        See details:
            https://de1.api.radio-browser.info/#List_of_states
        """

        endpoint = "json/states"

        url = self.build_url(endpoint)

        if country and state:

            response = self.client.get(url)
            return list(
                filter(
                    lambda _state: _state["country"].lower() == country.lower()
                    and _state["name"].lower() == state.lower(),
                    response,
                )
            )

        if country:
            response = self.client.get(url)
            return list(
                filter(
                    lambda _state: _state["country"].lower()
                    == country.lower(),
                    response,
                )
            )
        if state:
            response = self.client.get(url)
            return list(
                filter(
                    lambda _state: _state["name"].lower() == state.lower(),
                    response,
                )
            )
        return self.client.get(url)

    @type_check
    def languages(self, language=None):
        """Lists all languages.

        Args:
            language (str, optional): Filter by language. Defaults to None.

        Returns:
            list: Languages.

        See details:
            https://de1.api.radio-browser.info/#List_of_languages
        """
        if language:
            endpoint = "json/languages/{language}".format(
                language=language
            )
        else:
            endpoint = "json/languages/"
        url = self.build_url(endpoint)
        return self.client.get(url)

    @type_check
    def tags(self, tag=None):
        """Lists all tags.

        Args:
            tag (str, optional): Filter by tag. Defaults to None.

        Returns:
            list: Tags.

        See details:
            https://de1.api.radio-browser.info/#List_of_tags
        """

        if tag:
            tag = tag.lower()
            endpoint = "json/tags/{tag}".format(tag=tag)
        else:
            endpoint = "json/tags/"
        url = self.build_url(endpoint)
        return self.client.get(url)

    def station_by_uuid(self, stationuuid):
        """Radio station by stationuuid.

        Args:
            stationuuid (str): A globally unique identifier for the station.

        Returns:
            list: Stations.

        See details:
            https://de1.api.radio-browser.info/#List_of_radio_stations
        """
        endpoint = "json/stations/byuuid/{uuid}".format(
            uuid=stationuuid
        )
        url = self.build_url(endpoint)
        return self.client.get(url)

    def stations_by_name(self, name, exact=False, **kwargs):
        """Lists all radio stations by name.

        Args:
            name (str): The name of the station.
            reverse (bool): Reverse the result list if set to True.

        Returns:
            list: Stations.

        See details:
            https://de1.api.radio-browser.info/#List_of_radio_stations
        """
        kwargs.update({"name": name, "name_exact": exact})
        return self.search(**kwargs)

    def stations_by_codec(self, codec, exact=False, **kwargs):
        """Lists all radio stations by codec.

        Args:
            codec (str): The name of the codec.

        Returns:
            list: Stations.

        See details:
            https://de1.api.radio-browser.info/#List_of_radio_stations
        """
        kwargs.update({"codec": codec, "codec_exact": exact})
        return self.search(**kwargs)

    def stations_by_country(self, country, exact=False, **kwargs):
        """Lists all radio stations by country.

        Args:
            country (str): The name of the country.

        Returns:
            list: Stations.

        See details:
            https://de1.api.radio-browser.info/#List_of_radio_stations
        """
        kwargs.update({"country": country, "country_exact": exact})
        return self.search(**kwargs)

    def stations_by_countrycode(self, code, **kwargs):
        """Lists all radio stations by country code.

        Args:
            code (str): Official countrycodes as in ISO 3166-1 alpha-2.

        Returns:
            list: Stations.

        See details:
            https://de1.api.radio-browser.info/#List_of_radio_stations
        """
        kwargs.update({"countrycode": code})
        return self.search(**kwargs)

    def stations_by_state(self, state, exact=False, **kwargs):
        """Lists all radio stations by state.

        Args:
            state (str): The name of the state.

        Returns:
            list: Stations.

        See details:
            https://de1.api.radio-browser.info/#List_of_radio_stations
        """
        kwargs.update({"state": state, "state_exact": exact})
        return self.search(**kwargs)

    def stations_by_language(self, language, exact=False, **kwargs):
        """Lists all radio stations by language.

        Args:
            language (str): The name of the language.

        Returns:
            list: Stations.

        See details:
            https://de1.api.radio-browser.info/#List_of_radio_stations
        """
        kwargs.update({"language": language, "language_exact": exact})
        return self.search(**kwargs)

    def stations_by_tag(self, tag, exact=False, **kwargs):
        """Lists all radio stations by tag.

        Args:
            tag (str): The name of the tag.

        Returns:
            list: Stations.
        See details:
            https://de1.api.radio-browser.info/#List_of_radio_stations
        """
        kwargs.update({"tag": tag, "tag_exact": exact})
        return self.search(**kwargs)

    def stations_by_tag_list(self, tag_list, **kwargs):
        """Lists all radio stations by tag. Must match all tags exactly.

        Args:
            tag_list (list): A list of names of tags.

        Returns:
            list: Stations.
        See details:
            https://de1.api.radio-browser.info/#List_of_radio_stations
        """
        tag_list = ",".join(tag_list)
        kwargs.update({"tag_list": tag_list})
        return self.search(**kwargs)

    def click_counter(self, stationuuid):
        """Increase the click count of a station by one.

        This should be called everytime when a user starts
        playing a stream to mark the stream more popular than others.
        Every call to this endpoint from the same IP address and for
        the same station only gets counted once per day. The call will
        return detailed information about the stat stream, supported output
        formats: JSON

        Args:
            stationuuid (str): A globally unique identifier for the station.

        Returns:
            dict: A dict containing informations about the radio station.

        See details:
            https://de1.api.radio-browser.info/#Count_station_click
        """
        endpoint = "json/url/{uuid}".format(uuid=stationuuid)
        url = self.build_url(endpoint)
        return self.client.get(url)

    def stations(self, **kwargs):
        """Lists all radio stations.

        Returns:
            list: Stations.

        See details:
            https://nl1.api.radio-browser.info/#List_of_all_radio_stations
        """
        endpoint = "json/stations"
        url = self.build_url(endpoint)
        return self.client.get(url, **kwargs)

    def stations_by_votes(self, limit, **kwargs):
        """A list of the highest-voted stations.

        Args:
            limit: Number of wanted stations

        Returns:
            list: Stations.

        See details:
            https://nl1.api.radio-browser.info/#Stations_by_votes
        """
        endpoint = "json/stations/topvote/{limit}".format(limit=limit)
        url = self.build_url(endpoint)
        return self.client.get(url, **kwargs)

    @type_check
    def search(self, **kwargs):
        """Advanced search.

        It will search for the station whose attribute
        contains the search term.

        Args:
            name (str, optional): Name of the station.
            name_exact (bool, optional): Only exact matches, otherwise all
                matches (default: False).
            country (str, optional): Country of the station.
            country_exact (bool, optional): Only exact matches, otherwise
                all matches (default: False).
            countrycode (str, optional): 2-digit countrycode of the station
                (see ISO 3166-1 alpha-2)
            state (str, optional): State of the station.
            state_exact (bool, optional): Only exact matches, otherwise all
                matches. (default: False)
            language (str, optional): Language of the station.
            language_exact (bool, optional): Only exact matches, otherwise
                all matches. (default: False)
            tag (str, optional): Tag of the station.
            tag_exact (bool, optional): Only exact matches, otherwise all
                matches. (default: False)
            tag_list (str, optional): A comma-separated list of tag.
            bitrate_min (int, optional): Minimum of kbps for bitrate field of
                stations in result. (default: 0)
            bitrate_max (int, optional): Maximum of kbps for bitrate field of
                stations in result. (default: 1000000)
            order (str, optional): The result list will be sorted by: name,
                url, homepage, favicon, tags, country, state, language, votes,
                codec, bitrate, lastcheckok, lastchecktime, clicktimestamp,
                clickcount, clicktrend, random
            reverse (bool, optional): Reverse the result list if set to true.
                (default: false)
            offset (int, optional): Starting value of the result list from
                the database. For example, if you want to do paging on the
                server side. (default: 0)
            limit (int, optional): Number of returned datarows (stations)
                starting with offset (default 100000)
            hidebroken (bool, optional): do list/not list broken stations.
                Note: Not documented in the "Advanced Station Search".

        Returns:
            list: Stations.

        Example:
            >>> from pyradios import RadioBrowser
            >>> rb = RadioBrowser()
            >>> rb.search(name='BBC Radio 1', name_exact=True)

        See details:
            https://de1.api.radio-browser.info/#Advanced_station_search
        """
        endpoint = "json/stations/search"
        # lowercase tag reference since the API turned to be case-sensitive
        for paramkey in ['tag', 'tagList']:
            if paramkey in kwargs:
                kwargs[paramkey] = kwargs[paramkey].lower()
        url = self.build_url(endpoint)
        return self.client.get(url, **kwargs)
