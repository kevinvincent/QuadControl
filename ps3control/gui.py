from graphics import *

def initWindow():
        win = GraphWin("Stick Viewer", 600, 300, autoflush=False)
        win.setBackground("white")

        leftBox = Rectangle(Point(100,100) , Point(200,200))
        leftBox.setOutline("red")
        leftBox.draw(win)

        rightBox = Rectangle(Point(400,100) , Point(500,200))
        rightBox.setOutline("red")
        rightBox.draw(win)

        return win

def initLeftCircle(win):
        lc = Circle(Point(150,150), 5)
        lc.setFill("gray")
        lc.draw(win)

        return lc
        

def initRightCircle(win):
        rc = Circle(Point(450,150), 5)
        rc.setFill("gray")
        rc.draw(win)

        return rc

def updateLeftCircle(win,leftStick,throttle,yaw):
        try:
                leftStick.undraw()
        except Exception:
                pass

        leftStick = Circle(Point(150+(yaw),150+(throttle*-1)), 10)
        leftStick.setFill("gray");
        leftStick.draw(win)

        return leftStick

def updateRightCircle(win,rightStick,pitch,roll):
        try:
                rightStick.undraw()
        except Exception:
                pass
        
        rightStick = Circle(Point(450+(roll),150+(pitch*-1)), 10)
        rightStick.setFill("gray")
        rightStick.draw(win)

        return rightStick

def initLeftStick(win):
        lc = Line(Point(150,150), Point(150,150))
        lc.setFill("gray")
        lc.draw(win)

        return lc
        

def initRightStick(win):
        rc = Line(Point(450,150), Point(450,150))
        rc.setFill("gray")
        rc.draw(win)

        return rc

def updateLeftStick(win,leftStick,throttle,yaw):
        try:
                leftStick.undraw()
        except Exception:
                pass

        leftStick = Line(Point(150+(yaw),150+(throttle*-1)), Point(150,150))
        leftStick.setFill("gray");
        leftStick.draw(win)

        return leftStick

def updateRightStick(win,rightStick,pitch,roll):
        try:
                rightStick.undraw()
        except Exception:
                pass
        
        rightStick = Line(Point(450+(roll),150+(pitch*-1)), Point(450,150))
        rightStick.setFill("gray")
	rightStick.draw(win)

	return rightStick

