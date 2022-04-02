#!/usr/bin/env python

from scapy import all as scapy


def scan(ip):
    scapy.arping(ip)


scan("192.168.1.1/24")
