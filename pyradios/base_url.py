"""
This module get information about `Radio Browser` servers.
"""
import logging
import random
import socket


log = logging.getLogger("pyradios")


class Error(Exception):
    """Base class for all exceptions raised by this module."""
    pass


class RDNSLookupError(Error):
    def __init__(self, ip):
        self.ip = ip
        self.error_msg = (
            f'There was a problem with performing '
            f'reverse dns lookup for ip: {ip}'
        )
        super().__init__(self.error_msg)


def fetch_servers():
    """
    Get IP of all currently available `Radiob Browser` servers.

    Returns:
        list: List of IPs
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
    Reverse DNS lookup.

    Returns:
        str: hostname

    """
    try:
        hostname, _, _ = socket.gethostbyaddr(ip)
    except socket.herror as exc:
        raise RDNSLookupError(ip) from exc
    return hostname


def fetch_hosts():
    names = []
    servers = fetch_servers()

    for ip in servers:
        try:
            host_name = rdns_lookup(ip)
        except RDNSLookupError as exc:
            log.exception(exc.error_msg)
        else:
            names.append(host_name)
    return names


def pick_base_url():
    hosts = fetch_hosts()
    url = random.choice(sorted(hosts))
    return "https://{}/".format(url)
