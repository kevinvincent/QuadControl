#http://dlnmh9ip6v2uc.cloudfront.net/datasheets/Wireless/WiFi/WiFly-RN-UM.pdf
#http://niltoid.com/blog/rn-xv-wifly/

##import socket
##
##UDP_IP="0.0.0.0"
##UDP_PORT=5005
##
##sock = socket.socket( socket.AF_INET, # Internet
##                      socket.SOCK_DGRAM ) # UDP
##sock.bind( (UDP_IP,UDP_PORT) )
##
##while True:
##   print "Waiting for Wifly..."
##   data, addr = sock.recvfrom( 1024 ) # buffer size is 1024 bytes
##   print data,addr

import socket

# addressing information of target
IPADDR = '169.254.1.1'
PORTNUM = 2000

# initialize a socket, think of it as a cable
# SOCK_DGRAM specifies that this is UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

# connect the socket, think of it as connecting the cable to the address location
s.connect((IPADDR, PORTNUM))

for x in range(100):
   # send the command
   s.send(str(x))
   #s.send("*OPEN*"+str(x)+"\n*CLOS*")
   print x;

# close the socket
s.close()
