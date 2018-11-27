#view conditions for viewing the world
#

class viewport:
    ##
    x=25#5##10
    y=25##5##10
    z=0
    currx=0
    curry=0
    currz=0
    ##

    def __init__(self):
        pass

    def getviewable(self):##returns a tuple with the current z level and the 2 corners of the viewport
        return(self.z,(self.currx,self.curry),(self.currx+self.x,self.curry+self.y))

    def updateViewport(self,x,y,z):
        self.currx = x
        self.curry = y
        self.currz = z

    def moveViewport(self,x,y):
        self.currx = x
        self.curry = y

    def pushViewport(self,x,y):
        self.currx += x
        self.curry += y

    def SwapFloorViewport(self,z):
        self.currz = z

    def pushFloorViewport(self,z):
        self.currz += z

    def getCurrViewportPos(self):
        return (self.currx,self.curry,self.currz)

    def setViewportSize(self,x,y):
        self.x = x
        self.y = y
