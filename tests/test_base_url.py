import socket
from unittest.mock import Mock
from unittest.mock import patch

import pytest
from pyradios.base_url import fetch_servers


def getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
    """
    returns:
        (family, type, proto, canonname, sockaddr)
    """
    return_value = [
        ("family", "type", "proto", "canonname", ("192.168.1.1", 80)),
        ("family", "type", "proto", "canonname", ("192.168.1.2", 80)),
        ("family", "type", "proto", "canonname", ("192.168.1.3", 80)),
        ("family", "type", "proto", "canonname", ("192.168.1.4", 80)),
    ]
    return return_value


def test_fetch_servers():

    with patch("socket.getaddrinfo", getaddrinfo):
        assert fetch_servers() == [
            "192.168.1.1",
            "192.168.1.2",
            "192.168.1.3",
            "192.168.1.4",
        ]


def test_fetch_servers_network_failure():
    mock_getaddrinfo = Mock()
    mock_getaddrinfo.side_effect = socket.gaierror
    with patch("socket.getaddrinfo", mock_getaddrinfo):
        with pytest.raises(socket.gaierror) as exc_info:
            fetch_servers()
        assert issubclass(exc_info.type, (OSError,))
        assert exc_info.type == socket.gaierror
