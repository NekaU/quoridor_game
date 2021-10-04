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
    if coordinates[0] == 0 and coordinates[1] != 0 and coordinates[1] != 16:
        if field[coordinates[0]][coordinates[1]+1] == 3:
            places_to_move_list.append([coordinates[0], coordinates[1]+2])
        if field[coordinates[0]][coordinates[1]-1] == 3:
            places_to_move_list.append([coordinates[0], coordinates[1]-2])
        if field[coordinates[0]+1][coordinates[1]] == 3:
            places_to_move_list.append([coordinates[0]+2, coordinates[1]])
    elif coordinates[0] == 16 and coordinates[1] != 0 and coordinates[1] != 16:
        if field[coordinates[0]][coordinates[1]+1] == 3:
            places_to_move_list.append([coordinates[0], coordinates[1]+2])
        if field[coordinates[0]][coordinates[1]-1] == 3:
            places_to_move_list.append([coordinates[0], coordinates[1]-2])
        if field[coordinates[0]-1][coordinates[1]] == 3:
            places_to_move_list.append([coordinates[0]-2, coordinates[1]])
    elif coordinates[0] == 0 and coordinates[1] == 0:
        if field[coordinates[0]+1][coordinates[1]] == 3:
            places_to_move_list.append(up(coordinates[0], coordinates[1]))
        if 
    # elif coordinates[1] != 0 and coordinates[1] != 16:
    #     if field[coordinates[0]][coordinates[1]+1] == 3:
    #         places_to_move_list.append([coordinates[0], coordinates[1]+2])
    #     if field[coordinates[0]][coordinates[1]-1] == 3:
    #         places_to_move_list.append([coordinates[0], coordinates[1]-2])
    #     if field[coordinates[0]-1][coordinates[1]] == 3:
    #         places_to_move_list.append([coordinates[0]-2, coordinates[1]])
    #     if field[coordinates[0]+1][coordinates[1]] == 3:
    #         places_to_move_list.append([coordinates[0]+2, coordinates[1]])
    # elif coordinates[1] == 0:
    #     if field[coordinates[0]][coordinates[1]+1] == 3:
    #         places_to_move_list.append([coordinates[0], coordinates[1]+2])
    #     if field[coordinates[0]+1][coordinates[1]] == 3:
    #         places_to_move_list.append([coordinates[0]+2, coordinates[1]])
    #     if field[coordinates[0]-1][coordinates[1]] == 3:
    #         places_to_move_list.append([coordinates[0]-2, coordinates[1]])
    # elif coordinates[1] == 16:
    #     if field[coordinates[0]][coordinates[1]-1] == 3:
    #         places_to_move_list.append([coordinates[0], coordinates[1]+2])
    #     if field[coordinates[0]+1][coordinates[1]] == 3:
    #         places_to_move_list.append([coordinates[0]+2, coordinates[1]])
    #     if field[coordinates[0]-1][coordinates[1]] == 3:
    #         places_to_move_list.append([coordinates[0]-2, coordinates[1]])
    return places_to_move_list


def up(i, j):
    return [i-2, j]


def down(i, j):
    return [i+2, j]


def left(i, j):
    return [i, j-2]


def right(i, j):
    return [i, j+2]


# print(places_to_move(field_preparation(fill_the_field()), "first"))
# print(places_to_move(field_preparation(fill_the_field()), "second"))
