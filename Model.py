import pygame

class Model():
    '''
    A parent class used for the screens of the game,
    which is used by Game to handle different game states.
    '''
    def __init__(self):
        self.done = False
        self.quit = False
        self.next_model = None
        self.buttons = []
        self.text_color = pygame.Color("black")
        self.button_color0 = pygame.Color("white")
        self.button_color1 = pygame.Color("grey")
        self.button_outline = pygame.Color("black")
        
    def get_event(self, event):
        '''Receive and handle events.'''
        pass
    
    def draw(self, display):
        '''Draw onto the screen.'''
        pass
    