import pygame

CELL_SIZE = 64

class Game:

    def __init__(self):
        self.LINES = 6
        self.COLUMN = 7
        self.round = 0
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

    def add_piece(self, index_column_to_add):
        index_row = None
        for i in range(len(self.rects)-1, -1, -1):
            if (self.power4[i][index_column_to_add] == 0):
                index_row = i
                break
        if index_row is not None:
            self.power4[index_row][index_column_to_add] = 1
            return True
        return False


    def handle_mouse_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("right clic", event.pos)
                for row in self.rects:
                    for col, rect in enumerate(row):
                        if (rect.collidepoint(event.pos)):
                            if self.add_piece(col):
                                self.round += 1

            if event.button == 3:
                print("left clic")

    def start_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 455))
        run = True

        old_round = self.round

        while run:            
            self.screen.fill((255, 255, 255))  # Remplir l'écran avec une couleur blanche

            if old_round != self.round:
                old_round = self.round
                print("tour passe !")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                self.handle_mouse_event(event)

            for ligne in range(self.LINES):
                for colonne in range(self.COLUMN):
                    if self.power4[ligne][colonne] == 0:
                        self.rects[ligne][colonne] =  pygame.draw.rect(self.screen, (0, 0, 0), (16 + colonne * CELL_SIZE, 32 + ligne * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
                    else:
                        self.rects[ligne][colonne] =  pygame.draw.rect(self.screen, (255, 0, 0), (16 + colonne * CELL_SIZE, 32 + ligne * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
            
            pygame.display.flip()

        pygame.quit()
