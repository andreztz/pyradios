# Pyradios

![Upload Python Package](https://github.com/andreztz/pyradios/workflows/Upload%20Python%20Package/badge.svg)
![Python package](https://github.com/andreztz/pyradios/workflows/Python%20package/badge.svg)

> Python client for the [Radio Browser API](https://api.radio-browser.info)


## Installation

```sh
 pip install pyradios
```

## Examples

```sh
In [1]: from pyradios import RadioBrowser

In [2]: rb = RadioBrowser()

In [3]: rb.search(name="BBC Radio 1", name_exact=True)
Out[3]:
[{'changeuuid': '4f7e4097-4354-11e8-b74d-52543be04c81',
  'stationuuid': '96062a7b-0601-11e8-ae97-52543be04c81',
  'name': 'BBC Radio 1',
  'url': 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p',
  'url_resolved': 'http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p',
  'homepage': 'http://www.bbc.co.uk/radio1/',
  'favicon': 'https://cdn-radiotime-logos.tunein.com/s24939q.png',
  'tags': 'bbc,indie,entertainment,music,rock,pop',
  'country': 'United Kingdom',
  'countrycode': 'GB',
  'state': '',
  'language': 'english',
  'votes': 5018,
  'lastchangetime': '2020-01-19 13:17:11',
  'codec': 'MP3',
  'bitrate': 128,
  'hls': 0,
  'lastcheckok': 1,
  'lastchecktime': '2020-02-03 19:44:37',
  'lastcheckoktime': '2020-02-03 19:44:37',
  'lastlocalchecktime': '2020-02-03 09:23:37',
  'clicktimestamp': '2020-02-04 00:16:54',
  'clickcount': 2880,
  'clicktrend': 40}]  
```
## Help

```python
In [1]: from pyradios import RadioBrowser

In [2]: help(RadioBrowser)
```


## Development Setup

```
$ git clone https://github.com/andreztz/pyradios.git
$ cd pyradios
$ virtualenv venv
$ source venv/bin/activate
$ pip install -e .[dev]
```

## Run Tests

```
$ pytest
```

## Release History

    - Work in progress

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
