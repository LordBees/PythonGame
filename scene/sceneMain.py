import scene.sceneBase as Sbase
import pygame
from world import viewport,worldManager
from tileCode import tileManager



class sceneMain(Sbase.sceneBase):
    ##

    ##
    def __init__(self):
        Sbase.sceneBase.__init__(self)
        self.name = 'main'

        ##defs
        self.viewportCurrent = viewport.viewport()
        self.worldManagerCurrent = worldManager.worldManager()
        self.tileManagerCurrent = tileManager.tileManager()

        ##glue code written to load atleast a portion of the map
        ##load hack for the moment

        self.worldManagerCurrent.init()
        self.worldManagerCurrent.loadLevel('map')
        #self.world.setWorldRaw(self.worldloader.getFloors())
        for x in self.worldManagerCurrent.loader.getTilesID():
            self.tileManagerCurrent.register(int(x[0]), 'Res\\tiles\\' + x[1])
        ##end hack

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_ESCAPE:
                #    self.running = False
                if event.key == pygame.K_LEFT:
                    self.viewportCurrent.pushViewport(1,0)
                elif event.key == pygame.K_RIGHT:
                    self.viewportCurrent.pushViewport(-1,0)
                elif event.key == pygame.K_UP:
                    self.viewportCurrent.pushViewport(0, 1)
                elif event.key == pygame.K_DOWN:
                    self.viewportCurrent.pushViewport(0,-1)
                elif event.key == pygame.K_p:  ##pause event
                    pass
                elif event.key == pygame.K_PLUS:
                    pass

    def Update(self):
        pass

    def Render(self, screen):
        # The game scene is just a blank blue screen
        ##pass  ## screen.window.fill((0, 0, 255))
        screen.fill((0,0,255))
        self.renderTiles(screen)
        self.renderItems()
        self.renderScenery()
        self.renderUI()


    ##other stuff
    def renderTiles(self,screen):
        tileOffset = 32
        xOffset = 0
        yOffset = 0
        vRect = self.viewportCurrent.getviewable()
        data = self.worldManagerCurrent.getViewport(vRect[0],vRect[1],vRect[2])

        icount = 0
        for ystrip in data:  ##each x line on the y axis
            for ID in ystrip:  ##each tile in the strip
                if (int(ID) == -1):
                    pass
                else:
                    screen.blit(self.tileManagerCurrent.get(int(ID)).tex, (xOffset, yOffset))
                    ##self.window.winBlit(self.tilemanager.get(int(ID)).tex, xOffset, yOffset)
                xOffset = xOffset + tileOffset
            xOffset = 0
            yOffset = yOffset + tileOffset

    def renderItems(self):
        pass

    def renderScenery(self):
        pass

    def renderUI(self):
        pass
