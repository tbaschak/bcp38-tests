#!/usr/bin/env python

import socket
import sys
import requests
import string

r = requests.get("http://4.ipquail.com/ip")

if r.status_code == 200:
    ipv4 = r.content.translate(None, string.whitespace)
else:
    ipv4 = 'err'

#print ipv4

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('192.168.203.22', 10000)
message = "This is a test message from\n%s" % ipv4

try:

    # Send data
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, server_address)

    # Receive response
#    print >>sys.stderr, 'waiting to receive'
#    data, server = sock.recvfrom(4096)
#    print >>sys.stderr, 'received "%s"' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
