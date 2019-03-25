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
            print('Invalid input.\n' * 1)
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


# create board instance
my_board = Board(7, 7)

# red win_state
red_start_coordinates = [0, 0]
red_pivot = [1, 0]
red_win_coordinates = [1, 1], [1, 2], [1, 3], [1, 4]

# blue win_state
blue_start_coordinates = [0, 6]
blue_pivot = [0, 5]
blue_win_coordinates = [1, 5], [2, 5], [3, 5], [4, 5]

# green win_state
green_start_coordinates = [6, 6]
green_pivot = [5, 6]
green_win_coordinates = [5, 5], [5, 4], [5, 3], [5, 2]

# yellow win_state
yellow_start_coordinates = [6, 0]
yellow_pivot = [6, 1]
yellow_win_coordinates = [5, 1], [4, 1], [3, 1], [2, 1]

# dice
my_board.replace_coord(3, 3, '[6]')

unused_space = (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)
my_board.wipe_unused(unused_space)

# get player names and strip whitespaces
p1 = 'Adam'  # input('Who is red? ').strip()
p2 = 'Jack'  # input('Who is blue? ').strip()
p3 = 'Arnold'  # input('Who is green? ').strip()
p4 = 'Bart'  # input('Who is yellow? ').strip()

# create 4 instances of imported Player class
# color, name, pivot coordinate, and win coordinates list per player
    # pivot coordinate for victory path
# coordinates stored in board.py
red = Player('red', p1, red_start_coordinates, red_pivot, red_win_coordinates)
blue = Player('blue', p2, blue_start_coordinates, blue_pivot, blue_win_coordinates)
green = Player('green', p3, green_start_coordinates, green_pivot, green_win_coordinates)
yellow = Player('yellow', p4, yellow_start_coordinates, yellow_pivot, yellow_win_coordinates)

# Pieces associated with their respective player/color through key/value
# player instance variable = key / list of piece instances = value
# pass a start coordinate for pieces in [y, x] format
pieces = {red: [PlayerPiece('red', '1'),
                PlayerPiece('red', '2'),
                PlayerPiece('red', '3'),
                PlayerPiece('red', '4')],
          # pivot 1,0 -> 1,4

          blue: [PlayerPiece('blue', '1'),
                 PlayerPiece('blue', '2'),
                 PlayerPiece('blue', '3'),
                 PlayerPiece('blue', '4')],
          # pivot 0,5 -> 4,5

          green: [PlayerPiece('green', '1'),
                  PlayerPiece('green', '2'),
                  PlayerPiece('green', '3'),
                  PlayerPiece('green', '4')],
          # pivot 5,6 -> 5,2

          yellow: [PlayerPiece('yellow', '1'),
                   PlayerPiece('yellow', '2'),
                   PlayerPiece('yellow', '3'),
                   PlayerPiece('yellow', '4')],
          # pivot 6,1 -> 2,1
          }


players = [red, blue, green, yellow]
winner = None


while not (red.win_condition or blue.win_condition
           or green.win_condition or yellow.win_condition):
    '''
    These nested loops will only end once a player's home_piece variable > 3
    '''
    for current_player in players:
        current_turn = True
        awoken_piece = False

        while current_turn:
            print(f"{current_player.color}'s win coordinates are {current_player.win_coordinates} ")  # test print
            print("This is the status of those spaces: ")
            for coordinates in current_player.win_coordinates:
                print(my_board.get_coord(coordinates[0], coordinates[1]))
            print(f" Their pivot point looks like: " 
                  f"{my_board.get_coord(current_player.pivot_point[0], current_player.pivot_point[1])} ")  # test print
            my_board.board_check()

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
                    # todo: insert collision check
                    # collision_check(current_player.start_coordinates)
                    # if occupied by own piece
                    #   choose something else 
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
                current_piece = pieces[current_player][index_chopper('piece', 4)]  # 4 is max of the index (pieces)
                # set which piece to move by grabbing selected piece from current_player's pieces dictionary
                # index_chopper() method increments piece number to match list index
                if awoken_piece and current_piece.status == 'start':
                    # todo: insert check to ensure piece can move out
                    current_piece.awaken()  # sets piece's status to active
                    # my_board.bind_piece(current_piece.coordinates, current_piece.name, current_player.color)
                    # bind current piece to coords
                    piece_chosen = True
                elif awoken_piece and (current_piece.status != 'start'):
                    print('That piece is already on the board...\n')
                    continue
                elif current_piece.status != 'active':
                    print('Choose an active piece\n')
                    continue
                else:  # move forward with current_piece if status is active and piece was not awoken this turn
                    piece_chosen = True

            my_board.collision_check(current_piece.coordinates)
            #if not none:
                # reset dat bish

            current_piece.move_piece(move_roll)  # move piece by turn roll amount or 1 if piece awoken from start

            # todo: insert coordinate check if piece landed on

            if awoken_piece:  # if piece moved from start to board
                current_piece.store_coordinates(current_player.start_coordinates)
                my_board.replace_coord(current_player.start_coordinates[0], current_player.start_coordinates[1],
                                       f'({current_piece.color[0].capitalize()})')
                my_board.bind_piece(current_player.start_coordinates, current_piece.name, current_player.color)
                # update board coordinate stat list

                my_board.print_board()  # reprint board after moving piece out
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

            if turn_roll == 6: # this needs to be moved for when a piece isn't awoken, or a separate one
                awoken_piece = False
                continue  # give player another turn if turn roll was 6

            print('')
            my_board.replace_coord(current_piece.coordinates[0], current_piece.coordinates[1], '(o)')
            # leave previous coordinate and remove from board

            del my_board.pieces_on_board[my_board.unbind_piece(current_piece.name, current_piece.color)]
            # remove place in board queue

            current_piece.coordinates = board_move(current_piece.coordinates, move_roll)
            # redefine coordinates of current piece

            my_board.collision_check(current_piece.coordinates)
                # if not None then move that bish

            my_board.replace_coord(current_piece.coordinates[0], current_piece.coordinates[1],
                                   f'({current_piece.color[0].capitalize()})')
            # change board coordinate to first letter of player color
            my_board.bind_piece(current_piece.coordinates, current_piece.name, current_player.color)
            # update board coordinate stat list

            # print(leave_space)
            my_board.print_board()  # reprint the board
            current_turn = False  # end current turn

# victory prints only available once a player gets 4 pieces into home
print(f'{winner.name.capitalize()} the {winner.color} is the winner!\n' * 10)
print('Congratulations!!!\n\n' * 4)
