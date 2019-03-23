from boardclass import *


'''
How are different win paths going to be handled?
'''


def board_move(board_state, move_roll=0):

    y = board_state[0]  # define where y coordinate is stored/referenced for current piece
    x = board_state[1]  # define where x coordinate is stored/referenced for current piece

    for num in range(0, move_roll):  # also pass current piece coordinates, pivot point, and win coordinates list
        # todo

        ''' 
        
        if current_piece.coordinates == current_player.pivot point or in current_player.win_coordinates
            call separate function
            
            that function must contain a separate algorithm for modifying board state
        
                if (move_roll + piece.coordinate) > win_coordinates[-1]:
                can't make that move! select another piece
                break  # insert check to make sure piece was moved during turn

                if (move_roll + piece.coordinates) < win_coordinates[-1]:
                    board_move
            
                if (move_roll + piece.coordinates) == win_coordinates[-1]:
                    board_move
                    del player.win_spaces[-1]
        
        '''

        # add to x while y == 0 and x < 6
        if y == 0 and x < 6:
            x += 1
        # add to y while x == 6 and y < 6
        elif x == 6 and y < 6:
            y += 1
        # subtract from x while y == 6 and x > 0
        elif y == 6 and x > 0:
            x -= 1
        # subtract from y while x <= 6 and y > 1
        elif x <= 6 and y > 0:  # or (y <= 6 and x == 0):
            y -= 1

        print(f'I am moving to space {y, x}')  # demonstrate piece movement within loop
    return [y, x]  # return final y and x values in a [list] after completing loop


if __name__ == "__main__":
    my_board = Board(7, 7)
    piece_coordinate = [0, 0]  # must be held in list or other mutable data type
    print(piece_coordinate)  # show active piece's coordinate

    my_board.replace_coord(0, 1, '(A)')
    my_board.print_board()

    my_board.replace_coord(0, 1, '(O)')  # remove piece from board before moving
    piece_coordinate = board_move(piece_coordinate, 6)  # returns a list
    print(piece_coordinate)  # show active piece's coordinate

    my_board.replace_coord(0, 1, '(A)')
    my_board.print_board()

    my_board.replace_coord(0, 1, '(O)')  # remove piece from board before moving
    piece_coordinate = board_move(piece_coordinate, 9)  # returns a list
    print(piece_coordinate)  # show active piece's coordinate

    # code before making board a class
    # my_board[piece_coordinate[0]][piece_coordinate[1]] = '(A)'
    # print_board(my_board)

    print(piece_coordinate)  # show active piece's coordinate

    my_board.replace_coord(0, 1, '(R)') # f'({piece.color[0].capitalize()})'
    my_board.print_board()

    me = board_move((0, 0), 6)
    print(me)

    cord = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6]]
    if me in cord:
        print('Woo')