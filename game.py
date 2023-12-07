import pygame



class Game:

    def __init__(self):
        self.power4 = []
        self.initialize()
        self.start_game()

    def initialize(self):
        for i in range(6):
            temp = []
            for j in range(7):
                temp.append(0)
            self.power4.append(temp)

    def start_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 455))
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.screen.fill((255, 255, 255))  # Remplir l'écran avec une couleur blanche
            pygame.display.flip()

        pygame.quit()
