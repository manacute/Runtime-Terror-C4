import pygame

class Button():
    def __init__(self, x, y, w, h, text, font, color_text, color_0, color_1, screen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rectangle = pygame.Rect(x, y, w, h)
        self.text = text
        self.font = font
        self.color_text = color_text
        self.color = color_0
        self.color_0 = color_0
        self.color_1 = color_1
        self.screen = screen
        self.message = self.font.render(text, True, color_text)
        
    def draw(self):
        self.color = self.color_0
        if self.mouse_over():
            self.color = self.color_1
        pygame.draw.rect(self.screen, self.color, self.rectangle)
        self.screen.blit(self.message, (self.x + self.w/4, self.y + self.h/4))
        
    def mouse_over(self) -> bool:
        mouse_pos = pygame.mouse.get_pos()
        if self.rectangle.collidepoint(mouse_pos):
            return True 
        return False
    