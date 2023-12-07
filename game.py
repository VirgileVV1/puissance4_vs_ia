import pygame



class Game:

    def __init__(self):
        self.LINES = 6
        self.COLUMN = 7
        self.power4 = []
        self.rects = []
        self.initialize()
        self.start_game()

    def initialize(self):
        for i in range(self.LINES):
            temp = []
            rect = []
            for j in range(self.COLUMN):
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
            for ligne in range(self.LINES):
                for colonne in range(self.COLUMN):
                    self.rects[ligne][colonne] =  pygame.draw.rect(self.screen, (0, 0, 0), (16 + colonne * 64, 32 + ligne * 64, 64, 64), 2)
            
            pygame.display.flip()

        pygame.quit()
