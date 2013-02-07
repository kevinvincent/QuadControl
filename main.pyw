import socket
import StringIO
import csv
import pprint

UDP_IP="0.0.0.0"
UDP_PORT=5005
    
sock = socket.socket( socket.AF_INET, # Internet
                          socket.SOCK_DGRAM ) # UDP
sock.bind( (UDP_IP,UDP_PORT) )

print "reading port"

def clamp(n, minn, maxn):
    return max(min(maxn, n), minn)

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    values = data.strip().split(',')
    
    p_num = int(values[1])
    yaw   = float(values[3])
    pitch = float(values[5])*-1
    roll  = float(values[4])
    
    pitch = clamp(pitch,-90,90)
    roll = clamp(roll,-90,90)
    
    print "packet:" + "%5.5s" % str(p_num) + "\t yaw:" + "%5.5s" % str(yaw) + "\t pitch:" + "%5.5s" % str(pitch) + "\t roll:" +"%5.5s" % str(roll)
