import socket
import sys
from pydhcplib.dhcp_packet import DhcpPacket
from pydhcplib.type_hw_addr import hwmac
from pydhcplib.type_ipv4 import ipv4
import time


addr = 20
sub = 0
hl = {}
for i in range(0, 120):
        hl[i] = 0

def genADD(house):
        print 'the house is' + str(house)
        global hl
        global addr
        global sub
#       if hl[house] < 9:
        hl[house] += 1
        return '10.0.' + str(house) + "." + str(hl[house])
#       else:
#               for i in range(0,120):
#                       if hl[i] < 9:
#                               hl[i] += 1
#                               return '10.0.' + str(i) + "." + str(hl[i])


#               if sub < 4:
#                       sub += 1
#                       addr=0
#               else:
#                       return '0.0.0.0'
#       else:
#               addr += 1
#       return '10.0.' + str(sub) + '.' + str(addr)
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
logF = open('Log.txt', 'w')

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            if data:
                print >>sys.stderr, 'received' # "%s"' % data
                p = DhcpPacket()
                p.DecodePacket(data)
                print p.GetOption('dhcp_message_type')
                if p.GetOption('dhcp_message_type') == [1]:
                    print p.str()
                    print 'prepare'
                    p.SetOption('dhcp_message_type', [2])
                    yad = genADD(int(p.GetOption('ciaddr')[1]))
                    p.SetOption('yiaddr', ipv4(yad).list())
                    p.SetOption('siaddr', ipv4('34.234.154.205').list())
#                   p.SetOption('network_mask', ipv4('255.255.0.0').list())
                    print p.str()
                    print 'going to send'
                    connection.sendall(p.EncodePacket())
                    print 'sent'
                    break
                if p.GetOption('dhcp_message_type') == [3]:
                    print p.str()
                    print 'accepting request...'
                    p.SetOption('yiaddr', p.GetOption('request_ip_address'))
                    p.DeleteOption('request_ip_address')
                    p.SetOption('dhcp_message_type', [5])
                    print p.str()
                    givven = p.GetOption('yiaddr')
                    gIP = ''
                    for i in givven:
                        gIP += str(i) + "."
                    connection.sendall(p.EncodePacket())
                    print 'accepted and sent'
                    sec = time.time()
#                   milis = int(round(time.time() * 1000))
#                   logF = open('Log.txt', 'a')
                    logF.write("IP: " + gIP + " Time in seconds: " + str(sec) + "\n")
                    break

            else:
                break
#            if data:
#                       print >>sys.stderr, 'sending data back to the client'
#                connection.sendall(data)
#                   else:
#                       print >>sys.stderr, 'no more data from', client_address
#                break

    finally:
        # Clean up the connection
        connection.close()



