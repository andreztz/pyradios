"""
Get all base urls of all currently available radiobrowser servers

"""
import random
import socket

from pyradios.cache import cache
from pyradios.log import logger


def fetch_all_hosts():
    """
    Get all ip of all currently available radiobrowser servers.

    Returns:
        list: a list of strings

    """
    try:
        data = socket.getaddrinfo(
            "all.api.radio-browser.info", 80, 0, 0, socket.IPPROTO_TCP
        )
    except socket.gaierror as exc:
        logger.exception("Networking failure:")
    ips = [ip[4][0] for ip in data]
    return ips


def rdns_lookup(ip):
    """
    Do a reverse dns lookup.

    Resolves domain names into associated IP addresses.

    Returns:
        str: domain name

    """
    try:
        name = socket.gethostbyaddr(ip)
    except socket.herror as exc:
        logger.exception("Networking failure:")
    return name[0]


def pick_url(filename, expire, **kwargs):
    @cache(filename=filename, expire=expire, **kwargs)
    def fetch_hosts():
        return list({rdns_lookup(ip) for ip in fetch_all_hosts()})

    names = fetch_hosts()
    names.sort()
    url = random.choice(names)
    return "https://{}/".format(url)
