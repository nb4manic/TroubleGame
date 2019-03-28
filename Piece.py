from Player import *

class PlayerPiece:

    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.coordinates = []
        self.status = 'start'
        self.total_spaces_moved = 0

    def move_piece(self, move_by=0):
        self.total_spaces_moved += move_by
        # test print # print(f"Moving {self.color}'s number {self.name} piece {move_by} space(s)\n")
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

    def home_run(self):
        self.status = 'home'
