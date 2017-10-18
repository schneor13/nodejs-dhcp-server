import socket
from socket import *
import sys
from random import Random
from optparse import OptionParser
from pydhcplib.dhcp_packet import DhcpPacket
from pydhcplib.dhcp_network import DhcpClient
from pydhcplib.type_hw_addr import hwmac
from pydhcplib.type_ipv4 import ipv4
import time


r = Random()
r.seed()

#time.sleep(r.randint(2,6))
#break_wait = 0
#res = None

#dhcp_ip = ''

# generamte a random mac address
def genmac():
        i = []
        for z in xrange(6):
                i.append(r.randint(0,255))
        return ':'.join(map(lambda x: "%02x"%x,i))

#generate a random xid
def genxid():
        decxid = r.randint(0,0xffffffff)
        xid = []
        for i in xrange(4):
                xid.insert(0, decxid & 0xff)
                decxid = decxid >> 8
        return xid

#set up a dhcp packet, this defaults to the discover type
def discoverP():
        req = DhcpPacket()
        req.SetOption('op',[1])
        req.SetOption('htype',[1])
        req.SetOption('hlen',[6])
        req.SetOption('hops',[0])
	
	xid = genxid()
        req.SetOption('xid',xid)
	chaddr = genmac()

        req.SetOption('giaddr',ipv4('0.0.0.0').list())
        req.SetOption('chaddr',hwmac(chaddr).list() + [0] * 10)
        req.SetOption('ciaddr',ipv4('0.0.0.0').list())
        #if msgtype == 'request':
        #        mt = 3
        #elif msgtype == 'release':
        #        mt = 7
        #else:
        #        mt = 1
        #if mt == 3:
        #        req.SetOption('yiaddr', ipv4(yiaddr).list())
        #        req.SetOption('request_ip_address', ipv4(yiaddr).list())
        req.SetOption('dhcp_message_type',[1])
        return req


sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('',0))
sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
server_address = ('<broadcast>', 9999)

print >>sys.stderr, 'connecting to %s port %s' % server_address
#sock.connect(server_address)

try:
    
    # Send data
    res = discoverP()
    print res.str()
    message = res.EncodePacket()

    #message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending...' # "%s"' % message
    sock.sendto(message, server_address)

    # Look for the response
    #amount_received = 0
    #amount_expected = len(message)
    #d = ''
    #while amount_received < amount_expected:
        
	#d += data
        #amount_received += len(data)
    data, server = sock.recvfrom(1024)


        #print >>sys.stderr, 'received "%s"' % data
    #offer handle
    offer = DhcpPacket()
    offer.DecodePacket(data)
    print offer.str()
    offer_add = offer.GetOption('yiaddr')
    offer.SetOption('yiaddr', ipv4('0.0.0.0').list())
    offer.SetOption('request_ip_address', offer_add) #ipv4(offer_add).list())
    offer.SetOption('dhcp_message_type',[3])
    print offer.str()
    message = offer.EncodePacket()


    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(('',0))
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    server_address = ('<broadcast>', 9999)    

#    print >>sys.stderr, 'connecting to %s port %s' % server_address
    #sock.connect(server_address)

    print >>sys.stderr, 'requesting...' # "%s"' % message
    sock.sendto(message, server_address)
    print 'requested waiting for response'
# Look for the response
    amount_received = 0
    amount_expected = len(message)
    d = ''
        
    data, addDUM = sock.recvfrom(1024)
    print 'after'
    
    #amount_received += len(data)
        #print >>sys.stderr, 'received "%s"' % data
    print data
    ack = DhcpPacket()
    ack.DecodePacket(data)
    print ack.str()
    print 'my i.p. id: '
    ip = ''
    for i in ack.GetOption('yiaddr'):
	ip += str(i) + "."
    print ip

    log = open('Log.txt', 'a')
    log.write(str(time.time()) + "\n")

finally:
    print >>sys.stderr, 'closing socket'
  
    sock.close()
