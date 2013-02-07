from gui import *
import time

win = initWindow()

leftCircle = initLeftCircle(win)
rightCircle = initRightCircle(win)

leftStick = initLeftStick(win)
rightStick = initRightStick(win)

for x in range(0,100,1):
    leftCircle = updateLeftCircle(win,leftCircle,0,-x)
    rightCircle = updateRightCircle(win,rightCircle,0,-x)
    
    leftStick = updateLeftStick(win,leftStick,0,-x)
    rightStick = updateRightStick(win,rightStick,0,-x)
    time.sleep(.05)
    
    win.update()
    
win.close()
