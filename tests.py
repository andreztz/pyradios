import unittest

from pyradios.radios import RadioBrowser, build_mask, build_endpoint

from collections import OrderedDict


class TestRadioBrowser(unittest.TestCase):
    def setUp(self):
        self.url_base = "http://www.radio-browser.info/webservice/"
        self.rb = RadioBrowser()

    def test_build_mask_one(self):
        kwargs = {
            "searchterm": "100",
            "format": "json",
            "endpoint": "stations/byid",
        }
        ordered = OrderedDict()
        ordered["format"] = kwargs.get("format")
        ordered["endpoint"] = kwargs.get("endpoint")
        ordered["searchterm"] = kwargs.get("searchterm")

        expected_result = "{format}/{endpoint}/{searchterm}/"
        self.assertEqual(build_mask(ordered), expected_result)

    def test_build_mask_two(self):
        kwargs = {"format": "xml", "filter": "aac", "endpoint": "codecs"}
        ordered = OrderedDict()
        ordered["format"] = kwargs.get("format")
        ordered["endpoint"] = kwargs.get("endpoint")
        ordered["filter"] = kwargs.get("filter")
        expected_result = "{format}/{endpoint}/{filter}/"

        self.assertEqual(build_mask(ordered), expected_result)

    """ tests build endpoins """

    def test_build_endpoint_with_codecs(self):
        expected_result = self.url_base + "json/codecs"
        url = build_endpoint(endpoint="codecs")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_languages(self):
        expected_result = self.url_base + "xml/languages"
        url = build_endpoint(endpoint="languages", format="xml")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_codecs_filter_format(self):
        expected_result = self.url_base + "xml/codecs/aac"
        url = build_endpoint(endpoint="codecs", format="xml", filter="aac")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_codecs_filter(self):
        expected_result = self.url_base + "json/codecs/mp3"
        url = build_endpoint(endpoint="codecs", filter="mp3")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_states(self):
        expected_result = self.url_base + "json/states"
        url = build_endpoint(endpoint="states")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_states_format(self):
        expected_result = self.url_base + "xml/states"
        url = build_endpoint(endpoint="states", format="xml")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_states_fomat_country(self):
        expected_result = self.url_base + "xml/states/brasil/"
        url = build_endpoint(endpoint="states", format="xml", country="brasil")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_with_states_filter_coutry(self):
        expected_result = self.url_base + "json/states/brazil/parana"
        url = build_endpoint(
            endpoint="states", country="brazil", filter="parana"
        )
        self.assertEqual(url, expected_result)

    """ stations by """

    def test_build_endpoint_stations(self):
        expected_result = self.url_base + "json/stations"
        url = build_endpoint(endpoint="stations")
        self.assertEqual(url, expected_result)

    def test_build_endpoint_stations_byid(self):
        expected_result = self.url_base + "json/stations/byid/87019"
        url = build_endpoint(endpoint="stations/byid", by="87019")
        self.assertEqual(url, expected_result)

    """ playable station url """

    def test_build_endpoint_playable_stations_url(self):
        expected_result = self.url_base + "v2/json/url/87019"
        url = build_endpoint(endpoint="url", by="87019", ver="v2")
        self.assertEqual(url, expected_result)

    def test_countries(self):
        expected_result = [
            {"name": "58", "value": "58", "stationcount": "1"},
            {"name": "AAA", "value": "AAA", "stationcount": "6"},
            {
                "name": "Afghanistan",
                "value": "Afghanistan",
                "stationcount": "3",
            },
            {"name": "Albania", "value": "Albania", "stationcount": "12"},
            {"name": "Alberta", "value": "Alberta", "stationcount": "1"},
            {"name": "Algeria", "value": "Algeria", "stationcount": "58"},
            {
                "name": "American Samoa",
                "value": "American Samoa",
                "stationcount": "1",
            },
            {"name": "Andorra", "value": "Andorra", "stationcount": "7"},
            {"name": "Angola", "value": "Angola", "stationcount": "10"},
            {"name": "Anguilla", "value": "Anguilla", "stationcount": "2"},
            {
                "name": "Antigua & Barbuda",
                "value": "Antigua & Barbuda",
                "stationcount": "7",
            },
            {"name": "Argentina", "value": "Argentina", "stationcount": "163"},
            {"name": "Armenia", "value": "Armenia", "stationcount": "8"},
            {"name": "Aruba", "value": "Aruba", "stationcount": "13"},
            {"name": "Australia", "value": "Australia", "stationcount": "254"},
            {"name": "Austria", "value": "Austria", "stationcount": "194"},
            {"name": "Bahamas", "value": "Bahamas", "stationcount": "12"},
            {"name": "Bahrain", "value": "Bahrain", "stationcount": "1"},
            {"name": "Bangladesh", "value": "Bangladesh", "stationcount": "24"},
            {"name": "Barbados", "value": "Barbados", "stationcount": "8"},
            {"name": "Bavaria", "value": "Bavaria", "stationcount": "1"},
            {"name": "Belarus", "value": "Belarus", "stationcount": "53"},
            {"name": "België", "value": "België", "stationcount": "4"},
            {"name": "Belgium", "value": "Belgium", "stationcount": "217"},
            {"name": "Benin", "value": "Benin", "stationcount": "1"},
            {"name": "Bermuda", "value": "Bermuda", "stationcount": "9"},
            {"name": "Bolivia", "value": "Bolivia", "stationcount": "14"},
            {
                "name": "Bosnia and Herzegovina",
                "value": "Bosnia and Herzegovina",
                "stationcount": "26",
            },
            {"name": "Botswana", "value": "Botswana", "stationcount": "2"},
            {
                "name": "Brandenburg",
                "value": "Brandenburg",
                "stationcount": "1",
            },
            {"name": "Brasil", "value": "Brasil", "stationcount": "43"},
            {"name": "Brazil", "value": "Brazil", "stationcount": "382"},
            {
                "name": "British Virgin Islands",
                "value": "British Virgin Islands",
                "stationcount": "1",
            },
            {"name": "Brunei", "value": "Brunei", "stationcount": "2"},
            {"name": "Bulgaria", "value": "Bulgaria", "stationcount": "99"},
            {"name": "Cambodia", "value": "Cambodia", "stationcount": "3"},
            {"name": "Cameroon", "value": "Cameroon", "stationcount": "2"},
            {"name": "Canada", "value": "Canada", "stationcount": "1017"},
            {"name": "Cape Verde", "value": "Cape Verde", "stationcount": "7"},
            {
                "name": "Cayman Islands",
                "value": "Cayman Islands",
                "stationcount": "9",
            },
            {
                "name": "Česká Republika",
                "value": "Česká Republika",
                "stationcount": "1",
            },
            {"name": "Chile", "value": "Chile", "stationcount": "93"},
            {"name": "China", "value": "China", "stationcount": "608"},
            {"name": "Colombia", "value": "Colombia", "stationcount": "219"},
            {
                "name": "Cook Islands",
                "value": "Cook Islands",
                "stationcount": "1",
            },
            {"name": "Costa Rica", "value": "Costa Rica", "stationcount": "22"},
            {"name": "Croatia", "value": "Croatia", "stationcount": "111"},
            {"name": "Cuba", "value": "Cuba", "stationcount": "5"},
            {"name": "Cyprus", "value": "Cyprus", "stationcount": "26"},
            {
                "name": "Czech Republic",
                "value": "Czech Republic",
                "stationcount": "168",
            },
            {"name": "de", "value": "de", "stationcount": "1"},
            {
                "name": "Democratic Republic of the Congo",
                "value": "Democratic Republic of the Congo",
                "stationcount": "2",
            },
            {"name": "Denmark", "value": "Denmark", "stationcount": "59"},
            {
                "name": "Deutschland",
                "value": "Deutschland",
                "stationcount": "29",
            },
            {"name": "Dominica", "value": "Dominica", "stationcount": "4"},
            {
                "name": "Dominican Republic",
                "value": "Dominican Republic",
                "stationcount": "28",
            },
            {"name": "Ecuador", "value": "Ecuador", "stationcount": "24"},
            {"name": "Egypt", "value": "Egypt", "stationcount": "12"},
            {
                "name": "El Salvador",
                "value": "El Salvador",
                "stationcount": "14",
            },
            {"name": "España", "value": "España", "stationcount": "12"},
            {
                "name": "España, spain",
                "value": "España, spain",
                "stationcount": "1",
            },
            {"name": "Estonia", "value": "Estonia", "stationcount": "52"},
            {"name": "EUA", "value": "EUA", "stationcount": "2"},
            {
                "name": "Falkland Islands",
                "value": "Falkland Islands",
                "stationcount": "1",
            },
            {
                "name": "Faroe Islands",
                "value": "Faroe Islands",
                "stationcount": "6",
            },
            {"name": "Fiji", "value": "Fiji", "stationcount": "6"},
            {"name": "Finland", "value": "Finland", "stationcount": "150"},
            {"name": "France", "value": "France", "stationcount": "1546"},
            {
                "name": "FUCK YOU NACI",
                "value": "FUCK YOU NACI",
                "stationcount": "9",
            },
            {"name": "Gambia", "value": "Gambia", "stationcount": "6"},
            {"name": "Georgia", "value": "Georgia", "stationcount": "4"},
            {"name": "Germany", "value": "Germany", "stationcount": "2176"},
            {"name": "Ghana", "value": "Ghana", "stationcount": "6"},
            {"name": "Gibraltar", "value": "Gibraltar", "stationcount": "1"},
            {
                "name": "Great Britan",
                "value": "Great Britan",
                "stationcount": "1",
            },
            {"name": "Greece", "value": "Greece", "stationcount": "217"},
            {"name": "Greenland", "value": "Greenland", "stationcount": "1"},
            {"name": "Grenada", "value": "Grenada", "stationcount": "12"},
            {"name": "Guam", "value": "Guam", "stationcount": "3"},
            {"name": "Guatemala", "value": "Guatemala", "stationcount": "16"},
            {"name": "Guinea", "value": "Guinea", "stationcount": "2"},
            {"name": "Guyana", "value": "Guyana", "stationcount": "5"},
            {"name": "Haiti", "value": "Haiti", "stationcount": "13"},
            {"name": "Honduras", "value": "Honduras", "stationcount": "28"},
            {"name": "Hungary", "value": "Hungary", "stationcount": "248"},
            {"name": "Ibiza", "value": "Ibiza", "stationcount": "1"},
            {"name": "Iceland", "value": "Iceland", "stationcount": "26"},
            {"name": "India", "value": "India", "stationcount": "140"},
            {"name": "Indonesia", "value": "Indonesia", "stationcount": "120"},
            {
                "name": "International",
                "value": "International",
                "stationcount": "2",
            },
            {"name": "Iran", "value": "Iran", "stationcount": "15"},
            {"name": "Iraq", "value": "Iraq", "stationcount": "7"},
            {"name": "Ireland", "value": "Ireland", "stationcount": "123"},
            {
                "name": "Isle of Man",
                "value": "Isle of Man",
                "stationcount": "5",
            },
            {"name": "Israel", "value": "Israel", "stationcount": "39"},
            {"name": "Italia", "value": "Italia", "stationcount": "4"},
            {"name": "Italy", "value": "Italy", "stationcount": "1141"},
            {
                "name": "Ivory Coast",
                "value": "Ivory Coast",
                "stationcount": "13",
            },
            {"name": "Jamaica", "value": "Jamaica", "stationcount": "16"},
            {"name": "Japan", "value": "Japan", "stationcount": "70"},
            {"name": "Jordan", "value": "Jordan", "stationcount": "7"},
            {"name": "Kazakhstan", "value": "Kazakhstan", "stationcount": "34"},
            {"name": "Kenya", "value": "Kenya", "stationcount": "6"},
            {"name": "Kosovo", "value": "Kosovo", "stationcount": "8"},
            {"name": "Kuwait", "value": "Kuwait", "stationcount": "4"},
            {"name": "Laos", "value": "Laos", "stationcount": "1"},
            {"name": "Latvia", "value": "Latvia", "stationcount": "61"},
            {"name": "Lebanon", "value": "Lebanon", "stationcount": "6"},
            {
                "name": "Liechtenstein",
                "value": "Liechtenstein",
                "stationcount": "5",
            },
            {"name": "Lithuania", "value": "Lithuania", "stationcount": "48"},
            {"name": "Luxembourg", "value": "Luxembourg", "stationcount": "17"},
            {"name": "Macedonia", "value": "Macedonia", "stationcount": "10"},
            {"name": "Madagascar", "value": "Madagascar", "stationcount": "5"},
            {"name": "Malawi", "value": "Malawi", "stationcount": "2"},
            {"name": "Malaysia", "value": "Malaysia", "stationcount": "6"},
            {"name": "Mali", "value": "Mali", "stationcount": "1"},
            {"name": "Malta", "value": "Malta", "stationcount": "19"},
            {"name": "Mauritius", "value": "Mauritius", "stationcount": "1"},
            {"name": "Mayotte", "value": "Mayotte", "stationcount": "1"},
            {"name": "Mexico", "value": "Mexico", "stationcount": "199"},
            {
                "name": "Mexico Spain",
                "value": "Mexico Spain",
                "stationcount": "1",
            },
            {"name": "milkyway", "value": "milkyway", "stationcount": "1"},
            {"name": "Moldova", "value": "Moldova", "stationcount": "38"},
            {"name": "Monaco", "value": "Monaco", "stationcount": "2"},
            {"name": "Montenegro", "value": "Montenegro", "stationcount": "10"},
            {
                "name": "Montpellier",
                "value": "Montpellier",
                "stationcount": "1",
            },
            {"name": "Montserrat", "value": "Montserrat", "stationcount": "1"},
            {"name": "Morocco", "value": "Morocco", "stationcount": "64"},
            {"name": "Mozambique", "value": "Mozambique", "stationcount": "10"},
            {
                "name": "NACI DEUTSCHLAND",
                "value": "NACI DEUTSCHLAND",
                "stationcount": "8",
            },
            {"name": "Namibia", "value": "Namibia", "stationcount": "2"},
            {"name": "Nederland", "value": "Nederland", "stationcount": "8"},
            {
                "name": "Nederländerna",
                "value": "Nederländerna",
                "stationcount": "2",
            },
            {"name": "Nepal", "value": "Nepal", "stationcount": "16"},
            {"name": "Netherland", "value": "Netherland", "stationcount": "2"},
            {
                "name": "Netherlands",
                "value": "Netherlands",
                "stationcount": "282",
            },
            {
                "name": "Netherlands Antilles",
                "value": "Netherlands Antilles",
                "stationcount": "22",
            },
            {
                "name": "Netherlands Sint Maarten",
                "value": "Netherlands Sint Maarten",
                "stationcount": "7",
            },
            {
                "name": "New Zealand",
                "value": "New Zealand",
                "stationcount": "50",
            },
            {"name": "Nicaragua", "value": "Nicaragua", "stationcount": "15"},
            {"name": "Nigeria", "value": "Nigeria", "stationcount": "5"},
            {"name": "Norway", "value": "Norway", "stationcount": "81"},
            {
                "name": "Nouvelle Calédonie",
                "value": "Nouvelle Calédonie",
                "stationcount": "1",
            },
            {"name": "Oregon", "value": "Oregon", "stationcount": "1"},
            {"name": "Pakistan", "value": "Pakistan", "stationcount": "3"},
            {"name": "Palestine", "value": "Palestine", "stationcount": "9"},
            {"name": "Panama", "value": "Panama", "stationcount": "17"},
            {
                "name": "Papua New Guinea",
                "value": "Papua New Guinea",
                "stationcount": "2",
            },
            {"name": "Paraguay", "value": "Paraguay", "stationcount": "16"},
            {"name": "PARIS", "value": "PARIS", "stationcount": "1"},
            {"name": "Peru", "value": "Peru", "stationcount": "144"},
            {
                "name": "Philippines",
                "value": "Philippines",
                "stationcount": "19",
            },
            {"name": "playing", "value": "playing", "stationcount": "10"},
            {"name": "Poland", "value": "Poland", "stationcount": "707"},
            {"name": "Polska", "value": "Polska", "stationcount": "7"},
            {"name": "Portugal", "value": "Portugal", "stationcount": "195"},
            {
                "name": "Principato di Monaco",
                "value": "Principato di Monaco",
                "stationcount": "1",
            },
            {
                "name": "Puerto Rico",
                "value": "Puerto Rico",
                "stationcount": "25",
            },
            {"name": "Qatar", "value": "Qatar", "stationcount": "6"},
            {
                "name": "Republic of Srpska",
                "value": "Republic of Srpska",
                "stationcount": "1",
            },
            {
                "name": "Republic of the Congo",
                "value": "Republic of the Congo",
                "stationcount": "1",
            },
            {
                "name": "República Dominicana",
                "value": "República Dominicana",
                "stationcount": "1",
            },
            {"name": "Romania", "value": "Romania", "stationcount": "122"},
            {"name": "ROYAN", "value": "ROYAN", "stationcount": "1"},
            {"name": "Russia", "value": "Russia", "stationcount": "566"},
            {
                "name": "Russian Federation",
                "value": "Russian Federation",
                "stationcount": "17",
            },
            {"name": "Rwanda", "value": "Rwanda", "stationcount": "3"},
            {
                "name": "Saint Lucia",
                "value": "Saint Lucia",
                "stationcount": "7",
            },
            {
                "name": "Saint Vincent and the Grenadines",
                "value": "Saint Vincent and the Grenadines",
                "stationcount": "7",
            },
            {"name": "San Marino", "value": "San Marino", "stationcount": "4"},
            {
                "name": "Saudi Arabia",
                "value": "Saudi Arabia",
                "stationcount": "11",
            },
            {"name": "Senegal", "value": "Senegal", "stationcount": "7"},
            {"name": "Serbia", "value": "Serbia", "stationcount": "137"},
            {"name": "Seychelles", "value": "Seychelles", "stationcount": "7"},
            {
                "name": "Sierra Leone",
                "value": "Sierra Leone",
                "stationcount": "1",
            },
            {"name": "Singapore", "value": "Singapore", "stationcount": "14"},
            {"name": "Slovakia", "value": "Slovakia", "stationcount": "82"},
            {"name": "Slovenia", "value": "Slovenia", "stationcount": "31"},
            {
                "name": "South Africa",
                "value": "South Africa",
                "stationcount": "55",
            },
            {
                "name": "South Korea",
                "value": "South Korea",
                "stationcount": "19",
            },
            {"name": "Spain", "value": "Spain", "stationcount": "464"},
            {
                "name": "Spain, España",
                "value": "Spain, España",
                "stationcount": "46",
            },
            {"name": "Sri Lanka", "value": "Sri Lanka", "stationcount": "10"},
            {"name": "St. Helena", "value": "St. Helena", "stationcount": "1"},
            {
                "name": "St. Kitts-Nevis",
                "value": "St. Kitts-Nevis",
                "stationcount": "1",
            },
            {"name": "Sudan", "value": "Sudan", "stationcount": "1"},
            {"name": "Suisse", "value": "Suisse", "stationcount": "2"},
            {"name": "Suriname", "value": "Suriname", "stationcount": "3"},
            {"name": "Sweden", "value": "Sweden", "stationcount": "122"},
            {
                "name": "Switzerland",
                "value": "Switzerland",
                "stationcount": "408",
            },
            {"name": "Syria", "value": "Syria", "stationcount": "4"},
            {"name": "Szolnok", "value": "Szolnok", "stationcount": "1"},
            {"name": "Taiwan", "value": "Taiwan", "stationcount": "12"},
            {"name": "Tajikistan", "value": "Tajikistan", "stationcount": "1"},
            {"name": "Tanzania", "value": "Tanzania", "stationcount": "2"},
            {"name": "Thailand", "value": "Thailand", "stationcount": "53"},
            {"name": "Tibet", "value": "Tibet", "stationcount": "1"},
            {"name": "Tonga", "value": "Tonga", "stationcount": "1"},
            {
                "name": "Trinidad and Tobago",
                "value": "Trinidad and Tobago",
                "stationcount": "20",
            },
            {"name": "Tunisia", "value": "Tunisia", "stationcount": "25"},
            {"name": "Turkey", "value": "Turkey", "stationcount": "119"},
            {
                "name": "Turks & Caicos Islands",
                "value": "Turks & Caicos Islands",
                "stationcount": "3",
            },
            {"name": "Uganda", "value": "Uganda", "stationcount": "2"},
            {"name": "UK", "value": "UK", "stationcount": "2"},
            {"name": "Ukraine", "value": "Ukraine", "stationcount": "80"},
            {
                "name": "United Arab Emirates",
                "value": "United Arab Emirates",
                "stationcount": "17",
            },
            {
                "name": "United Kingdom",
                "value": "United Kingdom",
                "stationcount": "641",
            },
            {
                "name": "United States",
                "value": "United States",
                "stationcount": "9",
            },
            {
                "name": "United States of America",
                "value": "United States of America",
                "stationcount": "3733",
            },
            {"name": "Uruguay", "value": "Uruguay", "stationcount": "30"},
            {"name": "US", "value": "US", "stationcount": "3"},
            {
                "name": "US Virgin Islands",
                "value": "US Virgin Islands",
                "stationcount": "13",
            },
            {"name": "USA", "value": "USA", "stationcount": "45"},
            {"name": "Uzbekistan", "value": "Uzbekistan", "stationcount": "1"},
            {"name": "Vanuatu", "value": "Vanuatu", "stationcount": "2"},
            {
                "name": "Vatican City State",
                "value": "Vatican City State",
                "stationcount": "12",
            },
            {"name": "Venezuela", "value": "Venezuela", "stationcount": "16"},
            {"name": "Vietnam", "value": "Vietnam", "stationcount": "2"},
            {
                "name": "Vigo - Pontevedra",
                "value": "Vigo - Pontevedra",
                "stationcount": "1",
            },
            {"name": "Worldwide", "value": "Worldwide", "stationcount": "2"},
            {"name": "Yemen", "value": "Yemen", "stationcount": "1"},
            {"name": "Zimbabwe", "value": "Zimbabwe", "stationcount": "2"},
            {"name": "Россия", "value": "Россия", "stationcount": "15"},
            {"name": "Руссия", "value": "Руссия", "stationcount": "1"},
            {"name": "Украина", "value": "Украина", "stationcount": "2"},
        ]
        resp = self.rb.countries()
        self.assertEqual(resp, expected_result)

    def test_countries(self):
        expected_result = [
            {"name": "Brazil", "value": "Brazil", "stationcount": "382"}
        ]
        resp = self.rb.countries("Brazil")
        self.assertEqual(resp, expected_result)

    def test_states(self):
        expected_result = [{'name': 'Alberta',
                            'value': 'Alberta',
                            'country': 'Canada',
                            'stationcount': '111'},
                            {'name': 'Baden-Württemberg',
                            'value': 'Baden-Württemberg',
                            'country': 'Deutschland',
                            'stationcount': '3'},
                            {'name': 'Baden-Württemberg',
                            'value': 'Baden-Württemberg',
                            'country': 'Germany',
                            'stationcount': '75'},
                            {'name': 'Bergdietikon',
                            'value': 'Bergdietikon',
                            'country': 'Switzerland',
                            'stationcount': '1'},
                            {'name': 'Bergen',
                            'value': 'Bergen',
                            'country': 'Norway',
                            'stationcount': '2'},
                            {'name': 'Berkshire',
                            'value': 'Berkshire',
                            'country': 'United Kingdom',
                            'stationcount': '1'},
                            {'name': 'Berlin',
                            'value': 'Berlin',
                            'country': 'Deutschland',
                            'stationcount': '1'},
                            {'name': 'Berlin',
                            'value': 'Berlin',
                            'country': 'Germany',
                            'stationcount': '233'},
                            {'name': 'Berlin-Brandenburg',
                            'value': 'Berlin-Brandenburg',
                            'country': 'Germany',
                            'stationcount': '1'},
                            {'name': 'Berlin/Brandenburg',
                            'value': 'Berlin/Brandenburg',
                            'country': 'Deutschland',
                            'stationcount': '1'},
                            {'name': 'Bern',
                            'value': 'Bern',
                            'country': 'Switzerland',
                            'stationcount': '21'},
                            {'name': 'Brandenburg Oberhavel',
                            'value': 'Brandenburg Oberhavel',
                            'country': 'Deutschland',
                            'stationcount': '1'},
                            {'name': 'Humberside',
                            'value': 'Humberside',
                            'country': 'United Kingdom',
                            'stationcount': '2'},
                            {'name': 'Kronoberg',
                            'value': 'Kronoberg',
                            'country': 'Sweden',
                            'stationcount': '3'},
                            {'name': 'La Libertad',
                            'value': 'La Libertad',
                            'country': 'El Salvador',
                            'stationcount': '1'},
                            {'name': 'Oberoesterreich',
                            'value': 'Oberoesterreich',
                            'country': 'Austria',
                            'stationcount': '1'},
                            {'name': 'Szabolcs-Szatmár-Bereg',
                            'value': 'Szabolcs-Szatmár-Bereg',
                            'country': 'Hungary',
                            'stationcount': '4'},
                            {'name': 'Tønsberg',
                            'value': 'Tønsberg',
                            'country': 'Norway',
                            'stationcount': '1'},
                            {'name': 'Vorarlberg',
                            'value': 'Vorarlberg',
                            'country': 'Austria',
                            'stationcount': '7'},
                            {'name': 'Красноярский край, Шушенское, Siberia',
                            'value': 'Красноярский край, Шушенское, Siberia',
                            'country': 'Russia',
                            'stationcount': '1'}]

        resp = self.rb.states("ber")
        self.assertEqual(resp, expected_result)

    def test_states_with_country(self):
        expected_result = [
            {
                'name': 'Baden-Württemberg',
                'value': 'Baden-Württemberg',
                'country': 'Germany',
                'stationcount': '75'
            },
            {
                'name': 'Berlin',
                'value': 'Berlin',
                'country': 'Germany',
                'stationcount': '233'
            },
            {'name': 'Berlin-Brandenburg',
                'value': 'Berlin-Brandenburg',
                'country': 'Germany',
                'stationcount': '1'
            }
        ]
        resp = self.rb.states("ber", country='Germany')
        self.assertEqual(resp[0].keys(), expected_result[0].keys())

    def test_search(self):
        expected_result = [{'id': '87019',
            'changeuuid': '9615f296-0601-11e8-ae97-52543be04c81',
            'stationuuid': '9615f293-0601-11e8-ae97-52543be04c81',
            'name': 'TrancePulse FM',
            'url': 'http://sirius.shoutca.st:8878/stream',
            'homepage': 'http://www.trancepulsefm.com/',
            'favicon': 'http://www.trancepulsefm.com/files/theme/favicon.ico',
            'tags': 'edm,electronic,dance,trance',
            'country': 'Ireland',
            'state': '',
            'language': 'English',
            'votes': '46',
            'negativevotes': '0',
            'lastchangetime': '2017-11-15 11:04:06',
            'ip': '195.39.210.66',
            'codec': 'MP3',
            'bitrate': '160',
            'hls': '0',
            'lastcheckok': '1',
            'lastchecktime': '2018-09-06 11:04:53',
            'lastcheckoktime': '2018-09-06 11:04:53',
            'clicktimestamp': '2018-09-06 23:52:29',
            'clickcount': '6',
            'clicktrend': '5'}
        ]

        params = {'name': 'TrancePulse FM'}
        resp = self.rb.station_search(params=params)
        self.assertEqual(resp, expected_result)
if __name__ == "__main__":
    unittest.main()
