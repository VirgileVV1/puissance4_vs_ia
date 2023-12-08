import copy


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
