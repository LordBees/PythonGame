## class for registering all textures to an id
import tileCode.tile, pygame


class tileManager:
    ##
    maxTiles = 256
    maxEnabled = True  ##False
    ##tiles = dict()
    tiles = []  ##maybe stack, push onto end and pop from index For, deregister then sort with priority?

    ##
    def __init__(self):
        pass

    def init(self):
        pass
        ##tiles = [G_tile.G_tile()]*self.maxTiles
        ##tiles = [tileCode.tile.tile() for i in range(self.maxTiles)]  ##this makes seperate
        ##self.tiles = tiles

    def set_maxTiles(self, maxEnabled, maxTiles):
        self.maxEnabled = maxEnabled
        self.maxTiles = maxTiles

    def register(self, tileID, pathToFile):
        ##registers a tile to the system with a given id
        ##currently creates based on file
        for x in self.tiles:
            if (x.ID == tileID):##can put in check for name later
                return -1 ## cannot assign data
        tile = tileCode.tile.tile()
        Tex = pygame.image.load(pathToFile)
        ## the filepath is split then get file name and split off the extension as the name
        name = pathToFile.split('\\')[len(pathToFile.split('\\')) - 1].split('.')[0]

        tile.config(name, Tex)
        tile.ID = tileID
        tile.loaded = True

        ##Tex = None
        ##Tex = pygame.image.load(pathToFile)
        ##self.tiles.append(Tex)
        ##check if id already there
        self.tiles.append(tile)
        return tileID##return the id as success

    def deregister(self,tileID):
        for x in range(len(self.tiles)):
            if(self.tiles[x].ID == tileID):
                self.tiles.pop(x)
                return 1
        return 0

    def get(self, tileID):
        ##returns tile data
        for x in self.tiles:
            if(x.ID == tileID):
                return x#self.tiles[tileID]
        return tileCode.tile.tile()##return a blank one if no found

    def get_freeID(self):  ##returns available id if none found returns -1
        #for x in self.tiles:
        #    if (x.loaded == False):
        #        return x
        if (len(self.tiles) > self.maxTiles):
            ia=[]#intarray
            i=0
            for xID in self.tiles:
               ia.append(xID.ID)
            while(i in ia):##iterate through ids in array  until an id number not found in array
                i += 1
            return i
        return -1
