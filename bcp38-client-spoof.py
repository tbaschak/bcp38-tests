#!/usr/bin/env python

import socket
import sys
import requests
import string
from scapy.all import *

r = requests.get("http://4.ipquail.com/ip")

if r.status_code == 200:
    ipv4 = r.content.translate(None, string.whitespace)
else:
    ipv4 = 'err'

message = "%s" % ipv4

server  = '192.168.202.33'
fakesrc = '1.1.1.1'

srcport  = RandNum(1024,65535)
mypacket = IP(dst=server, src=ipv4)/UDP(sport=srcport,dport=10000)/message
l2packet = Ether()/mypacket
sendp(l2packet)

srcport  = RandNum(1024,65535)
mypacket = IP(dst=server, src=fakesrc)/UDP(sport=srcport,dport=10000)/message
l2packet = Ether()/mypacket
sendp(l2packet)

for x in range(0, 20):
    srcport  = RandNum(1024,65535)
    fakesrc  = RandIP()
    mypacket = IP(dst=server, src=RandIP())/UDP(sport=srcport,dport=10000)/message
    l2packet = Ether()/mypacket
    sendp(l2packet)

