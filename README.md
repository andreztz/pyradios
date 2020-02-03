# Pyradios

> A Python wrapper for the [Radio Browser](http://www.radio-browser.info/webservice).

![](header.png)

## Installation

```sh
 pip install pyradios
```

## Usage example

```sh
In [1]: from pyradios import RadioBrowser

In [2]: rb = RadioBrowser()

In [3]: rb.station_search(params={'name': 'BBC Radio 1', 'nameExact': 'true'})                
Out[3]: 
[{'changeuuid': '4f7e4097-4354-11e8-b74d-52543be04c81',
  'stationuuid': '96062a7b-0601-11e8-ae97-52543be04c81',
  'name': 'BBC Radio 1',
  'url': 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p',
  'homepage': 'http://www.bbc.co.uk/radio1/',
  'favicon': 'https://cdn-radiotime-logos.tunein.com/s24939q.png',
  'tags': 'bbc,indie,entertainment,music,rock,pop',
  'country': 'United Kingdom',
  'countrycode': 'GB',
  'state': '',
  'language': 'English',
  'votes': '4816',
  'negativevotes': '0',
  'lastchangetime': '2018-04-19 20:26:52',
  'ip': '5.15.39.213',
  'codec': 'MP3',
  'bitrate': '128',
  'hls': '0',
  'lastcheckok': '1',
  'lastchecktime': '2019-09-23 16:20:11',
  'lastcheckoktime': '2019-09-23 16:20:11',
  'clicktimestamp': '2019-09-24 10:21:47',
  'clickcount': '123',
  'clicktrend': '-12'}]
  
In [4]: rb.stations_byuuid('96062a7b-0601-11e8-ae97-52543be04c81')
Out[4]:
[{'changeuuid': 'e78eb8c0-1a25-11e8-a334-52543be04c81',
  'stationuuid': '9621d43e-0601-11e8-ae97-52543be04c81',
  'name': 'Radio Maria Südtirol',
  'url': 'http://s1.shoutitaly.com:8020/;',
  'homepage': 'http://radiomaria.bz.it/',
  'favicon': 'http://radiomaria.bz.it/wp-content/uploads/2013/04/Radio-Maria-S%C3%BCdtirol-340.jpg',
  'tags': 'bressanone,talk,catholic,christian',
  'country': 'Italy',
  'state': 'Trentino-Alto Adige/Südtirol',
  'language': 'German',
  'votes': '10',
  'negativevotes': '0',
  'lastchangetime': '2018-02-25 13:17:54',
  'ip': '176.31.180.157',
  'codec': 'MP3',
  'bitrate': '128',
  'hls': '0',
  'lastcheckok': '1',
  'lastchecktime': '2018-09-03 08:56:36',
  'lastcheckoktime': '2018-09-03 08:56:36',
  'clicktimestamp': '2018-09-03 09:57:59',
  'clickcount': '0',
  'clicktrend': '0'}]
  
```

## Development Setup

```
$ git clone https://github.com/andreztz/pyradios.git
$ cd pyradios
$ virtualenv venv
$ source venv/bin/activate
$ python setup.py develop
```

## Run Tests

```
$ virtualenv venv
$ source venv/bin/activate
$ python setup.py test
```

## Release History

    -   Work in progress

## Meta

Andre P. Santos – [@ztzandre](https://twitter.com/ztzandre) – andreztz@gmail.com

Distributed under the MIT LICENSE. See `LICENSE` for more information.

[https://github.com/andreztz](https://github.com/andreztz/)

## Contributing

1. Fork it (<https://github.com/andreztz/pyradios/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
