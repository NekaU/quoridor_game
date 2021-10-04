from field import found_players


def move_player(field, player, coordinate):
    players = found_players(field)
    answer = {"field": field, "result": False}
    if player == 'first':
        field[players[player][0]][players[player][1]] = 0
        field[coordinate[0]][coordinate[1]] = 1
        answer['field'] = field
        answer['result'] = True
    elif player == 'second':
        field[players[player][0]][players[player][1]] = 0
        field[coordinate[0]][coordinate[1]] = 2
        answer['field'] = field
        answer['result'] = True
    return answer


def places_to_move(field, player):
    players = found_players(field)
    places_to_move_list = []
    coordinates = [players[player][0], players[player][1]]
    if coordinates[0] == 0 and 0 < coordinates[1] < 16:
        if check_right(field, coordinates):
            places_to_move_list.append(right(coordinates))
        if check_left(field, coordinates):
            places_to_move_list.append(left(coordinates))
        if check_down(field, coordinates):
            places_to_move_list.append(down(coordinates))
    elif coordinates[0] == 16 and 0 < coordinates[1] < 16:
        if check_right(field, coordinates):
            places_to_move_list.append(right(coordinates))
        if check_left(field, coordinates):
            places_to_move_list.append(left(coordinates))
        if check_up(field, coordinates):
            places_to_move_list.append(up(coordinates))
    elif coordinates[0] == 0 and coordinates[1] == 0:
        if check_up(field, coordinates):
            places_to_move_list.append(up(coordinates))
        if check_right(field, coordinates):
            places_to_move_list.append(right(coordinates))
    elif coordinates[0] == 0 and coordinates[1] == 16:
        if check_up(field, coordinates):
            places_to_move_list.append(up(coordinates))
        if check_left(field, coordinates):
            places_to_move_list.append(left(coordinates))
    elif coordinates[0] == 16 and coordinates[1] == 0:
        if check_down(field, coordinates):
            places_to_move_list.append(down(coordinates))
        if check_right(field, coordinates):
            places_to_move_list.append(right(coordinates))
    elif coordinates[0] == 16 and coordinates[1] == 16:
        if check_up(field, coordinates):
            places_to_move_list.append(up(coordinates))
        if check_left(field, coordinates):
            places_to_move_list.append(left(coordinates))
    elif 0 < coordinates[0] < 16 and coordinates[1] == 16:
        if check_down(field, coordinates):
            places_to_move_list.append(down(coordinates))
        if check_up(field, coordinates):
            places_to_move_list.append(up(coordinates))
        if check_left(field, coordinates):
            places_to_move_list.append(left(coordinates))
    elif 0 < coordinates[0] < 16 and coordinates[1] == 0:
        if check_down(field, coordinates):
            places_to_move_list.append(down(coordinates))
        if check_up(field, coordinates):
            places_to_move_list.append(up(coordinates))
        if check_right(field, coordinates):
            places_to_move_list.append(right(coordinates))
    elif 0 < coordinates[0] < 16 and 0 < coordinates[1] < 16:
        if check_down(field, coordinates):
            places_to_move_list.append(down(coordinates))
        if check_up(field, coordinates):
            places_to_move_list.append(up(coordinates))
        if check_right(field, coordinates):
            places_to_move_list.append(right(coordinates))
        if check_left(field, coordinates):
            places_to_move_list.append(left(coordinates))
    return places_to_move_list


def up(coordinates):
    return [coordinates[0]-2, coordinates[1]]


def down(coordinates):
    return [coordinates[0]+2, coordinates[1]]


def left(coordinates):
    return [coordinates[0], coordinates[1]-2]


def right(coordinates):
    return [coordinates[0], coordinates[1]+2]


def check_up(field, coordinates):
    return True if field[coordinates[0]-1][coordinates[1]] == 3 else False


def check_down(field, coordinates):
    return True if field[coordinates[0]+1][coordinates[1]] == 3 else False


def check_right(field, coordinates):
    return True if field[coordinates[0]][coordinates[1]+1] == 3 else False


def check_left(field, coordinates):
    return True if field[coordinates[0]][coordinates[1]-1] == 3 else False

# print(places_to_move(field_preparation(fill_the_field()), "first"))
# print(places_to_move(field_preparation(fill_the_field()), "second"))
