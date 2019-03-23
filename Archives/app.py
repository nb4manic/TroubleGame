from Piece import *
from Player import Player
from logicboard import *

# todo: implement player victory paths
# remove victory space from list once reached
# roll must be exact amount to secure victory space

# todo: y/n function
# only needed once but it will be good to have as a module

# todo: error check for player's moving multiple pieces out while first spot still occupied
# simple solution: disable moving a piece out when an active piece's coordinates are the same as default for that piece

# todo: logic for pieces occupying the same space
# current_piece moves obstacle_piece back to start
# How does current_piece know what obstacle_piece's start coordinate is?

# todo: Sort players list based on roll order # Eventually, add a re - roll for when players roll the same number


def index_chopper(item, max_amount=1000):
    # todo make this separate function/module
    # adjusts piece number to reflect index in list
    # pass max_amount to cap index --- default: 1000

    while True:
        value = input('Which {} would you like to get? '.format(item))
        try:
            list_index = int(value) - 1
        except ValueError:
            print('Invalid input.\n' * 4)
            continue

        if list_index >= max_amount:
            print("You don't have that many {}s!".format(item))
            print("Nobody does!\n")
            continue
        else:
            return list_index


def check_piece(active_player, piece):
    if active_player.color == piece.color:
        return print('Woo! ')


# get player names and strip whitespaces
p1 = 'Adam'  # input('Who is red? ').strip()
p2 = 'Jack'  # input('Who is blue? ').strip()
p3 = 'Arnold'  # input('Who is green? ').strip()
p4 = 'Bart'  # input('Who is yellow? ').strip()

# create 4 instances of imported Player class
# pass color, name, pivot coordinate for victory path, and finally a win coordinates list to each one
red = Player('red', p1, red_pivot, red_win_coordinates)  # coordinates stored in board.py
blue = Player('blue', p2, blue_pivot, blue_win_coordinates)
green = Player('green', p3, green_pivot, green_win_coordinates)
yellow = Player('yellow', p4, yellow_pivot, yellow_win_coordinates)

# Pieces associated with their respective player/color through key/value
# player instance variable = key / list of piece instances = value
pieces = {red: [PlayerPiece('red', '1', [0, 0]),  # pass a start coordinate for pieces in [y, x] format
                PlayerPiece('red', '2', [0, 0]),
                PlayerPiece('red', '3', [0, 0]),
                PlayerPiece('red', '4', [0, 0])],
          # pivot 1,0 -> 1,4

          blue: [PlayerPiece('blue', '1', [0, 6]),
                 PlayerPiece('blue', '2', [0, 6]),
                 PlayerPiece('blue', '3', [0, 6]),
                 PlayerPiece('blue', '4', [0, 6])],
          # pivot 0,5 -> 4,5

          green: [PlayerPiece('green', '1', [6, 6]),
                  PlayerPiece('green', '2', [6, 6]),
                  PlayerPiece('green', '3', [6, 6]),
                  PlayerPiece('green', '4', [6, 6])],
          # pivot 5,6 -> 5,2

          yellow: [PlayerPiece('yellow', '1', [6, 0]),
                   PlayerPiece('yellow', '2', [6, 0]),
                   PlayerPiece('yellow', '3', [6, 0]),
                   PlayerPiece('yellow', '4', [6, 0])],
          # pivot 6,1 -> 2,1
          }

players = [red, blue, green, yellow]
winner = None


while not (red.win_condition or blue.win_condition or green.win_condition or yellow.win_condition):
    '''
    These nested loops will only end once a player's home_piece variable is greater than 3
    '''
    for current_player in players:
        current_turn = True
        awoken_piece = False

        while current_turn:
            print(f"Current player's win coordinates are {current_player.win_coordinates} ")  # test print
            print(f"Their pivot point is {current_player.pivot_point} ")  # test print
            turn_roll = roll()
            move_roll = turn_roll

            input('Press any key to roll ')
            print(f'{current_player.color.capitalize()} player {current_player.name.capitalize()} '
                  f'just rolled a {turn_roll}. ')

            # Ends current_player turn if no pieces to move and unable to awaken any
            if turn_roll < 6 and current_player.active_pieces == 0:
                print('Better luck next time, chump!\n')
                break

            elif turn_roll == 6 and current_player.start_pieces > 0:  # todo prevent pieces moving out atop one another
                print('Would you like to move a piece out?\n')

                # todo Create y/n check function
                yn_check = 'y'  # y/n prompt bypass
                if yn_check == 'y' or current_player.active_pieces == 0:
                    awoken_piece = True
                    current_player.wake_piece()     # adjust current_player start_pieces and active_pieces
                    move_roll = 1                   # awoken pieces only move onto board 1 space
                    # All are awoken on their start coordinates
                    # todo: add
                else:
                    pass

            # main turn sequence
            current_piece = None
            piece_chosen = False

            while not piece_chosen:
                current_piece = pieces[current_player][index_chopper('piece', 4)]
                # set which piece to move by grabbing selected piece from current_player's pieces dictionary
                # index_chopper() method increments piece number to match list index
                if awoken_piece and current_piece.status == 'start':
                    current_piece.awaken()  # sets piece's status to active
                    piece_chosen = True
                if awoken_piece and current_piece.status != 'start':
                    print('That piece is already on the board...\n')
                    continue
                elif current_piece.status != 'active':
                    print('Choose an active piece\n')
                    continue
                else:  # move forward with current_piece if status is active and piece was not awoken this turn
                    piece_chosen = True

            my_board[current_piece.coordinates[0]][current_piece.coordinates[1]] = '(o)'
            # leave previous coordinate and remove from board

            current_piece.move_piece(move_roll)  # move piece by turn roll amount or 1 if piece awoken from start
            if awoken_piece:  # if piece moved from start to board
                my_board[current_piece.coordinates[0]][current_piece.coordinates[1]] = \
                    f'({current_piece.color[0].capitalize()})'
                print_board(my_board)  # reprint board after moving piece out
                print(current_piece.coordinates)
                awoken_piece = False  # needed so piece can be deleted before being moved
                '''
                If removed then this awoken_piece block is run on the re-roll after a piece is moved out
                If the piece is moved out, and immediately moved with the re-roll, then its previous spot on the 
                board will not be returned to its original state
                '''

            if current_player.home_pieces > 3:  # win condition check and change
                current_player.you_win()  # set player win condition
                winner = current_player
                break

            if turn_roll == 6:
                awoken_piece = False
                continue  # give player another turn if turn roll was 6

            print('')
            current_piece.coordinates = board_move(current_piece.coordinates, move_roll)
            # redefine coordinates of current piece
            my_board[current_piece.coordinates[0]][current_piece.coordinates[1]] =\
                f'({current_piece.color[0].capitalize()})'  # change board coordinate to first letter of player color

            # print(leave_space)
            print_board(my_board)  # reprint the board
            current_turn = False  # end current turn

# victory prints only available once a player gets 4 pieces into home
print(f'{winner.name.capitalize()} the {winner.color} is the winner!\n' * 10)
print('Congratulations!!!\n\n' * 4)
