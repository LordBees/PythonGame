##1p
##3p
import pygame
##mine
from engine import configManager, Window
import scene.sceneManager

class gameMain:
    ##
    fps = 60
    ##

    def __init__(self):
        self.gameWindow = Window.window()
        self.engineCFG = configManager.configManager()
        self.clock = pygame.time.Clock()
        self.sceneManager = scene.sceneManager.sceneManager()
        self.gameWorld = None

    def run(self):
        print("running game")
        self.gameSetup()
        self.gameRun()
        self.gameCleanup()
        print("Quitting...")

    def gameSetup(self):
        print("|setup")
        ##
        self.loadWindowCFG()##window stuff
        self.setupWindow()  ##

        self.setupMisc()##misc setup
        ##sound setup

        ##
        print("|¬\n")

    def gameRun(self):##no textures being loaded see the old main and figure that bit out later
        print("|run")
        ##
        self.gameLoop()
        ##
        print("|¬\n")

    def gameCleanup(self):
        print("|cleanup")
        ##
        self.cleanupWindow()
        self.cleanupPygame()
        self.cleanupSceneManager()
        ##
        print("|¬\n")

    ##methods for actual setup (all internal)

    def loadWindowCFG(self):
        print("|>loading engine cfg")
        self.engineCFG.load('engineMain.cfg')

    def setupWindow(self):
        print("|>setting up window")
        ##self.gameWindow = Window.window()
        ##self.engineCFG.getValue('window','x')
        self.gameWindow.setupQ(self.engineCFG.getValue('win','x'),
                               self.engineCFG.getValue('win','y'),
                               self.engineCFG.getValue('win','title'),

                               (int(self.engineCFG.getValue('win','bR')),
                                int(self.engineCFG.getValue('win','bG')),
                                int(self.engineCFG.getValue('win','bB'))))
        self.gameWindow.init()

    def setupMisc(self):
        print("|>setting up clock")
        self.fps = self.engineCFG.getValue('game','fps')

        print("|>setting up sceneManager",end='')
        ##self.sceneManager.ID = int(self.engineCFG.getValue('game','startingscene'))
        self.sceneManager.setScene(int(self.engineCFG.getValue('game','startingscene')))
        print(" ->  starting scene ID:"+str(self.sceneManager.scene))





    ##cleanup stuff
    def cleanupWindow(self):
        print("|>quitting pygame window")
        self.gameWindow.qDisp()

    def cleanupPygame(self):
        print('|>quitting pygame')
        pygame.quit()

    def cleanupSceneManager(self):
        print("|>cleaning up scene manager")
        self.sceneManager.cleanup()

    ##game stuff
    def gameLoop(self):
        print("|>game loop")

        ##
        while True:
            pressed_keys = pygame.key.get_pressed()

            # Event filtering
            filtered_events = []
            for event in pygame.event.get():
                quit_attempt = False
                if event.type == pygame.QUIT:
                    quit_attempt = True
                elif event.type == pygame.KEYDOWN:  ##hardcoded
                    alt_pressed = pressed_keys[pygame.K_LALT] or \
                                  pressed_keys[pygame.K_RALT]
                    if event.key == pygame.K_ESCAPE:
                        quit_attempt = True
                    elif event.key == pygame.K_F4 and alt_pressed:
                        quit_attempt = True

                if quit_attempt:
                    ##self.scene.Terminate()
                    ##self.window.qDisp()
                    return 'Qstate'
                    ##pygame.quit()

                else:
                    filtered_events.append(event)
            ## end event filtering
            ##do loop
            #self.main_processInput(filtered_events, pressed_keys)
            #self.main_update()
            #self.main_render()
            self.sceneManager.doProcessInput(filtered_events, pressed_keys)
            self.sceneManager.doUpdate()
            self.sceneManager.doRender(self.gameWindow.screen)
            ##self.update()
            ##self.draw2screen()

            ##update scene
            ##self.scene = self.scene.next
            self.sceneManager.doNextScene()

            ## finally flip and tick
            self.clock.tick(float(self.fps))
            self.gameWindow.updateDisp()



    


