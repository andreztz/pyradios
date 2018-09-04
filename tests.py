import unittest

from pyradios.radios import RadioBrowser


class TestRadioBrowser(unittest.TestCase):
    def setUp(self):
        self.rb = RadioBrowser()

    def test_station_byname_response(self):
        station = [
            {
                "id": "113234",
                "changeuuid": "26b48bb1-a490-11e8-abb8-52543be04c81",
                "stationuuid": "26b48b9d-a490-11e8-abb8-52543be04c81",
                "name": "DNB Radio Brazil",
                "url": "http://stm43.srvstm.com:21376/;",
                "homepage": "https://dnbradio.com.br/",
                "favicon": "https://dnbradio.com.br/wp/wp-content/uploads/2018/08/Sem-T%C3%ADtulo-3.png",
                "tags": "drum and bass",
                "country": "Brazil",
                "state": "",
                "language": "",
                "votes": "10",
                "negativevotes": "0",
                "lastchangetime": "2018-08-20 17:46:07",
                "ip": "78.18.215.141",
                "codec": "AAC+",
                "bitrate": "48",
                "hls": "0",
                "lastcheckok": "1",
                "lastchecktime": "2018-09-02 17:48:04",
                "lastcheckoktime": "2018-09-02 17:48:04",
                "clicktimestamp": "2018-09-02 07:34:25",
                "clickcount": "0",
                "clicktrend": "0",
            }
        ]
        expected_keys = station[0].keys()
        self.assertEqual(self.rb.stations_byname("DNB Radio Brazil")[0].keys(), expected_keys)

    def test_codecs_response(self):
        codecs = [
            {"name": "AAC", "value": "AAC", "stationcount": "624"},
            {"name": "AAC+", "value": "AAC+", "stationcount": "4062"},
            {"name": "AAC,H.264", "value": "AAC,H.264", "stationcount": "64"},
            {"name": "FLV", "value": "FLV", "stationcount": "3"},
            {"name": "MP3", "value": "MP3", "stationcount": "13792"},
            {"name": "MP3,H.264", "value": "MP3,H.264", "stationcount": "2"},
            {"name": "OGG", "value": "OGG", "stationcount": "211"},
            {"name": "UNKNOWN", "value": "UNKNOWN", "stationcount": "670"},
        ]
        expected_keys = codecs[0].keys()
        self.assertEqual(self.rb.codecs()[0].keys(), expected_keys)

    def test_codecs_response_with_filters(self):
        # filter example
        # http://www.radio-browser.info/webservice/json/codecs/aac
        # http://www.radio-browser.info/webservice/json/codecs/?reverse=true&hidebroken=true&order=stationcount
        codecs_aac = [
            {"name": "AAC", "value": "AAC", "stationcount": "624"},
            {"name": "AAC+", "value": "AAC+", "stationcount": "4063"},
            {"name": "AAC,H.264", "value": "AAC,H.264", "stationcount": "64"},
        ]
        expected_keys = codecs_aac[0].keys()
        self.assertEqual(self.rb.codecs(filters="aac")[0].keys(), expected_keys)

    def test_playable_station(self):
        playable_station = [
            {
                "id": "87019",
                "message": "retrieved station url successfully",
                "name": "TrancePulse FM",
                "ok": "true",
                "url": "http://sirius.shoutca.st:8878/stream",
            }
        ]
        self.assertEqual(self.rb.playable_station("87019")[0].keys(), playable_station[0].keys())
        self.assertEqual(
            self.rb.playable_station(stationid="87019")[0].keys(), playable_station[0].keys()
        )


if __name__ == "__main__":
    unittest.main()
