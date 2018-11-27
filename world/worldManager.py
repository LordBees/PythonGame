##manager for the world ,handles the loading of world data and setting up for the
##import G_world, G_worldLoader, copy
from world import world,worldLoader

class worldManager:
    ##
    ##world = None  ##G_world.G_world
    ##loader = None  ##G_worldLoader.G_worldLoader

    ##
    def __init__(self):
        self.world = world.world()##G_world.G_world()
        self.loader = worldLoader.worldLoader()##G_worldLoader.G_worldLoader()

    def init(self):
        self.world.preInitialise()
        ##self.loader.init()

    def loadLevel(self, lvl):##loads a level by name
        ##load level data to loader object(replace with mapmanger and pre loading)
        self.loader.loadLevel(lvl)
        ##set world up and reinitialise tables
        self.world.set_XYZ_Tuple(self.loader.getCFG_XYZ())  ##check when viewport larger tne map size
        self.world.preInitialise()##quick hack to get working
        ##set raw world data into the data structure
        self.world.setWorldRaw(self.loader.getFloors())
        wConfig = []
        wDat = []

    def getSquare(self):
        pass

    def getRect(self):
        pass

    def getViewport(self, z, xy1t, xy2t):  ##z : xy start tuple : xy end tuple
        #xLen = xy2t[0] - xy1t[0]
        #yLen = xy2t[1] - xy1t[1]
        ###xStrip = [0]*xLen
        #data = self.world.getRect(xy1t[0], xy1t[1], z, xLen, yLen)
        #return data
        return self.world.getViewport(z,xy1t,xy2t)##returns tile ids in array?
