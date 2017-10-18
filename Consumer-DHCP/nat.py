import socket
import sys
from pydhcplib. dhcp_packet import DhcpPacket
from random import Random
from pydhcplib.type_ipv4 import ipv4
import time


hl = {}
for i in range(0,120):
	hl[i] = 0
#print hl

r = Random()
r.seed()
#time.sleep(1)

def genNum():
	i = []
	for z in xrange(6):
		i.append(r.randint(0,255))
	return ':'.join(map(lambda x: "%02x"%x,i))

def genHouse():
	global hl
	x = r.randint(0,119)
	if hl[x] < 9:
		hl[x] += 1
		return str(x)
	else:
		for i in range(0,119):
			if hl[i] < 9:
				hl[i] += 1
				return str(i)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('', 9999)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
#sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, '\nwaiting for a connection'
    data, address = sock.recvfrom(1024)

    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    #print >>sys.stderr, data
    #time.sleep(1)
    if data:
	p = DhcpPacket()
	p.DecodePacket(data)
	if p.GetOption('dhcp_message_type') == [1]:
		house = genHouse()
		houseIP = house + "." + house + "." + house + "." + house
	p.SetOption('ciaddr', ipv4(houseIP).list())
#	time.sleep(1)
	#connect and forward to server
	serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverADD = ('34.234.154.205', 10000)
	print >>sys.stderr, 'connecting to %s port %s' % serverADD
	serverSock.connect(serverADD)
	
	print >>sys.stderr, 'sending...'
	serverSock.sendall(p.EncodePacket())
	print 'sent'

	rec = 0
	exp = len(data)
	d = ''
	#while rec < exp:
	dataRec = serverSock.recv(1024)
	#	d += dataRec
	#	rec += len(dataRec)
#	time.sleep(1)
	print 'back to client'
	sent = sock.sendto(dataRec, address)
	print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)
