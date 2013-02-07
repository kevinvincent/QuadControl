import socket

#Connect to Wifly
IPADDR = '169.254.1.1'
PORTNUM = 2000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

s.connect((IPADDR, PORTNUM))

while True:
    data = raw_input("send:")
    if(data == "EXIT"):
        s.close
        break
    else:
        print data
        s.send("<"+data+">")
