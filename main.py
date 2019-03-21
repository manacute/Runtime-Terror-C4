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
    '''
    Base game instance, which handles game states and transitions
    between the different game screens. The play() method serves
    as the main gameplay loop. 
    Structure of state machine inspired by iminurnamez:
    https://gist.github.com/iminurnamez/8d51f5b40032f106a847
    Licensed under CC0 1.0 Universal.
    '''
    def __init__(self, display, screens, model_name):
        '''
        Initialize the Game object.
        
        Keyword arguments:
        display -- the display Surface used to draw the game
        screens -- a dict mapping names of models to their Model objects
        model_name -- the name of the model of the first game screen
        '''
        self.playing = True
        self.fps = 60
        self.screen = display
        self.screens = screens
        self.model_name = model_name
        self.model = screens[self.model_name]
        self.clock = pygame.time.Clock()
        self.controller = MoveController(screens["board"])
        
    def event_loop(self):
        '''Pass pygame events to current model to handle current game state.'''
        for event in pygame.event.get():
            if self.model_name == "board":
                self.model.get_event(event, self.controller)
            else:
                self.model.get_event(event)
            
    def draw(self):
        '''Pass screen to current model to draw current game state.'''
        self.model.draw(self.screen)

    def update(self, frame_time):
        '''
        Update current model if there is a change, it
        signals for a change in models, or if there is
        a game quit event.
        
        Keyword arguments:
        frame_time -- milliseconds since last frame
        '''
        if self.model.quit:
            self.playing = False
        elif self.model.done:
            self.change_screen()

    def change_screen(self):
        '''Change the model being used according to next_model.'''
        self.model.done = False
        self.model_name = self.model.next_model
        self.model = screens[self.model_name]

    def play(self):
        '''The main game loop. Halts upon game exit.'''
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
