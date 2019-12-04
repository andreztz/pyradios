"""
Get all base urls of all currently available radiobrowser servers.

"""
import random
import socket

from pyradios.cache import cache
from pyradios.log import logger


class Error(Exception):
    """Base class for all exceptions raised by this module."""

    pass


class RdnsLookupError(Error):
    """There was a problem with performing a reverse dns lookup."""

    pass


def fetch_all_hosts():
    """
    Get all ip of all currently available radiobrowser servers.

    Returns:
        list: an ip list in string format

    """
    try:
        data = socket.getaddrinfo(
            "all.api.radio-browser.info", 80, 0, 0, socket.IPPROTO_TCP
        )
    except socket.gaierror as exc:
        logger.exception("Network failure: ")
        raise
    else:
        ips = [ip[4][0] for ip in data]
    return ips


def rdns_lookup(ip):
    """
    Do a reverse dns lookup.

    Resolves Domain Names into associated IP addresses.

    Returns:
        str: Domain Name

    """
    try:
        name = socket.gethostbyaddr(ip)
    except socket.herror as exc:
        if "Unknown host" in exc.args:
            raise RdnsLookupError("Unknown host")
        else:
            raise
    return name[0]


def pick_url(filename, expire, **kwargs):
    @cache(filename=filename, expire=expire, **kwargs)
    def fetch_hosts():
        names = []
        try:
            hosts = fetch_all_hosts()
        except Exception as exc:
            logger.exception("Network failure. ")
        else:
            for ip in hosts:
                try:
                    name = rdns_lookup(ip)
                except RdnsLookupError as exc:
                    logger.exception("Network failure. ")
                else:
                    names.append(name)
        return names

    try:
        names = fetch_hosts()
    except Exception as exc:
        logger.exception("Network failure. ")
        raise

    names.sort()
    url = random.choice(names)
    return "https://{}/".format(url)


if __name__ == "__main__":
    ips = fetch_all_hosts()

    print(ips)

    for ip in ips:
        print(ip)
        try:
            print(rdns_lookup(ip))
        except RdnsLookupError as exc:
            print("Network failure: " + str(exc))

    url = pick_url(filename="data.cache", expire=0)
    print(url)
