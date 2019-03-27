from Player import *

#he
class PlayerPiece:

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.coordinates = []
        self.status = 'start'
        self.total_spaces_moved = 0

    def move_piece(self, move_by=0):
        self.total_spaces_moved += move_by
        print(f"Moving {self.color}'s number {self.name} piece {move_by} space(s)\n")
        return self.total_spaces_moved

    def get_coordinates(self):
        return self.coordinates

    def store_coordinates(self, coordinates):
        self.coordinates = coordinates

    def awaken(self):
        self.status = 'active'

    def sleep(self):
        self.status = 'start'
        self.coordinates = []
        print('I have gone to sleep')

    def home_run(self):
        self.status = 'home'

if __name__ == "__main__":

    '''
    Make players / define colors and names
    Add four players to list called 'players'
    '''

    player_one = Player('red', 'Adam',)
    player_two = Player('blue', 'Jack')
    player_three = Player('green', 'Arnold')
    player_four = Player('yellow', 'Bart')

    red = player_one
    blue = player_two
    green = player_three
    yellow = player_four

    players = [red, blue, green, yellow]

    '''
    Make pieces for players / define color and number and default coordinates (stored in list)
    Access pieces through dictionary (key / value pairs)
        Player variable is the key
    '''

    pieces = {red: [PlayerPiece('red', '1', [0, 0]),
                    PlayerPiece('red', '2', [0, 0]),
                    PlayerPiece('red', '3', [0, 0]),
                    PlayerPiece('red', '4', [0, 0])],

              blue: [PlayerPiece('blue', '1', [0, 0])]
              }

    # iterate over list called players and print player colors/names
    for player in players:
        print(f"{player.name} is {player.color}\n")

    for num in range(1,8):
        pieces[red][0].move_piece(3)

    print(pieces[red][0].total_spaces_moved)
    print(pieces[red][1].name)
    red.wake_piece()
    print(red.start_pieces)
    print(red.active_pieces)


