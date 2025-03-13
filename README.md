# Pyradios

![Upload Python Package](https://github.com/andreztz/pyradios/workflows/Upload%20Python%20Package/badge.svg)  
![Python package](https://github.com/andreztz/pyradios/workflows/Python%20package/badge.svg)

> A Python client for the [Radio Browser API](https://api.radio-browser.info), allowing users to search and filter thousands of online radio stations.

## 📥 Installation

Install `pyradios` via pip:

```sh
pip install pyradios

```

## 🚀 Usage

### Basic Example

```python
from pyradios import RadioBrowser

rb = RadioBrowser()
results = rb.search(name="BBC Radio 1", name_exact=True)

print(results)

```

### Sample Output

```json
[
  {
    "changeuuid": "4f7e4097-4354-11e8-b74d-52543be04c81",
    "stationuuid": "96062a7b-0601-11e8-ae97-52543be04c81",
    "name": "BBC Radio 1",
    "url": "http://bbcmedia.ic.llnwd.net/stream/bbcmedia_radio1_mf_p",
    "homepage": "http://www.bbc.co.uk/radio1/",
    "tags": "bbc,indie,entertainment,music,rock,pop",
    "country": "United Kingdom",
    "countrycode": "GB",
    "language": "english",
    "codec": "MP3",
    "bitrate": 128
  }
]

```

## 🔍 Faceted Search with `RadioFacets`

### What is `RadioFacets`?

`RadioFacets` extends `RadioBrowser` by providing faceted search functionality. It allows you to filter radio stations by various attributes such as:

-   **Tags** (`tags`)
-   **Country Code** (`countrycode`)
-   **Language** (`language`)
-   **State/Region** (`state`)
-   **Audio Codec** (`codec`)

### Example: Using `RadioFacets`

```python
from pyradios import RadioBrowser, RadioFacets

rb = RadioBrowser()
rf = RadioFacets(rb)

print(len(rf))  # Total stations available

rf_be = rf.narrow(countrycode="BE")  # Narrow by Belgium (BE)
print(len(rf_be))

rf_nl = rf_be.narrow(language="dutch")  # Further narrow by Dutch language
print(len(rf_nl))

rf_reset = rf_nl.broaden(countrycode="BE", language="dutch")  # Remove filters
print(len(rf_reset))  # Back to original count

```

### Explanation

-   **`narrow(**params)`** → Adds filters and narrows results.
-   **`broaden(*keys, **params)`** → Removes filters and broadens results.
-   **`len(rf)`** → Returns the number of stations matching the filters.
-   **`rf.result`** → Stores the list of filtered stations.

### Example Output

```sh
53768  # Total available stations
398    # Stations in Belgium
108    # Dutch-speaking stations in Belgium
53768  # Reset back to all stations

```

## 📖 Documentation

To explore all available methods and options, use Python’s built-in `help()` function:

```python
from pyradios import RadioBrowser, RadioFacets

help(RadioBrowser)
help(RadioFacets)

```

## 🛠 Development Setup

Clone the repository and set up the environment:

```sh
git clone https://github.com/andreztz/pyradios.git
cd pyradios
virtualenv venv
source venv/bin/activate
pip install -e .[dev]

```

## ✅ Running Tests

Execute the test suite using `pytest`:

```sh
pytest

```

## 📌 Release History

-   **Work in progress**

## 📄 License

Distributed under the MIT License. See `LICENSE` for more details.

## 👥 Contributing

Contributions are welcome! Follow these steps to contribute:

1.  **Fork the repository** ([https://github.com/andreztz/pyradios/fork](https://github.com/andreztz/pyradios/fork))
2.  **Create a feature branch** (`git checkout -b feature/fooBar`)
3.  **Commit your changes** (`git commit -am 'Add feature fooBar'`)
4.  **Push to your branch** (`git push origin feature/fooBar`)
5.  **Submit a Pull Request**

----------

📧 **Author:** Andre P. Santos – [@ztzandre](https://twitter.com/ztzandre) – [andreztz@gmail.com](mailto:andreztz@gmail.com)

GitHub: [https://github.com/andreztz](https://github.com/andreztz/)
