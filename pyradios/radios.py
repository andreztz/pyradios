import requests
from pyradios.base_url import pick_base_url


class Request:
    def __init__(self, fmt, **kwargs):

        self._fmt = fmt

        if "base_url" in kwargs:  # for tests with lib response
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

        Args:
            code ({str}, optional): Filter by country code. Defaults to None.

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

        Args:
            code ({str}, optional): Filter by country code. Defaults to None.

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

        Args:
            codec ({str}, optional): Filter by codec. Defaults to None.

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

        Args:
            country ({str}, optional): Filter by country. Defaults to None.
            state ({str}, optionla): Filter by state.  Defaults to None.

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

        Args:
            language ({str}, optional): Filter by language. Defaults to None.

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

        Args:
            tag ({str}, optional): Filter by tag. Defaults to None.

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

        Args:
            stationuuid {str}: A globally unique identifier for the station.

        Returns:
            list: Stations.
        """
        endpoint = "{fmt}/stations/byuuid/{uuid}".format(
            fmt=self._fmt, uuid=stationuuid
        )

        return self.client.get(endpoint)

    def stations_by_name(self, name, exact=False):
        """Lists all radio stations by name.

        Args:
            name {str}: The name of the station.

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

        Args:
            codec {str}: The name of the codec.

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

        Args:
            country {str}: The name of the country.

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

        Args:
            code {str}: Official countrycodes as in ISO 3166-1 alpha-2.

        Returns:
            list: Stations.
        """

        endpoint = "{fmt}/stations/bycountrycodeexact/{code}".format(
            fmt=self._fmt, code=code
        )
        return self.client.get(endpoint)

    def stations_by_state(self, state, exact=False):
        """Lists all radio stations by state.

        Args:
            state {str}: The name of the state.

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

        Args:
            language {str}: The name of the language.

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

        Args:
            tag {str}: The name of the tag.

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

        Args:
            stationuuid {str}: A globally unique identifier for the station.

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

        Returns:
            list: Stations.

        https://nl1.api.radio-browser.info/#List_of_all_radio_stations
        """
        endpoint = "{fmt}/stations".format(fmt=self._fmt)
        return self.client.get(endpoint, **kwargs)

    def search(self, **kwargs):
        """Advanced search.

        It will search for the station whose attribute
        contains the search term.

        Args:
            name ({str}, optional): Name of the station.
            nameExact ({bool}, optional): Only exact matches, otherwise all
                matches (default: False).
            country ({str}, optional): Country of the station.
            countryExact ({bool}, optional): Only exact matches, otherwise
                all matches (default: False).
            countrycode ({str}, optional): 2-digit countrycode of the station
                (see ISO 3166-1 alpha-2)
            state ({str}, optional): State of the station.
            stateExact ({bool}, optional): Only exact matches, otherwise all
                matches. (default: False)
            language ({str}, optional): Language of the station.
            languageExact ({bool}, optional): Only exact matches, otherwise
                all matches. (default: False)
            tag ({str}, optional): Tag of the station.
            tagExact ({bool}, optional): Only exact matches, otherwise all
                matches. (default: False)
            tagList ({str}, optional): A comma-separated list of tag.
            bitrateMin ({int}, optional): Minimum of kbps for bitrate field of
                stations in result. (default: 0)
            bitrateMax ({int}, optional): Maximum of kbps for bitrate field of
                stations in result. (default: 1000000)
            order ({str}, optional): The result list will be sorted by: name,
                url, homepage, favicon, tags, country, state, language, votes,
                codec, bitrate, lastcheckok, lastchecktime, clicktimestamp,
                clickcount, clicktrend, random
            reverse ({bool}, optional): Reverse the result list if set to true.
                (default: false)
            offset ({int}, optional): Starting value of the result list from
                the database. For example, if you want to do paging on the
                server side. (default: 0)

        Returns:
            list: Stations.

        http://www.radio-browser.info/webservice#Advanced_station_search
        """

        endpoint = "{fmt}/stations/search".format(fmt=self._fmt)
        return self.client.get(endpoint, **kwargs)
