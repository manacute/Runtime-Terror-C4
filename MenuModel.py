import pygame, sys
from Model import Model
from Button import Button

class MenuModel(Model):
    def __init__(self):
        '''
        Creates a menu model object.
        '''
        super(MenuModel, self).__init__()
        pygame.display.set_caption('4-in-a-row Menu')

        self.font = pygame.font.SysFont('Arial', 40)


    def draw(self, screen):
        '''
        Draws a menu model on the game.
        '''
        screen.fill(pygame.Color("white"))

        title_text = self.font.render("Four-In-A-Row", True, pygame.Color("black"))
        screen.blit(title_text, (352, 30))

        #Creates the 3 interactive buttons
        self.start_button = Button(350, 100, 200, 100, "START",
                       self.font, self.text_color, self.button_color0,
                       self.button_color1, self.button_outline, screen)
        self.help_button = Button(350, 300, 200, 100, "HELP",
                       self.font, self.text_color, self.button_color0,
                       self.button_color1, self.button_outline, screen)
        self.quit_button = Button(350, 500, 200, 100, "QUIT",
                       self.font, self.text_color, self.button_color0,
                       self.button_color1, self.button_outline, screen)

        self.buttons.append(self.start_button)
        self.buttons.append(self.help_button)
        self.buttons.append(self.quit_button)

        for button in self.buttons:
            button.draw()

    def get_event(self, event):
        '''
        Gets user inputted event by detecting which button has been clicked
        by the user.
        '''
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
