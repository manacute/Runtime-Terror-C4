import pygame, sys
from Model import Model
from Button import Button

class HelpModel(Model):
    def __init__(self):
        
        super(HelpModel, self).__init__()
        pygame.display.set_caption('4-in-a-row - Instructions/Help')
        
        self.font = pygame.font.SysFont('Arial', 40)
        p = pygame.font.SysFont('Arial Light', 30)
        

        header = "4-in-a-row Instructions"
        body1 = "Welcome to 4-in-a-row! Your goal is to connect four of your"
        body2 = "checkers in a row while preventing your opponent from doing"
        body3 = "the same. First to get four in a row wins!"
        body4 = "To place your checker, select the desired column."
        body5 = "To undo/redo a move, use the controls at the top."
        
        self.instructions_header = self.font.render(header, True, pygame.Color("blue"))
        self.i1 = p.render(body1, True, pygame.Color("black"))
        self.i2 = p.render(body2, True, pygame.Color("black"))
        self.i3 = p.render(body3, True, pygame.Color("black"))
        self.i4 = p.render(body4, True, pygame.Color("black"))
        self.i5 = p.render(body5, True, pygame.Color("black"))      

        
    def draw(self, screen):
        screen.fill(pygame.Color("white"))
        self.button = Button(350, 500, 200, 100, "BACK", 
               self.font, pygame.Color("blue"), pygame.Color("red"), 
               pygame.Color("pink"), screen) 
        screen.blit(self.instructions_header, (290, 100))
        screen.blit(self.i1, (155, 200))
        screen.blit(self.i2, (140, 240))
        screen.blit(self.i3, (245, 280))
        screen.blit(self.i4, (200, 350))
        screen.blit(self.i5, (200, 390))
        self.button.draw()


    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.button.mouse_over():
                self.next_model = "menu"
                self.done = True