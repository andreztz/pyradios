import requests

from pyradios.base_url import pick_base_url
from pyradios.utils import type_check


class Request:
    def __init__(self, fmt, session=None, **kwargs):
        self._session = self._init_session(session)

        self._fmt = fmt

        if "base_url" in kwargs:  # for tests with the responses lib
            self.base_url = kwargs.get("base_url")
        else:
            self.base_url = pick_base_url()

    def _init_session(self, session):
        if session is None:
            return requests.Session()
        return session

    def get(self, endpoint, **kwargs):

        if "fmt" in kwargs:
            self._fmt = kwargs.get("fmt")
            endpoint = self._fmt + "/" + endpoint.split("/", 1)[1]
            del kwargs["fmt"]

        if self._fmt == "xml":
            content_type = "application/{}".format(self._fmt)
        else:
            content_type = "application/{}".format(self._fmt)

        headers = {"content-type": content_type, "User-Agent": "pyradios/dev"}

        url = self.base_url + endpoint

        resp = self._session.get(url, headers=headers, params=kwargs)

        if resp.status_code == 200:
            if self._fmt == "xml":
                # return resp.text
                return resp.content
            return resp.json()

        return resp.raise_for_status()


class RadioBrowser:
    """This class implements the main interface for the Radio Browser API.

    Args:
        session (obj, optional): The `requests_cache.CachedSession` instance.

    Examples:
        To create an instance of the RadioBrowser class with cached session

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

        No cahce

        >>> import pyradios
        >>> rb = pyradios.RadioBrowser()
        >>> rb.countries()

    Note:
        Run `pip install requests_cache` to use cached session.

    """

    def __init__(self, fmt="json", session=None, **kwargs):

        self._fmt = fmt
        self.client = Request(self._fmt, session, **kwargs)

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
            endpoint = "{fmt}/countrycodes/{code}".format(
                fmt=self._fmt, code=code
            )
        else:
            endpoint = "{fmt}/countrycodes/".format(fmt=self._fmt)
        return self.client.get(endpoint)

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
            endpoint = "{fmt}/countrycodes/{code}".format(
                fmt=self._fmt, code=code
            )
        else:
            endpoint = "{fmt}/countrycodes/".format(fmt=self._fmt)
        return self.client.get(endpoint)

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

        endpoint = "{fmt}/codecs/".format(fmt=self._fmt)

        if codec:
            response = self.client.get(endpoint)
            return list(
                filter(
                    lambda _codecs: _codecs["name"].lower() == codec.lower(),
                    response,
                )
            )

        return self.client.get(endpoint)

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

        endpoint = "{fmt}/states".format(fmt=self._fmt)

        if country and state:

            response = self.client.get(endpoint)
            return list(
                filter(
                    lambda _state: _state["country"].lower() == country.lower()
                    and _state["name"].lower() == state.lower(),
                    response,
                )
            )

        if country:
            response = self.client.get(endpoint)
            return list(
                filter(
                    lambda _state: _state["country"].lower()
                    == country.lower(),
                    response,
                )
            )
        if state:
            response = self.client.get(endpoint)
            return list(
                filter(
                    lambda _state: _state["name"].lower() == state.lower(),
                    response,
                )
            )
        return self.client.get(endpoint)

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
            endpoint = "{fmt}/languages/{language}".format(
                fmt=self._fmt, language=language
            )
        else:
            endpoint = "{fmt}/languages/".format(fmt=self._fmt)

        return self.client.get(endpoint)

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
            endpoint = "{fmt}/tags/{tag}".format(fmt=self._fmt, tag=tag)
        else:
            endpoint = "{fmt}/tags/".format(fmt=self._fmt)

        return self.client.get(endpoint)

    def station_by_uuid(self, stationuuid):
        """Radio station by stationuuid.

        Args:
            stationuuid (str): A globally unique identifier for the station.

        Returns:
            list: Stations.

        See details:
            https://de1.api.radio-browser.info/#List_of_radio_stations
        """
        endpoint = "{fmt}/stations/byuuid/{uuid}".format(
            fmt=self._fmt, uuid=stationuuid
        )
        return self.client.get(endpoint)

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
        kwargs.update({"code": codec, "codec_exact": exact})
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

    def click_counter(self, stationuuid):
        """Increase the click count of a station by one.

        This should be called everytime when a user starts
        playing a stream to mark the stream more popular than others.
        Every call to this endpoint from the same IP address and for
        the same station only gets counted once per day. The call will
        return detailed information about the stream, supported output
        formats: JSON

        Args:
            stationuuid (str): A globally unique identifier for the station.

        Returns:
            dict: A dict containing informations about the radio station.

        See details:
            https://de1.api.radio-browser.info/#Count_station_click
        """
        endpoint = "{fmt}/url/{uuid}".format(fmt=self._fmt, uuid=stationuuid)

        return self.client.get(endpoint)

    def stations(self, **kwargs):
        """Lists all radio stations.

        Returns:
            list: Stations.

        See details:
            https://nl1.api.radio-browser.info/#List_of_all_radio_stations
        """
        endpoint = "{fmt}/stations".format(fmt=self._fmt)
        return self.client.get(endpoint, **kwargs)

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
        endpoint = "{fmt}/stations/search".format(fmt=self._fmt)
        return self.client.get(endpoint, **kwargs)

