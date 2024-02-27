import struct
import socket
import ipaddress


def ip2int(addr):
    """
    Convert an IP in string format to decimal format
    """

    return struct.unpack("!I", socket.inet_aton(addr))[0]


def check_ip(ip: str, network_range: str) -> bool:
    """
    Test if the IP is in range

    Range is expected to be in CIDR notation format. If no MASK is
    given /32 is used. It return True if the IP is in the range.
    """
    try:
        ip = ipaddress.ip_address(ip)
        network = ipaddress.ip_network(network_range, strict=False)
        if isinstance(ip, ipaddress.IPv6Address) and ip.ipv4_mapped is not None:
            ip = ipaddress.ip_address(ip.ipv4_mapped)
        if ip in network:
            return True
        else:
            return False
    except:  # noqa: E722
        return False
