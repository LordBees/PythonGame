## pygame window
import pygame

class window:
    ##
    ##window = None
    x = 300  ##100
    y = 300  ##100
    mode = None
    title = 'Default'
    backFill = (0, 0, 0)

    ##
    def __init__(self):
        pygame.display.init()
        self.screen = pygame.display.set_mode([self.x, self.y])

    ##
    def init(self):
        ##win = pygame.display
        ##win.set_mode([self.x,self.y])##would have flags=self.mode
        ##win.set_caption(self.title)
        ##self.updateDisp()

        ##self.window = pygame.display()##win
        ##self.updateDispSetting()
        ##self.window.init()

        self.screen = pygame.display.set_mode([self.x, self.y])



    def updateDispSetting(self):
        self.screen.set_mode([self.x, self.y])  ##would have flags=self.mode
        self.set_caption(self.title)

    def set_dimensions(self, x, y):
        self.x = x
        self.y = y

    def winBlit(self, img, x, y):  ##blit to screen
        self.screen.blit(img, (x, y))

    def updateDisp(self):
        pygame.display.flip()
        self.screen.fill(self.backFill)

    def set_screenMode(self, mode):
        '''
        add these together to make mode
        pygame.FULLSCREEN    create a fullscreen display
        pygame.DOUBLEBUF     recommended for HWSURFACE or OPENGL
        pygame.HWSURFACE     hardware accelerated, only in FULLSCREEN
        pygame.OPENGL        create an OpenGL-renderable display
        pygame.RESIZABLE     display window should be sizeable
        pygame.NOFRAME       display window will have no border or controls
        '''
        self.mode = mode

    def set_title(self, title):
        self.title = title

    def set_backFill(self, rgbtuple):
        self.backFill = rgbtuple

    def qDisp(self):
        ##if (self.window.get_init()):
        pygame.display.quit()

    def setupQ(self, x, y, title,
               backFill):  ##def setupQ(self,x = self.x, y = self.y, title = self.title,backFill  = self.backFill):
        self.set_dimensions(int(x), int(y))
        self.set_title(title)
        self.set_backFill(backFill)