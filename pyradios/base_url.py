"""
Get all base urls of all currently available radiobrowser servers.
"""
import logging
import random
import socket


log = logging.getLogger("pyradios")


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
        list: A list of IPs
    """
    ips = []
    try:
        data = socket.getaddrinfo(
            "all.api.radio-browser.info", 80, 0, 0, socket.IPPROTO_TCP
        )
    except socket.gaierror:
        log.exception("Network failure")
        raise
    else:
        if data and isinstance(data[0][4], tuple):
            for ip in data:
                ips.append(ip[4][0])
    return ips


def rdns_lookup(ip):
    """
    Do reverse dns lookup.

    Returns:
        str: domain name

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
        log.exception("Network failure")
        raise
    else:
        for ip in hosts:
            try:
                name = rdns_lookup(ip)
            except RdnsLookupError:
                log.exception("Network failure")
            else:
                names.append(name)
    return names


def pick_base_url():

    try:
        names = fetch_hosts()
    except Exception:
        log.exception("Network failure")
        raise

    names.sort()
    url = random.choice(names)
    return "https://{}/".format(url)
