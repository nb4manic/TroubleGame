from Piece import *


class Player:

    def __init__(self, color, name, start_coordinates, pivot_point, win_coordinates):
        self.color = color
        self.name = name
        self.start_coordinates = start_coordinates
        self.pivot_point = pivot_point
        self.win_coordinates = win_coordinates
        self.win_condition = False
        self.pieces = []
        self.start_pieces = 4
        self.active_pieces = 0
        self.home_pieces = 0

    def you_win(self):
        self.win_condition = True
   
    def wake_piece(self):
        self.start_pieces -= 1
        self.active_pieces += 1

    def add_home_piece(self):
        self.active_pieces -= 1
        self.home_pieces += 1

    def sleep_piece(self):
        self.start_pieces += 1
        self.active_pieces -= 1


# todo: have player class make its own pieces?
'''
    def make_pieces(self, y, x):
        for number in range(1, 5):
            piece = [PlayerPiece(str(self.color), number, [y, x])]
            self.pieces.append({number: piece})
'''