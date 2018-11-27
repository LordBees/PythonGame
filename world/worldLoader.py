##gets world data from file
import copy,configparser

class worldLoader:
    ##
    hasloaded = False
    zPref = '_Z_'
    tPref = '_table'
    mapPath = 'Res\\map\\Map01\\'
    levelsID = []
    floors = []
    #CFG = configparser.ConfigParser()
    ##

    def __init__(self):
        self.CFG = configparser.ConfigParser()

    def loadworld(self):
        pass

    def cleardata(self):
        pass

    def loadLevel(self,levelname):
        dataTemp = []
        ##get cfg variables
        self.CFG = configparser.ConfigParser()
        print('reading '+levelname+'.cfg')
        self.CFG.read(self.mapPath+levelname+'.cfg')
        print('got\n',self.CFG.sections())

        ##get index table
        dataTemp = self.readFile(self.pathTo(levelname+self.tPref+'.txt'))
        for x in range(0,len(dataTemp)):
           dataTemp[x] = dataTemp[x].strip('\n')
           dataTemp[x] = dataTemp[x].split(',')
        self.levelsID = copy.deepcopy(dataTemp)

        ##get z levels and append them
        # only 1 floor atm
        ##print(self.CFG['CFG']['z'])
        for x in range(0,int(self.CFG['cfg']['z'])):
            dataTemp = self.readFile(self.pathTo(levelname+self.zPref+str(x)+'.txt'))
            for x in range(0,len(dataTemp)):
                dataTemp[x] = dataTemp[x].strip('\n')
                dataTemp[x] = dataTemp[x].split(',')
            self.floors.append(copy.deepcopy(dataTemp))

        ##dataTemp = self.readFile(self.pathTo(levelname+self.zPref+'0.txt'))
        ##for x in range(0,len(dataTemp)):
        ##    dataTemp[x] = dataTemp[x].strip('\n')
        ##    dataTemp[x] = dataTemp[x].split(',')
        ##self.floors.append(copy.deepcopy(dataTemp))



    def readFile(self,fn):
        f = open(fn,'r')
        dat = f.readlines()
        f.close()
        return dat

    def pathTo(self,fn):
        return self.mapPath+fn

    def getTilesID(self): ##def getLevelsID(self):
        return self.levelsID
    def getFloors(self):
        return self.floors
    def getCFG(self):
        return self.CFG
    def getCFG_XYZ(self):
        return (self.CFG['cfg']['x'],self.CFG['cfg']['y'],self.CFG['cfg']['z'])