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
        ##tiles = [G_tile.G_tile()]*self.maxTiles
        tiles = [tileCode.tile.tile() for i in range(self.maxTiles)]  ##this makes seperate
        self.tiles = tiles

    def set_maxTiles(self,maxEnabled, maxTiles):
        self.maxEnabled = maxEnabled
        self.maxTiles = maxTiles

    def register(self, tileID, pathToFile):
        ##registers a tile to the system with a given id
        ##currently creates based on file
        tile = tileCode.tile.tile()
        Tex = pygame.image.load(pathToFile)
        ## the filepath is split then get file name and split off the extension
        name = pathToFile.split('\\')[len(pathToFile.split('\\')) - 1].split('.')[0]


        tile.config(name, Tex)
        tile.ID = tileID
        tile.loaded = True

        ##Tex = None
        ##Tex = pygame.image.load(pathToFile)
        ##self.tiles.append(Tex)
        ##check if id already there

        self.tiles[tileID] = tile

    def get(self, tileID):
        ##returns tile data
        return self.tiles[tileID]

    def get_freeID(self):  ##returns available id if none found returns -1
        for x in self.tiles:
            if x.loaded == False:
                return x
        return -1
