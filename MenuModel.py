import pygame, sys

class MenuModel:
    def __init__(self):

        pygame.init()
        pygame.font.init()
        my_font = pygame.font.SysFont('Arial', 40)

        #Keeping consistent display size with game
        screen = pygame.display.set_mode((900, 700))
        pygame.display.set_caption('4-in-a-row Menu')

        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        WHITE = (255, 255, 255)
        YELLOW = (255, 255, 0)

        screen.fill(WHITE)

        #Creates the 3 interactive buttons
        start_button = pygame.Rect(350, 100, 200, 100)
        help_button = pygame.Rect(350, 300, 200, 100)
        quit_button = pygame.Rect(350, 500, 200, 100)


        start_text = my_font.render("START", True, BLUE)
        help_text = my_font.render("HELP", True, BLUE)
        quit_text = my_font.render("QUIT", True, BLUE)


        pygame.draw.rect(screen, RED, start_button)
        pygame.draw.rect(screen, RED, help_button)
        pygame.draw.rect(screen, RED, quit_button)

        #Draws the text after drawing the rectangle so you can see the text
        screen.blit(start_text, (405, 135))
        screen.blit(help_text, (405, 335))
        screen.blit(quit_text, (405, 535))

        pygame.display.update()
        
    
    def select_game_type(self) -> str:
        flag = True
        start_button = pygame.Rect(350, 100, 200, 100)
        help_button = pygame.Rect(350, 300, 200, 100)
        quit_button = pygame.Rect(350, 500, 200, 100)

        #Runs until a button has been clicked or the program has been closed.
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = event.pos
                    if start_button.collidepoint(mouse_position):
                        return("start")
                        flag = False

                    elif help_button.collidepoint(mouse_position):
                        return("help")
                        flag = False

                    elif quit_button.collidepoint(mouse_position):
                        pygame.quit()
                        sys.exit()
