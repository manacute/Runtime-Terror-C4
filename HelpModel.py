import pygame, sys

class HelpModel:
    def __init__(self):
        h1 = pygame.font.SysFont('Arial', 40)
        p = pygame.font.SysFont('Arial Light', 30)

        screen = pygame.display.set_mode((900, 700))
        pygame.display.set_caption('4-in-a-row - Instructions/Help')

        # --- Variables --- #
        BLUE = (0, 0, 255)
        RED = (255, 0, 0)
        WHITE = (255, 255, 255)
        YELLOW = (255, 255, 0)
        BLACK = (0,0,0)


        header = "4-in-a-row Instructions"
        body1 = "Welcome to 4-in-a-row! Your goal is to connect four of your"
        body2 = "checkers in a row while preventing your opponent from doing"
        body3 = "the same. First to get four in a row wins!"
        body4 = "To place your checker, select the desired column."
        body5 = "To undo/redo a move, use the controls at the top."

        back_text = h1.render("BACK", True, BLUE)
        instructions_header = h1.render(header, True, BLUE)
        i1 = p.render(body1, True, BLACK)
        i2 = p.render(body2, True, BLACK)
        i3 = p.render(body3, True, BLACK)
        i4 = p.render(body4, True, BLACK)
        i5 = p.render(body5, True, BLACK)
        back_button = pygame.Rect(350, 500, 200, 100)
        help = True
        # --- Placing everything on the screen --- #
        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, back_button)
        screen.blit(instructions_header, (290, 100))
        screen.blit(i1, (155, 200))
        screen.blit(i2, (140, 240))
        screen.blit(i3, (245, 280))
        screen.blit(i4, (200, 350))
        screen.blit(i5, (200, 390))
        screen.blit(back_text, (405, 540))

        pygame.display.update()

        # --- Page functionality --- #

    def help_menu(self):
        back_button = pygame.Rect(350, 500, 200, 100)
        help = True
        while help:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_position = event.pos
                    if back_button.collidepoint(mouse_position):
                        return("menu")
                        help = False