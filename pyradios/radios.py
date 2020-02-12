import requests
from pyradios.base_url import pick_base_url
from pyradios.utils import bool2string


class Error(Exception):
    """Base class for all excpetions raised by this module."""


class IllegalArgumentError(Error):
    pass


class Request:
    def __init__(self, fmt, **kwargs):

        self._fmt = fmt

        if "base_url" in kwargs:  # for tests with lib responses
            self.base_url = kwargs.get("base_url")
        else:
            self.base_url = pick_base_url()

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

        resp = requests.get(url, headers=headers, params=kwargs)

        if resp.status_code == 200:
            if self._fmt == "xml":
                # return resp.text
                return resp.content
            return resp.json()

        return resp.raise_for_status()


class RadioBrowser:
    def __init__(self, fmt="json", **kwargs):

        self._fmt = fmt
        self.client = Request(self._fmt, **kwargs)

    def countries(self, code=None):
        """Lists all countries.

        See details at:
        https://de1.api.radio-browser.info/#List_of_countries

        Args:
            code (str, optional): Filter by country code. Defaults to None.

        Returns:
            list: Countries.
        """

        if code:
            endpoint = "{fmt}/countrycodes/{code}".format(
                fmt=self._fmt, code=code
            )
        else:
            endpoint = "{fmt}/countrycodes/".format(fmt=self._fmt)
        return self.client.get(endpoint)

    def countrycodes(self, code=None):
        """Lists all countries.

        See details at:
        https://de1.api.radio-browser.info/#List_of_countrycodes

        Args:
            code (str, optional): Filter by country code. Defaults to None.

        Returns:
            list: Countries.
        """

        if code:
            endpoint = "{fmt}/countrycodes/{code}".format(
                fmt=self._fmt, code=code
            )
        else:
            endpoint = "{fmt}/countrycodes/".format(fmt=self._fmt)
        return self.client.get(endpoint)

    def codecs(self, codec=None):
        """Lists all codecs.

        See details at:
        https://de1.api.radio-browser.info/#List_of_codecs

        Args:
            codec (str, optional): Filter by codec. Defaults to None.

        Returns:
            list: Codecs.
        """

        endpoint = "{fmt}/codecs/".format(fmt=self._fmt)

        # filter
        if codec:
            response = self.client.get(endpoint)
            return list(
                filter(
                    lambda _codecs: _codecs["name"].lower() == codec.lower(),
                    response,
                )
            )

        return self.client.get(endpoint)

    def states(self, country=None, state=None):
        """Lists all states.

        See details at:
        https://de1.api.radio-browser.info/#List_of_states

        Args:
            country (str, optional): Filter by country. Defaults to None.
            state (str, optionla): Filter by state.  Defaults to None.

        Returns:
            list: States.
        """

        endpoint = "{fmt}/states".format(fmt=self._fmt)

        # filters
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

    def languages(self, language=None):
        """Lists all languages.

        See details at:
        https://de1.api.radio-browser.info/#List_of_languages

        Args:
            language (str, optional): Filter by language. Defaults to None.

        Returns:
            list: Languages.
        """
        if language:
            endpoint = "{fmt}/languages/{language}".format(
                fmt=self._fmt, language=language
            )
        else:
            endpoint = "{fmt}/languages/".format(fmt=self._fmt)

        return self.client.get(endpoint)

    def tags(self, tag=None):
        """Lists all tags.

        See details at:
        https://de1.api.radio-browser.info/#List_of_tags

        Args:
            tag (str, optional): Filter by tag. Defaults to None.

        Returns:
            list: Tags.
        """

        if tag:
            endpoint = "{fmt}/tags/{tag}".format(fmt=self._fmt, tag=tag)
        else:
            endpoint = "{fmt}/tags/".format(fmt=self._fmt)

        return self.client.get(endpoint)

    def station_by_uuid(self, stationuuid):
        """Radio station by stationuuid.

        See details at:
        https://de1.api.radio-browser.info/#List_of_radio_stations


        Args:
            stationuuid (str): A globally unique identifier for the station.

        Returns:
            list: Stations.
        """
        endpoint = "{fmt}/stations/byuuid/{uuid}".format(
            fmt=self._fmt, uuid=stationuuid
        )

        return self.client.get(endpoint)

    def stations_by_name(self, name, exact=False):
        """Lists all radio stations by name.

        See details at:
        https://de1.api.radio-browser.info/#List_of_radio_stations


        Args:
            name (str): The name of the station.

        Returns:
            list: Stations.
        """
        if exact:
            endpoint = "{fmt}/stations/bynameexact/{name}".format(
                fmt=self._fmt, name=name
            )
        else:
            endpoint = "{fmt}/stations/byname/{name}".format(
                fmt=self._fmt, name=name
            )

        return self.client.get(endpoint)

    def stations_by_codec(self, codec, exact=False):
        """Lists all radio stations by codec.

        See details at:
        https://de1.api.radio-browser.info/#List_of_radio_stations



        Args:
            codec (str): The name of the codec.

        Returns:
            list: Stations.
        """
        if exact:
            endpoint = "{fmt}/stations/bycodecexact/{codec}".format(
                fmt=self._fmt, codec=codec
            )
        else:
            endpoint = "{fmt}/stations/bycodec/{codec}".format(
                fmt=self._fmt, codec=codec
            )
        return self.client.get(endpoint)

    def stations_by_country(self, country, exact=False):
        """Lists all radio stations by country.

        See details at:
        https://de1.api.radio-browser.info/#List_of_radio_stations


        Args:
            country (str): The name of the country.

        Returns:
            list: Stations.
        """
        if exact:
            endpoint = "{fmt}/stations/bycoutryexact/{country}".format(
                fmt=self._fmt, country=country
            )
        else:
            endpoint = "{fmt}/stations/bycountry/{country}".format(
                fmt=self._fmt, country=country
            )
        return self.client.get(endpoint)

    def stations_by_countrycode(self, code):
        """Lists all radio stations by country code.

        See details at:
        https://de1.api.radio-browser.info/#List_of_radio_stations


        Args:
            code (str): Official countrycodes as in ISO 3166-1 alpha-2.

        Returns:
            list: Stations.
        """

        endpoint = "{fmt}/stations/bycountrycodeexact/{code}".format(
            fmt=self._fmt, code=code
        )
        return self.client.get(endpoint)

    def stations_by_state(self, state, exact=False):
        """Lists all radio stations by state.

        See details at:
        https://de1.api.radio-browser.info/#List_of_radio_stations


        Args:
            state (str): The name of the state.

        Returns:
            list: Stations.
        """
        if exact:
            endpoint = "{fmt}/stations/bystateexact/{state}".format(
                fmt=self._fmt, state=state
            )
        else:
            endpoint = "{fmt}/stations/bystate/{state}".format(
                fmt=self._fmt, state=state
            )
        return self.client.get(endpoint)

    def stations_by_language(self, language, exact=False):
        """Lists all radio stations by language.

        See details at:
        https://de1.api.radio-browser.info/#List_of_radio_stations

        Args:
            language (str): The name of the language.

        Returns:
            list: Stations.
        """
        if exact:
            endpoint = "{fmt}/stations/bylanguageexact/{language}".format(
                fmt=self._fmt, language=language
            )
        else:

            endpoint = "{fmt}/stations/bylanguage/{language}".format(
                fmt=self._fmt, language=language
            )
        return self.client.get(endpoint)

    def stations_by_tag(self, tag, exact=False):
        """Lists all radio stations by tag.

        See details at:
        https://de1.api.radio-browser.info/#List_of_radio_stations

        Args:
            tag (str): The name of the tag.

        Returns:
            list: Stations.
        """
        if exact:
            endpoint = "{fmt}/stations/bytagexact/{tag}".format(
                fmt=self._fmt, tag=tag
            )
        else:
            endpoint = "{fmt}/stations/bytag/{tag}".format(
                fmt=self._fmt, tag=tag
            )
        return self.client.get(endpoint)

    def click_counter(self, stationuuid):
        """Increase the click count of a station by one.

        This should be called everytime when a user starts
        playing a stream to mark the stream more popular than others.
        Every call to this endpoint from the same IP address and for
        the same station only gets counted once per day. The call will
        return detailed information about the stream, supported output
        formats: JSON

        See details at:
        https://de1.api.radio-browser.info/#Count_station_click

        Args:
            stationuuid (str): A globally unique identifier for the station.

        Returns:
            dict: A dict containing informations about the radio station.
        """
        endpoint = "{fmt}/url/{uuid}".format(fmt=self._fmt, uuid=stationuuid)

        return self.client.get(endpoint)

    # def stations_byvotes(self, row_count):
    #     """A list of the highest-voted stations.

    #     You can add a parameter with the number of wanted stations.

    #     Args:
    #         row_count {int}: Number of wanted stations

    #     Returns:
    #         {list}: Stations
    #     TODO: endpoint = "{fmt}/stations/topvote/{row_count}" if row_count else "{fmt}/stations/topvote/"
    #     """
    #     return None

    # def vote_for_station(self, stationuuid):
    #     """Increase the vote count for the station by one.

    #     Can only be done by same IP address for one station every 10 minutes.
    #     If it woeks, the changed station will be returned as result.

    #     Args:
    #         stationuuid {str}: A globally unique identifier for the station.

    #     Returns:
    #         {dict}: Station

    #     TODO:
    #     https://de1.api.radio-browser.info/#Vote_for_station
    #     """
    #     return

    # def add_radio_station(self, **kwargs):
    #     """Add a radio station to the database.

    #     TODO:
    #     https://de1.api.radio-browser.info/#Add_radio_station
    #     """
    #     return None

    def stations(self, **kwargs):
        """Lists all radio stations.

        See details at:
        https://nl1.api.radio-browser.info/#List_of_all_radio_stations

        Returns:
            list: Stations.

        """
        endpoint = "{fmt}/stations".format(fmt=self._fmt)
        return self.client.get(endpoint, **kwargs)

    def search(self, **kwargs):
        """Advanced search.

        It will search for the station whose attribute
        contains the search term.

        See details at:
        https://de1.api.radio-browser.info/#Advanced_station_search

        Args:
            name (str, optional): Name of the station.
            name_exact (bool, optional): Only exact matches, otherwise all
                matches (default: False).
            country (str, optional): Country of the station.
            country_exact (bool, optional): Only exact matches, otherwise
                all matches (default: False).
            country_code (str, optional): 2-digit countrycode of the station
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

        Raises:
            ValueError: [description] # TODO
            ValueError: [description] # TODO

        Returns:
            list: Stations.

        Example:
            >>> from pyradios import RadioBrowser
            >>> rb = RadioBrowser()
            >>> rb.search(name="BBC Radio 1", name_exact=True)  # doctest: +ELLIPSIS
            [{'changeuuid': '4f7e4097-4354-11e8-b74d-52543be04c81', ...

        """
        _valid_kwargs = {
            "name": str,
            "name_exact": bool,
            "country": str,
            "country_exact": bool,
            "country_code": str,
            "state": str,
            "state_exact": bool,
            "language": str,
            "language_exact": bool,
            "tag": str,
            "tag_exact": bool,
            "tag_list": str,
            "bitrate_min": int,
            "bitrate_max": int,
            "order": str,
            "reverse": bool,
            "offset": int,
        }

        for key, value in kwargs.items():
            try:
                type_ = _valid_kwargs[key]
            except KeyError as exc:
                raise IllegalArgumentError(
                    "There is no paramter named '{}'".format(exc.args[0])
                )
            else:
                if not isinstance(value, type_):
                    raise TypeError(
                        "{} must be {}, not {}".format(
                            repr(key), type_.__name__, type(value).__name__,
                        )
                    )
                continue

        for key, value in kwargs.items():
            if isinstance(kwargs[key], bool):
                kwargs[key] = bool2string(value)

        endpoint = "{fmt}/stations/search".format(fmt=self._fmt)

        return self.client.get(endpoint, **kwargs)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
