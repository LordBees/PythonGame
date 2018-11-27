import scene.sceneBase as Sbase


class sceneTest(Sbase.sceneBase):
    ##

    ##
    def __init__(self):
        Sbase.sceneBase.__init__(self)
        self.name = 'test'

    def ProcessInput(self, events, pressed_keys):
        print("testinp")

    def Update(self):
        print("testupd")

    def Render(self, screen):
        print("testren")