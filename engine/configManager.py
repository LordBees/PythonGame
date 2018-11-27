import configparser,os


class configManager:##loads configuration data for a given file
    ##
    CFG_PATH = 'res\\cfg\\'
    fileName = ''
    CFG = configparser.ConfigParser()
    loaded = False
    ##

    def __init__(self):
        pass

    def load(self, fn):##cfg to load
        if not (os.path.isfile(self.CFG_PATH+fn)):
            print("|file doesnt exist!["+str(self.CFG_PATH+fn)+"]")
            return 1
        self.fileName = fn
        print("|loading CFG: "+str(fn), end='')
        self.CFG.read(self.CFG_PATH+fn)
        print(" .. Done")
        self.loaded = True
        return 0

    def save(self):##save loaded
        if not self.loaded:
            return 0

        with open(self.CFG_PATH+str(self.fileName), 'w') as configFile:
            self.CFG.write(configFile)
        return 1

    def close(self):
        self.CFG = configparser.ConfigParser()
        self.loaded = False

    def getValue(self, section, key):##get value from dict
        return self.CFG[section][key]

    def getSections(self):
        return self.CFG.sections()

