
def make_board(x, y):
    board = [['(o)' for count in range(x)] for rows in range(y)]
    return board


def print_board(board):
    # todo: coordinates
    for row in board:
        print(' '.join(row))
    print('')


# print('x: ', end='')
x = 7  # get_board_size()
# print('y: ', end='')
y = 7  # get_board_size()
my_board = make_board(x, y)  # (x, y)
print_board(my_board)

# put value as string, indexes are 0 based
# [y][x]

# red win_state
my_board[1][1] = '(R)'
my_board[1][2] = '(R)'
my_board[1][3] = '(R)'
my_board[1][4] = '(R)'
red_win_spaces = [my_board[1][1], my_board[1][2], my_board[1][3], my_board[1][4]]

# blue win_state
my_board[1][5] = '(B)'
my_board[2][5] = '(B)'
my_board[3][5] = '(B)'
my_board[4][5] = '(B)'
blue_win_spaces = [my_board[1][5], my_board[2][5], my_board[3][5], my_board[4][5]]

# green win_state
my_board[5][5] = '(G)'
my_board[5][4] = '(G)'
my_board[5][3] = '(G)'
my_board[5][2] = '(G)'
green_win_spaces = [my_board[5][5], my_board[5][4], my_board[5][3], my_board[5][2]]

# yellow win_state
my_board[5][1] = '(Y)'
my_board[4][1] = '(Y)'
my_board[3][1] = '(Y)'
my_board[2][1] = '(Y)'
yellow_win_spaces = [my_board[5][1], my_board[4][1], my_board[3][1], my_board[2][1]]

# dice
my_board[3][3] = '[6]'

# unused spaces
my_board[2][2] = '   '
my_board[2][3] = '   '
my_board[2][4] = '   '

my_board[3][2] = '   '
my_board[3][4] = '   '

my_board[4][2] = '   '
my_board[4][3] = '   '
my_board[4][4] = '   '

unused_space = {my_board[2][2], my_board[2][3], my_board[2][4], my_board[3][2], my_board[3][4],
                my_board[4][2], my_board[4][3], my_board[4][4]}

# playable_spaces = [my_board.remove(unused_space)]
# print(playable_spaces)

my_board[1][0] = '(Z)'

print_board(my_board)
print(my_board)

for spaces in red_win_spaces:
    print(spaces)

print(blue_win_spaces)
print(green_win_spaces)
print(yellow_win_spaces)
