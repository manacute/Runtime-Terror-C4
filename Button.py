import pygame

class Button():
    def __init__(self, x, y, w, h, msg, font, text_color, color_0, color_1, outline, screen):
        '''
        Initialize a Button object.
        
        Keyword arguments:
        x -- horizontal position
        y -- vertical position
        w -- width of button
        h -- height of button
        msg -- string displayed on button
        font -- font of msg
        text_color -- color of msg
        color_0 -- initial color of button
        color_1 -- color when mouse is over button
        outline -- color of outline of box
        screen -- surface to display button on
        '''
        self.rectangle = pygame.Rect(x, y, w, h)
        self.font = font
        self.color = color_0
        self.color_0 = color_0
        self.color_1 = color_1
        self.outline_color = outline
        self.screen = screen
        self.message = self.font.render(msg, True, text_color)
        self.text_pos = (x + (w - self.message.get_rect().width) / 2, 
                         y + (h - self.message.get_rect().height) / 2)
        
    def draw(self):
        '''
        Draw the button, outline, and message.
        Switch color if mouse is over button.
        '''
        self.color = self.color_0
        if self.mouse_over():
            self.color = self.color_1
        pygame.draw.rect(self.screen, self.color, self.rectangle)
        pygame.draw.rect(self.screen, self.outline_color, self.rectangle, 2)
        self.screen.blit(self.message, self.text_pos)
        
    def mouse_over(self) -> bool:
        '''Return True iff the mouse is over the button.'''
        mouse_pos = pygame.mouse.get_pos()
        if self.rectangle.collidepoint(mouse_pos):
            return True 
        return False
    