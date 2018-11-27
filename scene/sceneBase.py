class sceneBase(object):
    ##
    name = 'base name'
    ID = 0
    nextID = 0

    ##
    def __init__(self):
        self.next = self

    def ProcessInput(self, events, pressed_keys):
        print("uh-oh, you didn't override this in the child class")

    def Update(self):
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):##moved viewport to inside scene and world
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):
        self.next = next_scene

    def getNextScene(self):
        return self.nextID

    def Terminate(self):
        self.SwitchToScene(None)
