import pygame
from timer import Timer
import copy 
from ai import AI
import numpy as np


CELL_SIZE = 64
OFFSET_TOP = 48
OFFSET_LEFT = 32
PIECE_SIZE = 25 # x2
ROWS = 6
COLUMNS = 7

class Game:

    def __init__(self):
        self.round = 0
        self.power4 = []
        self.rects = []
        self.initialize()
        self.start_game()

    def initialize(self):
        for i in range(ROWS):
            temp = []
            rect = []
            for j in range(COLUMNS):
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

    def print_game(self):
        for i in range(ROWS):
            for j in range(COLUMNS):
                print(self.power4[i][j], end="")
            print()

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
                if (self.round % 2) == 1:       # c'est l'ia 
                    for row in self.rects:
                        for col, rect in enumerate(row):
                            if (rect.collidepoint(event.pos)):
                                if self.add_piece(col, 2):
                                    self.round += 1
        if event.type == pygame.K_f:
            print("c'est au tour de l'ia")

    def print_piece(self, row, col, color):
        #self.rects[row][col] =  pygame.draw.rect(self.screen, (0, 0, 0), (16 + col * CELL_SIZE, 32 + row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
        x = col * CELL_SIZE + OFFSET_LEFT + CELL_SIZE/2
        y = row * CELL_SIZE + OFFSET_TOP + CELL_SIZE/2
        pygame.draw.circle(self.screen,color, (x,y), PIECE_SIZE, PIECE_SIZE)

    def check_win(self, num):
        # on check la ligne
        for row in range(ROWS):
            pow = 0
            for i in range(COLUMNS):
                if self.power4[row][i] == num:
                    pow += 1
                else:
                    pow = 0
                if pow == 4:
                    return True

        # on check la colonne
        for col in range(COLUMNS):
            pow = 0
            for i in range(ROWS):
                if self.power4[i][col] == num:
                    pow += 1
                else:
                    pow = 0
                if pow == 4:
                    return True

        diags = self.list_all_diagonals(self.power4)
        for n in diags:
            pow = 0
            for i in range(len(n)):
                if n[i] == num:
                    pow += 1
                else:
                    pow = 0
                if pow == 4:
                    return True

    def list_all_diagonals(self, array):
        a = np.array(array)
        diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]

        # Now back to the original array to get the upper-left-to-lower-right diagonals,
        # starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.
        diags.extend(a.diagonal(i) for i in range(a.shape[1]-1,-a.shape[0],-1))

        # Another list comp to convert back to Python lists from numpy arrays,
        # so it prints what you requested.
        return diags
     

    def ai_round(self): 
        ai = AI(copy.copy(self.power4), 2, 1)
        return ai.search_best_col()
        
    def start_game(self):
        pygame.init()
        #Initialisation du timer
        timer = Timer(pygame.time.get_ticks())
        self.screen = pygame.display.set_mode((640, 455))
        run = True
        win = None
        while run:            
            self.screen.fill((255, 255, 255))  

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if win is None:
                    self.handle_mouse_event(event)

            if win is not None:
                font = pygame.font.SysFont('Arial', 16)
                text = font.render("Victoire du joueur "+str(win), True, (0, 0, 0))
                self.screen.blit(text, (16, 8)) 
            else:
                #self.print_game()
                #print()

                #if (self.round % 2) == 1:
                    # IA ici
                    #col = self.ai_round()
                    #print("col", col)
                    #if col != -1:
                        #if (self.add_piece(col, 2)):
                            #self.round += 1
                    #else:
                        #print("l'ia est bloque")
                        #run = False

                if self.check_win(1) == True:
                    print("joueur 1 gagnant")
                    win = 1
                if self.check_win(2) == True:
                    win = 2
                    print("joueur 2 gagnant")

                for row in range(ROWS):
                    for col in range(COLUMNS):
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
