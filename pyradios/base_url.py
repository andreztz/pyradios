"""
Get all base urls of all currently available radiobrowser servers.

"""
import random
import socket

from pyradios.log import logger


class Error(Exception):
    """Base class for all exceptions raised by this module."""

    pass


class RdnsLookupError(Error):
    """There was a problem with performing reverse dns lookup."""

    pass


def fetch_all_hosts():
    """
    Get all ip of all currently available radiobrowser servers.

    Returns:
        list: ips

    """
    try:
        data = socket.getaddrinfo(
            "all.api.radio-browser.info", 80, 0, 0, socket.IPPROTO_TCP
        )
    except socket.gaierror:
        logger.exception("Network failure: ")
        raise
    else:
        ips = [ip[4][0] for ip in data]
    return ips


def rdns_lookup(ip):
    """
    Do reverse dns lookup.

    Returns:
        str: DNS

    """
    try:
        name = socket.gethostbyaddr(ip)
    except socket.herror as exc:
        if "Unknown host" in exc.args:
            raise RdnsLookupError("Unknown host")
        else:
            raise
    return name[0]


def fetch_hosts():
    names = []
    try:
        hosts = fetch_all_hosts()
    except Exception:
        logger.exception("Network failure. ")
    else:
        for ip in hosts:
            try:
                name = rdns_lookup(ip)
            except RdnsLookupError:
                logger.exception("Network failure. ")
            else:
                names.append(name)
    return names


def pick_base_url():

    try:
        names = fetch_hosts()
    except Exception:
        logger.exception("Network failure. ")
        raise

    names.sort()
    url = random.choice(names)
    return "https://{}/".format(url)


if __name__ == "__main__":
    url = pick_base_url()
    print(url)
