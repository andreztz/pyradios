# Pyradios

> A Python wrapper for the [Radio Browser](http://www.radio-browser.info/webservice).

[![Build Status][travis-image]][travis-url]

One to two paragraph statement about your product and what it does.

![](header.png)

## Installation

```sh
 pip install pyradios
```

## Usage example

```sh
In [1]: from pyradios import RadioBrowser

In [2]: rb = RadioBrowser()

In [3]: rb.stations_byid('92585')
Out[3]:
[{'id': '92585',
  'changeuuid': 'e78eb8c0-1a25-11e8-a334-52543be04c81',
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

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Release History

- 0.0.3
  - Work in progress

## Meta

Andre P. Santos – [@ztzandre](https://twitter.com/ztzandre) – andreztz@gmail.com

Distributed under the XYZ license. See `LICENSE` for more information.

[https://github.com/andreztz/github-link](https://github.com/andreztz/)

## Contributing

1. Fork it (<https://github.com/andreztz/pyradios/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->

[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
