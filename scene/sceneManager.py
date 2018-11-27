from scene import sceneBase,sceneTest,sceneMenu,sceneMain ##sceneBase,sceneMenu,sceneMain


class sceneManager:
    ##
    gameScenes = [sceneBase.sceneBase()]
    scene = 0
    ##
    def __init__(self):
        ##initialise the scenes to the manager
        #self.addScene(sceneMenu.sceneMenu())
        #self.addScene(sceneMain.sceneMain())
        self.addScene(sceneTest.sceneTest())
        self.addScene(sceneMenu.sceneMenu())
        self.addScene(sceneMain.sceneMain())

        for x in range(len(self.gameScenes)):
            self.gameScenes[x].ID = x
            self.gameScenes[x].nextID=x

    def addScene(self,sc):
        self.gameScenes.append(sc)

    def delScene(self,scID):
        for x in range(len(self.gameScenes)):
            if (self.gameScenes[x].ID == scID):
                self.gameScenes.pop(x)

    def cleanup(self):
        pass

    def setScene(self,scene):
        self.scene = scene

    def doProcessInput(self,events,pressed_keys):
        self.gameScenes[self.scene].ProcessInput(events,pressed_keys)

    def doUpdate(self):
        self.gameScenes[self.scene].Update()

    def doRender(self,screen):
        self.gameScenes[self.scene].Render(screen)

    def doNextScene(self):
        self.scene = self.gameScenes[self.scene].getNextScene()
