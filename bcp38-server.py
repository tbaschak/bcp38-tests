#!/usr/bin/env python

import socket
import sys

# Create a UDP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('0.0.0.0', 10000)
#print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

while True:
#    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(4096)
    
#    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
#    print >>sys.stderr, data

    responselines = data.splitlines()
    src_ip = responselines[0]
    udp_ip = address[0]

    if src_ip == udp_ip:
        print "udp src IP %s matches packet contents ip %s" % (udp_ip, src_ip)
    else:
        print "udp src IP %s DOES NOT MATCH packet contents ip %s" % (udp_ip, src_ip)
    
#    if data:
#        sent = sock.sendto(data, address)
#        print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
