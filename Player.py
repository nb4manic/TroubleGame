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

    def add_home_piece(self):
        self.active_pieces -= 1
        self.home_pieces += 1

    def wake_piece(self):
        self.start_pieces -= 1
        self.active_pieces += 1

    def sleep_piece(self):
        self.start_pieces += 1
        self.active_pieces -= 1

    def make_pieces(self, y, x):
        for number in range(1, 5):
            piece = [PlayerPiece(str(self.color), number, [y, x])]
            self.pieces.append({number: piece})

    def get_piece(self, index):
        active_piece = self.pieces[index-1][index]
        return active_piece

    # todo: functions to change pieces from active to home and active back to start


if __name__ == "__main__":
    print('''
    This is the Player class test sequence
    ''')
    testi = Player('red', 'Testi')
    print(testi.name)
    testi.make_pieces()
    current_piece = testi.get_piece(1)
    print(current_piece[0])
    #print(current_piece.color)
