from random import randint


def roll():
    return randint(1, 6)


class Board:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = [['(o)' for count in range(x)] for rows in range(y)]
        self.pieces_on_board = []

    def print_board(self):
        # todo: coordinates
        for row in self.board:
            print(' '.join(row))
        print('')

    def get_coord(self, y, x):
        return self.board[y][x]

    def replace_coord(self, y, x, replace):
        self.board[y][x] = replace

    def bind_piece(self, coordinates, piece, player):
        stats = [coordinates, piece, player]
        self.pieces_on_board.append(stats)

    def unbind_piece(self, piece_name, piece_color):
        for index in range(len(self.pieces_on_board)):
            print(index, self.pieces_on_board[index])
            if self.pieces_on_board[index][1] == piece_name and self.pieces_on_board[index][2] == piece_color:
                return index
        # pass current_piece.name and color

    def board_check(self):
        for piece in self.pieces_on_board:
            print(piece)

    def wipe_coord(self, y, x):
        self.board[y][x] = '   '

    def wipe_unused(self, unused_list):
        for coordinates in unused_list:
            self.wipe_coord(coordinates[0], coordinates[1])  # access y, x values by index of coordinates tuples
    
    def collision_check(self, board_coordinates):
        if len(self.pieces_on_board) > 0:
            for i in range(len(self.pieces_on_board)):
                print("{}{}".format(i, self.pieces_on_board[i][0]))
                print('Occupied by: {}'.format(self.pieces_on_board[i][1:]))
                if board_coordinates == self.pieces_on_board[i][0]:
                    print('Kick out {}'.format(self.pieces_on_board[i][1:]))
                    #return index of collided piece
                #loop over board coordinates



if __name__ == "__main__":

    my_board = Board(7, 7)
    my_board.print_board()

    my_board.replace_coord(1, 2, '(R)')
    print(my_board.get_coord(1, 2))
    print('')

    my_board.print_board()

    my_board.wipe_coord(3, 3)
    my_board.print_board()

    # red win_state
    red_pivot = my_board.get_coord(1, 0)
    red_win_coordinates = (1, 1), (1, 2), (1, 3), (1, 4)

    # blue win_state
    blue_pivot = my_board.get_coord(0, 5)
    blue_win_coordinates = (1, 5), (2, 5), (3, 5), (4, 5)
    # green win_state
    green_pivot = my_board.get_coord(5, 6)
    green_win_coordinates = (5, 5), (5, 4), (5, 3), (5, 2)

    # yellow win_state
    yellow_pivot = my_board.get_coord(6, 1)
    yellow_win_coordinates = (5, 1), (4, 1), (3, 1), (2, 1)

    # dice
    my_board.replace_coord(3, 3, '[6]')

    my_board.print_board()

    unused = (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)
    my_board.wipe_unused(unused)
    my_board.print_board()

    # i want to take the coordinate tuple and compare it to the board[0][0]
    piece_coordinates = [0, 0]
    if piece_coordinates in unused:
        print('yay!')

    # my_board.replace_coord(active_piece.coordinate[0], active_piece.coordinates[1])

    my_board.wipe_unused(yellow_win_coordinates)
    my_board.print_board()

    my_board.bind_piece(piece_coordinates, 'piece 2', 'jack')
    my_board.bind_piece((3, 6), 'piece 3', 'arny')
    my_board.bind_piece((1, 9), 'piece 11', 'atkinston')
    my_board.bind_piece((9, 0), 'piece 0', 'i have no name')
#  my_board.unbind_piece(piece_coordinates, current_piece, current_player
#  if next_coord in coordinates_in_play:
    # remove projected space coordinates_in_play, piece and player and make adjustments

    my_board.board_check()

    print(my_board.pieces_on_board)

    # todo
    # todo
    # todo
    # todo
    new_coord = [0, 0]
    house_keeping = []
    for piece in my_board.pieces_on_board:
        house_keeping.append(piece[0])
    if new_coord in house_keeping:
        print('Yay')
        house_keeping.index(new_coord)
        '''
         return index?
         reference index with board queue
         get piece information from board queue
         if current_piece.name = target_piece.name:
             can't move on your own piece
             current_piece = None
         else:
             (send that bitch back home!)    
        '''

        # house_keeping[i] = pieces_on_board[i]

    for coordinates in house_keeping:
        print(coordinates)
    print(my_board.pieces_on_board[2][0])
    print('')
    for coord in range(len(my_board.pieces_on_board)):
        print(f'I am {my_board.pieces_on_board[coord][0]}')
    #print(my_board.pieces_on_board[range(len(my_board.pieces_on_board))][0])
    print('')
    my_board.collision_check([0, 0])
    print('')
    print(my_board.pieces_on_board)
    del my_board.pieces_on_board[my_board.unbind_piece('piece 3', 'arny')]
    print(my_board.pieces_on_board)
    print('')
    print('')
    print(my_board.pieces_on_board[1])
    