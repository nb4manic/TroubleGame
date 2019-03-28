from Piece import *
from Player import *
from logicboard import *
from yes_no_check import *
from index_chopper import *
from colorama import init, Fore, Style

'''
Coordinates are in [y, x] format
'''


# todo: clean up and remove test prints
# todo: review functions dealing with collision and see if they can be simplified 

# todo: add computer player/AI. Start simple and select a random move, later add more logic

# todo: Write stats to csv file and structure it. Wins/turns/total moves/total roll etc.

# todo: add terminal colors. Pieces should print the number and be shaded their respective colors

# todo: Sort players list based on roll order # Eventually, add a re - roll for when players roll the same number


def master_collision(piece, coordinates, move_roll=0):  
    # returns True if colliding with allied piece 

    # coordinates are piece coordinates OR player start coordinates if awakening piece
    # Pass player instead of piece if awakening a piece, cannot get color from piece if piece not chosen!
 
    move_collision = my_board.collision_check(coordinates)
    if move_collision:
        collision_index = my_board.get_obstacle(coordinates)
        collision_piece = my_board.pieces_on_board[collision_index]
        print(collision_piece) # would print coords, piece number, and player color
        if collision_piece[2] == piece.color:
            print("I can\'t kick out my own teammate! Make another move, boss! ")
            return True
        if collision_piece[2] != piece.color:
            my_board.to_be_removed(collision_index)
            return False
            # move that bitch
        else:
            return False


def make_piece_sprite(piece_name, player_color):  # returns a sprite for board print

    # replace return statements with f'({player_color})' if removing colorama 

    if player_color == 'red':
        return f'{Fore.RED}({piece_name}){Style.RESET_ALL}'

    if player_color == 'blue':
        return f'{Fore.BLUE}({piece_name}){Style.RESET_ALL}'

    if player_color == 'green':
        return f'{Fore.GREEN}({piece_name}){Style.RESET_ALL}'

    if player_color == 'yellow':
        return f'{Fore.YELLOW}({piece_name}){Style.RESET_ALL}'


init()  # initialize colorama

# create board instance
my_board = Board(7, 7)

# red win_state
red_start_coordinates = [0, 0]
red_pivot = [1, 0]
red_win_coordinates = [[1, 1], [1, 2], [1, 3], [1, 4]]

# blue win_state
blue_start_coordinates = [0, 6]
blue_pivot = [0, 5]
blue_win_coordinates = [[1, 5], [2, 5], [3, 5], [4, 5]]

# green win_state
green_start_coordinates = [6, 6]
green_pivot = [5, 6]
green_win_coordinates = [[5, 5], [5, 4], [5, 3], [5, 2]]

# yellow win_state
yellow_start_coordinates = [6, 0]
yellow_pivot = [6, 1]
yellow_win_coordinates = [[5, 1], [4, 1], [3, 1], [2, 1]]

# dice
dice_space = [3, 3]

unused_space = (2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)
my_board.wipe_unused(unused_space)  # replaces unused board spaces with strings containing white space

# get player names and strip whitespaces
p1 = 'Adam'  # input('Who is red? ').strip()
p2 = 'Jack'  # input('Who is blue? ').strip()
p3 = 'Arnold'  # input('Who is green? ').strip()
p4 = 'Bart'  # input('Who is yellow? ').strip()

# create 4 instances of imported Player class
red = Player('red', p1, red_start_coordinates, red_pivot, red_win_coordinates)
blue = Player('blue', p2, blue_start_coordinates, blue_pivot, blue_win_coordinates)
green = Player('green', p3, green_start_coordinates, green_pivot, green_win_coordinates)
yellow = Player('yellow', p4, yellow_start_coordinates, yellow_pivot, yellow_win_coordinates)

# Pieces associated with their respective player/color through key/value
# player instance variable = key / list of piece instances = value
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


if __name__ == "__main__":

    while not (red.win_condition or blue.win_condition
            or green.win_condition or yellow.win_condition):
        
        for current_player in players:
            current_turn = True
            possible_move = True
            awoken_piece = False
            activate_piece = False
            first_step_collision = False
            move_collision = False
            removal_check = my_board.check_for_removals(current_player)
            
            while removal_check:
                removal_index = my_board.index_removals(current_player)  # search removal queue for pieces sent back to start
                piece_number = my_board.removal_queue[removal_index][1]
                removal_piece = pieces[current_player][(int(piece_number) - 1)]  
                print('{}\'s #{} piece is being sent home'.format(removal_piece.color.capitalize(), removal_piece.name))
                removal_piece.sleep()
                current_player.sleep_piece()
                my_board.delete_from_removal(removal_index)
                removal_piece = None
                removal_index = None
                removal_check = my_board.check_for_removals(current_player)

            while current_turn:
                turn_roll = roll()
                move_roll = turn_roll
                # my_board.board_check()  # uncomment if removing colorama

                input('Press Enter key to roll ')
                my_board.replace_coord(3, 3, '[{}]'.format(turn_roll)) # replace middle board space with dice roll
                print(f'{current_player.color.capitalize()} player {current_player.name.capitalize()} '
                    f'just rolled a {turn_roll}. ')

                # Ends current_player turn if no pieces to move and unable to awaken any
                if turn_roll != 6 and (current_player.active_pieces + current_player.home_pieces) == 0:
                    print('Better luck next time, chump!\n')
                    break

                elif turn_roll == 6 and current_player.start_pieces > 0:
                    if current_player.active_pieces == 0:
                        activate_piece = True
                    else:
                        activate_piece = yn_check('Would you like to move a piece out? Y/N ')

                    while activate_piece:
                        if master_collision(current_player, current_player.start_coordinates):
                            activate_piece = False
                            awoken_piece = False
                            break
                        awoken_piece = True
                        current_player.wake_piece()     # adjust current_player start_pieces and active_pieces
                        move_roll = 1  # awoken pieces only move onto board 1 space
                        activate_piece = False

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
                        current_piece.awaken()  # sets piece's status to active
                        piece_chosen = True
                        break

                    elif awoken_piece and (current_piece.status != 'start'):
                        print('That piece is already on the board...\n')
                        continue
                    elif current_piece.status == 'start':
                        print('Choose an active piece\n')
                        continue

                    future_move = board_move(current_piece.coordinates, current_player.pivot_point, 
                    current_piece, current_player.win_coordinates, current_player, move_roll)

                    # move forward with current_piece if status is active and piece was not awoken this turn
                    if not future_move or master_collision(current_piece, future_move):
                        print('Pick another piece! ')
                        for piece in pieces[current_player]:  
                            # this may be able to be reloacted, but be aware of calculating possible moves of awoken pieces
                            # currently returns no possible moves even if move possible
                            # make function?
                            if piece.status != 'start':
                                hypothetical_move = board_move(piece.coordinates, current_player.pivot_point,
                                piece, current_player.win_coordinates, current_player, move_roll)
                                if hypothetical_move and not master_collision(piece, hypothetical_move):
                                    possible_move = True
                                    break

                        if not hypothetical_move:
                            possible_move = False
                        
                        if possible_move:
                            continue
                

                    piece_chosen = True


                if not possible_move:
                    print('No possible moves! ')
                    break

                if awoken_piece:  # if piece moved from start to board
                    current_piece.store_coordinates(current_player.start_coordinates)
                    piece_sprite = make_piece_sprite(current_piece.name, current_player.color)
                    my_board.replace_coord(current_player.start_coordinates[0], current_player.start_coordinates[1], piece_sprite)
                    my_board.bind_piece(current_player.start_coordinates, current_piece.name, current_player.color)
                    # update board coordinate stat list

                    my_board.print_board()  # reprint board after moving piece out
                    awoken_piece = False 
                    continue


                print('')

                # The following lines must happen before modifying current_piece.coordinates
                # If they don't, the board print out will retain previous traces of current_piece
                my_board.replace_coord(current_piece.coordinates[0], current_piece.coordinates[1], '(o)')
                # replace piece print on board. Does NOT update coordinate
                del my_board.pieces_on_board[my_board.unbind_piece(current_piece.name, current_piece.color)]
                # remove place in board queue

                
                current_piece.move_piece(move_roll)  # move piece by turn roll amount or 1 if piece awoken from start
                current_piece.coordinates = board_move(current_piece.coordinates, current_player.pivot_point,
                current_piece, current_player.win_coordinates, current_player, move_roll)
                # Modify current_piece.coordinates with algorithm by passing current coordinates and move_roll 
                piece_sprite = make_piece_sprite(current_piece.name, current_player.color)
                my_board.replace_coord(current_piece.coordinates[0], current_piece.coordinates[1], piece_sprite)
                # change board print coordinate to first letter of player color

                my_board.bind_piece(current_piece.coordinates, current_piece.name, current_player.color)
                # update board coordinate stat list

                if (current_piece.coordinates in current_player.win_coordinates) and (current_piece.status != 'home'):
                    current_piece.home_run()
                    current_player.add_home_piece()

                my_board.print_board()  # reprint the board

                if current_player.home_pieces > 3:  # win condition check and change
                    current_player.you_win()  # set player win condition
                    winner = current_player
                    break

                if turn_roll == 6:
                    continue  # give player another turn if turn roll was 6
                    
                current_turn = False  # end current turn

            if current_player.home_pieces > 3:  # win condition check and change
                current_player.you_win()  # set player win condition
                winner = current_player
                break

    # victory prints only available once a player gets 4 pieces into home
    victory_print = f'{winner.name.capitalize()} the {winner.color} is the winner!\n'
    congratulations = 'Congratulations!!!\n\n'
    print(victory_print * 10)
    print(congratulations * 4)

