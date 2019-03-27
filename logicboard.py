from boardclass import *


def victory_pathing(y, x, piece, win_path, player, move_roll, pivot_secure):  # only called once pivot point reached
    #piece.status = 'stretch'
    #player.home_pieces = 4
    #player.win_condition = True
    overextend_warning = 'I can\'t move that far! '

    # win paths were working... now they aren't

    for num in range(move_roll):
        if win_path == [[1, 1], [1, 2], [1, 3], [1, 4]]:  # red
            if (x + move_roll) <= 4:
                x += 1
                move_roll -= 1
            else:
                print(overextend_warning)
                return False

        elif win_path == [[1, 5], [2, 5], [3, 5], [4, 5]]:  # blue
            if (y + move_roll) <= 4:
                y += 1
                move_roll -= 1

            else:
                print(overextend_warning)
                return False
    
        elif win_path == [[5, 5], [5, 4], [5, 3], [5, 2]]:  # green
            if (x - move_roll) >= 2:
                x -= 1
                move_roll -= 1
            else:
                print(overextend_warning)
                return False

        elif win_path == [[5, 1], [4, 1], [3, 1], [2, 1]]:  # yeller
            if (y - move_roll) >=2:
                y -= 1
                move_roll -= 1
            else:
                print(overextend_warning)
                return False

    return [y, x]


def board_move(board_state, pivot, piece, win_path, player, move_roll=0):  # pass player, pivot point

    y = board_state[0]  # define where y coordinate is stored/referenced for current piece
    x = board_state[1]  # define where x coordinate is stored/referenced for current piece
    pivot_secure = False

    for num in range(0, move_roll):  # also pass current piece coordinates, pivot point, and win coordinates list
        # todo

        if ([y, x] == pivot) and (move_roll != 0):
            pivot_secure = True

        if ([y, x] == pivot) or piece.status == 'home':
            # print('Almost there')
            victory_road = victory_pathing(y, x, piece, win_path, player, move_roll, pivot_secure)

            if pivot_secure and not victory_road:  # piece reached pivot point and move roll exceeds win path
                y = pivot[0]
                x = pivot[1]
                # print('Securing pivot point')
            if not pivot_secure and not victory_road:  # not on pivot and unable to move through win path
                return False
            if victory_road:  # moved into with path
                y = victory_road[0]
                x = victory_road[1]

            return[y, x]

        # add to x while y == 0 and x < 6
        if y == 0 and x < 6:
            x += 1
            move_roll -= 1
        # add to y while x == 6 and y < 6
        elif x == 6 and y < 6:
            y += 1
            move_roll -= 1
        # subtract from x while y == 6 and x > 0
        elif y == 6 and x > 0:
            x -= 1
            move_roll -= 1
        # subtract from y while x <= 6 and y > 1
        elif x <= 6 and y > 0:  # or (y <= 6 and x == 0):
            y -= 1
            move_roll -= 1

    # print(f'I am attempting to move to space {y, x}')  # demonstrate piece movement within loop
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
