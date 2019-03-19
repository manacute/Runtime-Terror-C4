import pygame, sys
from Move import Move
from BoardModel import BoardModel
from MoveController import MoveController
from HelpModel import HelpModel
from MenuModel import MenuModel
from Model import Model

'''
CSC290 Group Project
C4: Four In A Row
University of Toronto Mississauga
'''

class Game():
    def __init__(self, display, screens, model_name):
        self.playing = True
        self.fps = 60
        self.screen = screen
        self.screens = screens
        self.model_name = model_name
        self.model = screens[self.model_name]
        self.clock = pygame.time.Clock()
        self.controller = MoveController(screens["board"])
        
    def event_loop(self):
        for event in pygame.event.get():
            if self.model_name == "board":
                self.model.get_event(event, self.model_name, self.controller)
            else:
                self.model.get_event(event)
            
    def draw(self):
        self.model.draw(self.screen)

    def update(self, frame_time):
        if self.model.quit:
            self.playing = False
        elif self.model.done:
            self.change_screen()
        self.model.update(frame_time)

    def change_screen(self):
        self.model.done = False
        self.model_name = self.model.next_model
        self.model = screens[self.model_name]

    def play(self):
        while self.playing:
            frame_time = self.clock.tick(self.fps)
            self.event_loop()
            self.update(frame_time)
            self.draw()
            pygame.display.update()
            


if __name__ == '__main__':
    pygame.init()   
    pygame.font.init()  
    screen = pygame.display.set_mode((900, 700))

    screens = {"menu": MenuModel(), "help": HelpModel(), "board": BoardModel()}
    game = Game(screen, screens, "menu")
    game.play()
    
    pygame.quit()
    sys.exit()
