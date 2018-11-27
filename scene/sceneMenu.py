##import ren.S_sceneMain as S_sceneMain
import pygame
##3p imports

##importing ui elements
##from UI_buttonMain import UI_buttonMain

import scene.sceneBase as Sbase


class sceneMenu(Sbase.sceneBase):
    ##
    UI_PARTS = []

    ##
    def __init__(self):
        Sbase.sceneBase.__init__(self)
        self.name = 'menu'
        self.setupUI()

    ##code

    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter
                ##self.SwitchToScene(S_sceneMain())
                self.nextID = 3
                print('main')

            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                ##self.UI_PARTS[0].x = self.UI_PARTS[0].x + 50
                print("E")

    def Update(self):
        pass  ##if

    def Render(self, screen):
        ##screen = screen.window
        # For the sake of brevity, the title scene is a blank red screen
        screen.fill((255, 0, 0))


        ##draw buttons
        for btn in self.UI_PARTS:
            btn.render(screen)
            ##print('www')
        ##pass

    def setupUI(self):
        self.populateButtons()

    def populateButtons(self):
        ##button = UI_buttonMain()
        ##button.setup(0, (50, 100), (150, 50), 'test')
        ##button.init()

        ## button = UI_buttonMain()
        ## button.setup(0,(200,50),(50,50),'test')
        ## button.init()

        ##self.UI_PARTS.append(button)
        pass

