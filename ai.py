import copy
import numpy as np
import random

class AI:
    def __init__(self, array, player_playing, other_player):
        self.array = array
        self.nb_rows = len(self.array)
        self.nb_columns = len(self.array[0])
        self.player_playing = player_playing
        self.other_player = other_player

    def list_all_possibilities(self, array):

        index_rows = [-1]*7

        # On fait une liste de tous les coups possible
        for index_col in range(self.nb_columns):
            for index_row_desc in range(self.nb_rows-1, -1, -1): # index row descendant
                if (array[index_row_desc][index_col] == 0):
                    index_rows[index_col] = index_row_desc
                    break
        return index_rows
        # pour chaque coup on calcule son score

    def check_align4(self, row, col, temp_array):
        if row != -1:
            temp_array[row][col] = self.player_playing
            if self.check_win(temp_array, self.player_playing, 4):
                return col
        return -1
    
    def check_align3(self, row, col, temp_array):
        if row != -1:
            temp_array[row][col] = self.player_playing
            if self.check_win(temp_array, self.player_playing, 3):
                return col
        return -1
    
    def check_block4(self, row, col, temp_array):
        if row != -1:
            temp_array[row][col] = self.other_player
            if self.check_win(temp_array, self.other_player, 4):
                return col
        return -1

    def search_best_col(self):
        scores = [-1, 0, 1, 1, 1, 0, -1]

        # On liste toutes les possibilites
        possibilities = self.list_all_possibilities(self.array)
        print(possibilities)

        for i, p in enumerate(possibilities):
            print(p, i)
            if p == -1:
                print("scores i -1000", scores[i])
                scores[i] -= 1000

        depth = 2
        array_copy = copy.deepcopy(self.array)
        for i in range(depth):

            # Pour chaque possibilites on calcule son score
            # Pour calculer le score on va additioner les bloquage et les alignements que permet le coup

            for col in range(self.nb_columns):
                
                array_copy = copy.deepcopy(self.array)

                # si le coup permet d'aligner 4 pieces +50
                if (self.check_align4(possibilities[col], col, copy.deepcopy(array_copy)) != -1):
                    scores[col] += 500
                # si le coup permet d'aligner 3 pieces +5
                if (self.check_align3(possibilities[col], col, copy.deepcopy(array_copy)) != -1):
                    scores[col] += 5
                # si le coup permet de bloquer 4 pieces +25
                if (self.check_block4(possibilities[col], col, copy.deepcopy(array_copy)) != -1):
                    scores[col] += 250
            
               


        # faire une liste des index des scores max
        indexes = self.list_all_indexes_of_max(scores)
        random_index = random.choice(indexes)
        print(scores)
        print("meilleur choix",random_index)
        return random_index
    

    def list_all_indexes_of_max(self, scores):
        max = 0
        indexes = []

        for i in range(len(scores)):
            if scores[i] == max:
                indexes.append(i)
            if scores[i] > max:
                max = scores[i]
                indexes.clear()
                indexes.append(i)


        return indexes

    def check_win(self, temp_array, num, win):
        # on check la ligne
        pow = 0
        for row in range(self.nb_rows):
            pow = 0
            for i in range(self.nb_columns):
                if temp_array[row][i] == num:
                    pow += 1
                else:
                    pow = 0
                if pow == win:
                    return True

        # on check la colonne
        for col in range(self.nb_columns):
            pow = 0
            for i in range(self.nb_rows):
                if temp_array[i][col] == num:
                    pow += 1
                else:
                    pow = 0
                if pow == win:
                    return True

        diags = self.list_all_diagonals(temp_array)
        for n in diags:
            pow = 0
            for i in range(len(n)):
                if n[i] == num:
                    pow += 1
                else:
                    pow = 0
                if pow == win:
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