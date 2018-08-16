#!/usr/bin/python3

from dnslib.fixedresolver import DNSLogger, DNSServer, FixedResolver

if __name__ == '__main__':
    import os
    import sys
    fullpath = os.path.abspath(__file__)
    parentdir = '/'.join(fullpath.split('/')[:-2])
    sys.path.insert(0, parentdir)

from comitup import nm, modemgr

udp_server = None


def get_ip():
    return nm.get_active_ip(modemgr.get_ap_device())


def start_dns(ip_addr, port=1553, ttl=5):
    global udp_server
    response = ". {0} IN A {1}".format(ttl, ip_addr)

    if udp_server:
        udp_server.stop()

    resolver = FixedResolver(response)

    logger = DNSLogger("-request,-reply,-truncated,-error", False)

    udp_server = DNSServer(resolver, port=port, logger=logger)
    udp_server.start_thread()


def stop_dns():
    global udp_server

    if udp_server:
        udp_server.stop()

    udp_server = None


def state_callback(state, action):
    if (state, action) == ("HOTSPOT", "start"):
        start_dns(get_ip())
    elif (state, action) == ("CONNECTED", "start"):
        stop_dns()


if __name__ == "__main__":
    import time

    start_dns(get_ip())

    try:
        while True:
            time.sleep(.1)
    except KeyboardInterrupt:
        stop_dns()
