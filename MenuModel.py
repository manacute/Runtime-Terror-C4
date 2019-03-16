import pygame, sys
from Model import Model
from Button import Button

class MenuModel(Model):
    def __init__(self):
        super(MenuModel, self).__init__()
        pygame.display.set_caption('4-in-a-row Menu')
        
        self.font = pygame.font.SysFont('Arial', 40)
        
        
    def draw(self, screen):

        screen.fill(pygame.Color("white"))

        #Creates the 3 interactive buttons
        self.start_button = Button(350, 100, 200, 100, "START", 
                       self.font, pygame.Color("blue"), pygame.Color("red"), 
                       pygame.Color("pink"), screen)
        self.help_button = Button(350, 300, 200, 100, "HELP", 
                       self.font, pygame.Color("blue"), pygame.Color("red"), 
                       pygame.Color("pink"), screen)
        self.quit_button = Button(350, 500, 200, 100, "QUIT", 
                       self.font, pygame.Color("blue"), pygame.Color("red"), 
                       pygame.Color("pink"), screen)

        self.buttons.append(self.start_button)
        self.buttons.append(self.help_button)
        self.buttons.append(self.quit_button)
        
        for button in self.buttons:
            button.draw()

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.mouse_over():
                self.next_model = "board"
                self.done = True
            elif self.help_button.mouse_over():
                self.next_model = "help"
                self.done = True
            elif self.quit_button.mouse_over():
                self.quit = True
