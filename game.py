import pygame



class Game:

    def __init__(self):
        self.power4 = []
        self.rects = []
        self.initialize()
        self.start_game()

    def initialize(self):
        for i in range(6):
            temp = []
            rect = []
            for j in range(7):
                temp.append(0)
                rect.append(None)
            self.power4.append(temp)
            self.rects.append(rect)

    def start_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 455))
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.screen.fill((255, 255, 255))  # Remplir l'écran avec une couleur blanche
            for ligne in range(6):
                for colonne in range(7):
                    self.rects[ligne][colonne] =  pygame.draw.rect(self.screen, (0, 0, 0), (16 + colonne * 64, 32 + ligne * 64, 64, 64), 2)
            
            pygame.display.flip()

        pygame.quit()
