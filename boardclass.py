from random import randint

class Board:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = [['(o)' for count in range(x)] for rows in range(y)]
        self.pieces_on_board = []
        self.removal_queue = []

    def print_board(self):
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

    def unbind_piece(self, piece_name, piece_color):  # pass current_piece.name and color
        # iterates through board queue and checks for entry matching piece name and color
        for index in range(len(self.pieces_on_board)):
            if self.pieces_on_board[index][1] == piece_name and self.pieces_on_board[index][2] == piece_color:
                return index  # return index if match found

    def board_check(self):
        for piece in self.pieces_on_board:
            print(piece)

    def wipe_coord(self, y, x):
        self.board[y][x] = '   '

    def wipe_unused(self, unused_list):
        for coordinates in unused_list:
            self.wipe_coord(coordinates[0], coordinates[1])  # access y, x values by index of coordinates list
    
    def collision_check(self, board_coordinates):  # returns True if any piece collided with
        # is iteration necessary? 
        # if board_coordinate in self.pieces_on_board?
        if len(self.pieces_on_board) > 0:
            for i in range(len(self.pieces_on_board)):
                if board_coordinates == self.pieces_on_board[i][0]:
                    return True

    def get_obstacle(self, board_coordinates): #returns index of collided piece
        # can I combine this with collision_check, or is it better to split the task?
        if len(self.pieces_on_board) > 0:
            for i in range(len(self.pieces_on_board)):
                if board_coordinates == self.pieces_on_board[i][0]:
                    return i

    def to_be_removed(self, index):  # adds piece to removal queue to remove from board
        self.removal_queue.append(self.pieces_on_board[index])
        del self.pieces_on_board[index]

    def check_for_removals(self, player):  # checks removal_queue for match in player color
        if len(self.removal_queue) > 0:
            for i in range(len(self.removal_queue)):
                if player.color == self.removal_queue[i][2]:
                    return True

    def index_removals(self, player):  # check removal_queue for match in player color and returns index
        if len(self.removal_queue) > 0:
            for i in range(len(self.removal_queue)):
                if player.color == self.removal_queue[i][2]:  # player color match
                    return i  # return index to remove

    def delete_from_removal(self, index):
        del self.removal_queue[index]



if __name__ == "__main__":
    print('Tests')