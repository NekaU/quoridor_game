from Coordinate import Coordinate


class Player:
    def __init__(self, player_type, player_number):
        self.player_type = player_type  # True - Player, False - computer
        self.player_number = player_number  # int
        self.walls_amount = 10
        self.current_position = self._set_start_position()
        self.next_position = None
        self.can_move_here = None
        self.places_to_move = None
        if self.player_number == 2:
            self._forWin = [[16, 0], [16, 2], [16, 4], [16, 6], [16, 8], [16, 10], [16, 12], [16, 14], [16, 16]]
        else:
            self._forWin = [[0, 0], [0, 2], [0, 4], [0, 6], [0, 8], [0, 10], [0, 12], [0, 14], [0, 16]]

    def isWin(self):
        if self.player_number == 1:
            if self.current_position.x == 0:
                return True
        if self.player_number == 2:
            if self.current_position.x == 16:
                return True
        return False

    def _set_start_position(self):
        return Coordinate(16, 8) if self.player_number == 1 else Coordinate(0, 8)

    def decrease_wall_amount(self):
        if self.walls_amount != 0:
            self.walls_amount -= 1

    def set_places_to_move(self, game_field, list_of_players=None, list_of_possible_moves=None, anotherPlayer=None,
                           flag=False):
        if flag == False:
            if self.player_number == list_of_players[0].player_number:
                anotherPlayer = list_of_players[1]
            else:
                anotherPlayer = list_of_players[0]
        if flag == False:
            list_of_possible_moves = []
        if self.current_position.x - 2 >= 0:  # UP
            if self.check_up(game_field.field):
                if not self.player_check_up(game_field.field, anotherPlayer.current_position):
                    list_of_possible_moves.append(self.up())
                elif flag is False:
                    list_of_possible_moves = anotherPlayer.set_places_to_move(game_field,
                                                                              list_of_possible_moves=list_of_possible_moves,
                                                                              anotherPlayer=self, flag=True)
        if self.current_position.y + 2 <= 16:  # RIGHT
            if self.check_right(game_field.field):
                if not self.player_check_right(game_field.field, anotherPlayer.current_position):
                    list_of_possible_moves.append(self.right())
                elif flag is False:
                    list_of_possible_moves = anotherPlayer.set_places_to_move(game_field,
                                                                              list_of_possible_moves=list_of_possible_moves,
                                                                              anotherPlayer=self, flag=True)
        if self.current_position.x + 2 <= 16:  # DOWN
            if self.check_down(game_field.field):
                if not self.player_check_down(game_field.field, anotherPlayer.current_position):
                    list_of_possible_moves.append(self.down())
                elif flag is False:
                    list_of_possible_moves = anotherPlayer.set_places_to_move(game_field,
                                                                              list_of_possible_moves=list_of_possible_moves,
                                                                              anotherPlayer=self, flag=True)
        if self.current_position.y - 2 >= 0:  # LEFT
            if self.check_left(game_field.field):
                if not self.player_check_left(game_field.field, anotherPlayer.current_position):
                    list_of_possible_moves.append(self.left())
                elif flag is False:
                    list_of_possible_moves = anotherPlayer.set_places_to_move(game_field,
                                                                              list_of_possible_moves=list_of_possible_moves,
                                                                              anotherPlayer=self, flag=True)
        self.places_to_move = list_of_possible_moves
        return list_of_possible_moves

    def set_next_position(self, coordinate):
        if coordinate.is_correct and coordinate in self.places_to_move:
            self.next_position = coordinate
            self.can_move_here = True
        else:
            self.next_position = None
            self.can_move_here = False

    def up(self):
        return Coordinate(self.current_position.x - 2, self.current_position.y)

    def down(self):
        return Coordinate(self.current_position.x + 2, self.current_position.y)

    def left(self):
        return Coordinate(self.current_position.x, self.current_position.y - 2)

    def right(self):
        return Coordinate(self.current_position.x, self.current_position.y + 2)

    def check_up(self, field):
        return True if field[self.current_position.x - 1][self.current_position.y] == 3 else False

    def check_down(self, field):
        return True if field[self.current_position.x + 1][self.current_position.y] == 3 else False

    def check_right(self, field):
        return True if field[self.current_position.x][self.current_position.y + 1] == 3 else False

    def check_left(self, field):
        return True if field[self.current_position.x][self.current_position.y - 1] == 3 else False

    def player_check_up(self, field, secPlayer):
        if self.current_position.x - 2 == secPlayer.x and self.current_position.y == secPlayer.y:
            return True
        return False

    def player_check_down(self, field, secPlayer):
        if self.current_position.x + 2 == secPlayer.x and self.current_position.y == secPlayer.y:
            return True
        return False

    def player_check_right(self, field, secPlayer):
        if self.current_position.x == secPlayer.x and self.current_position.y + 2 == secPlayer.y:
            return True
        return False

    def player_check_left(self, field, secPlayer):
        if self.current_position.x == secPlayer.x and self.current_position.y - 2 == secPlayer.y:
            return True
        return False

    @property
    def forWin(self):
        return self._forWin

# player = Player(True, 1)
#
# for i in player.forWin:
#     # print(i[0])
#     # print(i[1])
#
# # print(f"x-{player.current_position.x} y-{player.current_position.y}")
# # print(player.next_position)
