import copy
#from G_defines import DEBUG
DEBUG= True

class world:
    ##
    ##world dimensions
    worldX = 5
    worldY = 5
    worldZ = 2  ## worldLayers = 1

    ##world options
    worldSpriteLayer = 1  ##how many layers of sprites per layer
    worldPlayerLayer = 1

    ##world creation defines
    world = []

    ##

    def __init__(self):
        pass

    def internal_WorldInit(self):
        ##line  = [0]    *self.worldX
        ##layer = [list(line)] *self.worldY ## each layer
        ##world = [list(layer)]*self.worldZ
        xline = [0] * self.worldX
        yline = [0] * self.worldY
        zline = [0] * self.worldZ

        for yl in range(0, self.worldY):
            yline[yl] = copy.deepcopy(xline)
        for zl in range(0, self.worldZ):
            zline[zl] = copy.deepcopy(yline)
        self.world = zline

    def set_XYZ(self, x, y, z):  ##set size of worlds
        self.worldX = x
        self.worldY = y
        self.worldZ = z

    def set_XYZ_Tuple(self, xyz):
        self.set_XYZ(int(xyz[0]), int(xyz[1]), int(xyz[1]))

    def preInitialise(self):
        ##sets up world data for population
        self.internal_WorldInit()

    def setTile(self, x, y, z, tileID):
        ##sets tileid of x y
        self.world[z][y][x] = tileID

    def setTileXStrip(self, z, y, tileIDs):
        x = 0
        ##check if same length or shorter if not return
        for TileID in tileIDs:
            self.world[z][y][x] = TileID
            x = x + 1

    def setWorldRaw(self, rawdata):
        self.world = rawdata

    def getTile(self, x, y, z):  ##-1 catches coords as 5 len is actually[edit now >= instead]
        if ((x >= self.worldX) or (x < 0)):
            return -1
        if ((y >= self.worldY) or (y < 0)):
            return -1
        if ((z >= self.worldZ) or (z < 0)):
            return -1
        if DEBUG:
            print(x, y, z)
        return self.world[z][y][x]

    def getRect(self, x, y, z, lenX, lenY):  ##wasgetSquare
        xline = [0] * lenX
        yline = [0] * lenY
        xp = 0  ##pos in loop for data
        yp = 0
        ##zline = [0]*self.worldZ

        for yl in range(0, lenY):
            yline[yl] = copy.deepcopy(xline)
            ##optimize me

        for yl in range(y, y + lenY):
            for xl in range(x, x + lenX):
                yline[yp][xp] = self.getTile(xl, yl, z)  ##self.world[z][y+yp][x+xp]
                ##print(self.getTile(x+xl,y+yl,z),'['+str(x+xp)+'|'+str(y+yp)+']',' , ',yline)
                if DEBUG:
                    print('got: ' + str(self.getTile(xl, yl, z)) + ' x/y ' + str(xl) + '|' + str(yl)
                                                                            + '' + ' , ' + str(yline))
                xp = xp + 1
            yp = yp + 1
            xp = 0
        return yline

    def getSquare(self, x, y, z, iLen):
        return self.getRect(x, y, z, iLen, iLen)

    def getViewport(self, z, xy1t, xy2t):  ##z : xy start tuple : xy end tuple
        xLen = xy2t[0] - xy1t[0]
        yLen = xy2t[1] - xy1t[1]
        ##xStrip = [0]*xLen
        data = self.getRect(xy1t[0], xy1t[1], z, xLen, yLen)
        return data

    def dbg_printfloor(self, z):
        temp = self.world[z]
        for x in temp:
            for y in x:
                print(str(y) + ' ', end='')

            print('')
        print('end')

