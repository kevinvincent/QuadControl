#!/usr/bin/env python

import pygame
import time
import socket

from utils import *
from gui import *

#Initilize StickViewer
win = initWindow()
leftCircle = initLeftCircle(win)
rightCircle = initRightCircle(win)

leftStick = initLeftStick(win)
rightStick = initRightStick(win)

wiflystatus = Text(Point(300,15),"Waiting for Wifly...")
wiflystatus.draw(win)

joystatus = Text(Point(300,35),"Connecting to Joystick...")
joystatus.draw(win)

dat = Text(Point(300,285),"")
dat.draw(win)

win.update()

time.sleep(1)

#Initilize Joystick
pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

joystatus.setText('Initializing Joystick...')
win.update()
time.sleep(2)
joystatus.setText('Initialized Joystick: %s' % j.get_name())
win.update()

#Connect to Wifly
IPADDR = '169.254.1.1'
PORTNUM = 2000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)

s.connect((IPADDR, PORTNUM))
time.sleep(1)
while True:
    try:
        s.connect((IPADDR, PORTNUM))
        s.send("")
        break;
    except Exception, e:
        wiflystatus.setText("Retrying: " + str(e))
        win.update()
        time.sleep(1)
s.close()
time.sleep(1)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
s.connect((IPADDR, PORTNUM))
time.sleep(1)
while True:
    try:
        s.connect((IPADDR, PORTNUM))
        s.send("")
        break;
    except Exception, e:
        wiflystatus.setText("Retrying: " + str(e))
        win.update()
        time.sleep(1)
time.sleep(1)
wiflystatus.setText("Wifly Status: Connected!")
win.update()
        
#Constants
THROTTLE_AXIS = 1;
YAW_AXIS = 0;
ROLL_AXIS = 2;
PITCH_AXIS = 3;

BUTTON_X = 14
 
throttle = 0.00
yaw = 0.00
roll = 0.00
pitch = 0.00

#Wait to Arm
while(pygame.event.pump() and not j.get_axis(THROTTLE_AXIS)==9.99):
    continue;
try:
    while True:
        pygame.event.pump()

        #Raw Values FTW!
        yaw = j.get_axis(YAW_AXIS)*100
        throttle = j.get_axis(THROTTLE_AXIS)*-100
        roll = (j.get_axis(ROLL_AXIS)*100)
        pitch = (j.get_axis(PITCH_AXIS)*-100)

        #Update StickViewer
        leftCircle = updateLeftCircle(win,leftCircle,throttle,yaw)
        rightCircle = updateRightCircle(win,rightCircle,pitch,roll)

        leftStick = updateLeftStick(win,leftStick,throttle,yaw)
        rightStick = updateRightStick(win,rightStick,pitch,roll)

        #Normalize Expo and Map throttle
        roll = translate(roll**3,-1000000,1000000,-100,100)
        pitch = translate(pitch**3,-1000000,1000000,-100,100)
        throttle = translate(throttle,-100,100,0,100)

        dat.setText("%4.4s" % str(throttle) + "\t" + "%4.4s" % str(yaw) + "\t" + "%4.4s" % str(pitch) + "\t" +"%4.4s" % str(roll))

        win.update()
        
        #Send to Wifly
        #print "throttle:" + "%4.4s" % str(throttle) + "\t yaw:" + "%4.4s" % str(yaw) + "\t pitch:" + "%4.4s" % str(pitch) + "\t roll:" +"%4.4s" % str(roll) 

        try:
            s.send("@\t"+"%4.4s" % str(throttle) + "\t" + "%4.4s" % str(yaw) + "\t" + "%4.4s" % str(pitch) + "\t" +"%4.4s" % str(roll) + "\t!\n")
        except Exception, e:
            print e
            
        time.sleep(.1)
        
        if(j.get_button(BUTTON_X)):
            s.send("@\t"+"0.00\t" + "%4.4s" % str(yaw) + "\t" + "%4.4s" % str(pitch) + "\t" +"%4.4s" % str(roll) + "\t!\n")
            j.quit()
         
        for i in range(0, j.get_numbuttons()):
            if j.get_button(i) != 0:
                print 'Button %i reads %i' % (i, j.get_button(i))
               
except Exception, e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]      
    print(exc_type, fname, exc_tb.tb_lineno)
    throttle = 0;
    s.close()
    win.close();
