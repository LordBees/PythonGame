##tile class
class tile:
    ##
    name = ''
    ID = -1
    tex = None
    loaded = False

    ##
    def __init__(self):
        pass

    def addTex(self, tex):
        self.tex = tex

    def addName(self, name):
        self.name = name

    def setLoaded(self, loaded):
        self.loaded = loaded

    def setID(self, ID):
        self.ID = ID

    def config(self, name, tex):  ##basic config
        self.addTex(tex)
        self.addName(name)
        self.loaded = True

