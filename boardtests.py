from boardclass import *
from logicboard import *

if __name__ == "__main__":
    my_board = Board(7, 7)
    my_board.print_board()
    coordinate1 = [0, 0]
    coordinate2 = [0, 2]
    my_board.bind_piece(coordinate1, '1', 'red')
    my_board.bind_piece(coordinate2, '2', 'blue')
    print(my_board.pieces_on_board)

    print(my_board.pieces_on_board[len(my_board.pieces_on_board) - 1][0])

    if coordinate1 in my_board.pieces_on_board[len(my_board.pieces_on_board) - 1][0]:
        print('Yay')

    for piece in my_board.pieces_on_board:
        print('Printing relevant piece information {}'.format(piece))
        # print all entries in board queue

        print('Printing piece coordinates {}'.format(piece[0]))
        # print coordinates for comparison

        print('Printing relevant piece information {}'.format(piece[1:]))
        # print remaining information to reset player piece

    for i in range(len(my_board.pieces_on_board)):
        print("{} {}".format(i, my_board.pieces_on_board[i][0]))