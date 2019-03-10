import pygame, sys
from Model import Model

class MenuModel(Model):
    def __init__(self):
        super(MenuModel, self).__init__()
        pygame.display.set_caption('4-in-a-row Menu')
        
        self.font = pygame.font.SysFont('Arial', 40)
        
        
    def draw(self, screen):


        screen.fill(pygame.Color("white"))

        #Creates the 3 interactive buttons
        self.start_button = pygame.Rect(350, 100, 200, 100)
        self.help_button = pygame.Rect(350, 300, 200, 100)
        self.quit_button = pygame.Rect(350, 500, 200, 100)

        start_text = self.font.render("START", True, pygame.Color("blue"))
        help_text = self.font.render("HELP", True, pygame.Color("blue"))
        quit_text = self.font.render("QUIT", True, pygame.Color("blue"))

        pygame.draw.rect(screen, pygame.Color("red"), self.start_button)
        pygame.draw.rect(screen, pygame.Color("red"), self.help_button)
        pygame.draw.rect(screen, pygame.Color("red"), self.quit_button)

        #Draws the text after drawing the rectangle so you can see the text
        screen.blit(start_text, (405, 135))
        screen.blit(help_text, (405, 335))
        screen.blit(quit_text, (405, 535))


    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = event.pos
            if self.start_button.collidepoint(mouse_position):
                self.next_model = "board"
                self.done = True
            elif self.help_button.collidepoint(mouse_position):
                self.next_model = "help"
                self.done = True
            elif self.quit_button.collidepoint(mouse_position):
                self.quit = True
