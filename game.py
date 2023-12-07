import pygame
from timer import Timer

CELL_SIZE = 64
OFFSET_TOP = 48
OFFSET_LEFT = 32
PIECE_SIZE = 25 # x2

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

    def add_piece(self, index_column_to_add, value):
        index_row = None
        for i in range(len(self.rects)-1, -1, -1):
            if (self.power4[i][index_column_to_add] == 0):
                index_row = i
                break
        if index_row is not None:
            self.power4[index_row][index_column_to_add] = value
            return True
        return False


    def handle_mouse_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:  # il y a un clique
            if event.button == 1:               # clic gauche 
                if (self.round % 2) == 0:       # c'est notre tour
                    for row in self.rects:
                        for col, rect in enumerate(row):
                            if (rect.collidepoint(event.pos)):
                                if self.add_piece(col, 1):
                                    self.round += 1

            if event.button == 3:
                print("left clic")

    def print_piece(self, row, col, color):
        #self.rects[row][col] =  pygame.draw.rect(self.screen, (0, 0, 0), (16 + col * CELL_SIZE, 32 + row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
        x = col * CELL_SIZE + OFFSET_LEFT + CELL_SIZE/2
        y = row * CELL_SIZE + OFFSET_TOP + CELL_SIZE/2
        pygame.draw.circle(self.screen,color, (x,y), PIECE_SIZE, PIECE_SIZE)

    def ai_round(self):
        col = 0
        return col

    def start_game(self):
        pygame.init()
        #Initialisation du timer
        timer = Timer(pygame.time.get_ticks())
        self.screen = pygame.display.set_mode((640, 455))
        run = True

        while run:            
            self.screen.fill((255, 255, 255))  

       
            if (self.round % 2) == 1:
                # IA ici
                col = self.ai_round()
                
                if (self.add_piece(col, 2)):
                    self.round += 1


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                self.handle_mouse_event(event)

            for row in range(self.LINES):
                for col in range(self.COLUMN):
                    self.rects[row][col] =  pygame.draw.rect(self.screen, (0, 0, 0), (OFFSET_LEFT + col * CELL_SIZE, OFFSET_TOP + row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
                    if self.power4[row][col] == 1:
                        self.print_piece(row, col, (255,0,0))
                    if self.power4[row][col] == 2:
                        self.print_piece(row, col, (0,255,0))

            timer.update(pygame.time.get_ticks())
            
            font = pygame.font.SysFont('Arial', 16)
            text = font.render(str(timer), True, (0, 0, 0))
            self.screen.blit(text, (16, 8))

            pygame.display.flip()

        pygame.quit()
