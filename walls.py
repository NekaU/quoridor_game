from graph import if_there_path_to_win


def check_if_it_wall(start_wall, end_wall):
    if start_wall[0] == end_wall[0]:
        if start_wall[1] > end_wall[1]:
            return True if len([num for num in range(end_wall[1]+1, start_wall[1])]) == 1 else False
        else:
            return True if len([num for num in range(start_wall[1]+1, end_wall[1])]) == 1 else False
    elif start_wall[1] == end_wall[1]:
        if start_wall[0] > end_wall[0]:
            return True if len([num for num in range(end_wall[0]+1, start_wall[0])]) == 1 else False
        else:
            return True if len([num for num in range(start_wall[0]+1, end_wall[0])]) == 1 else False
    else:
        return False


def set_wall(data, start_wall, end_wall):
    answer = {"data": data, "result": False}
    middle_wall = []
    if start_wall[1] == end_wall[1]:
        if start_wall[0] > end_wall[0]:
            middle_wall.append(end_wall[0]+1)
            middle_wall.append(start_wall[1])
        else:
            middle_wall.append(start_wall[0]+1)
            middle_wall.append(start_wall[1])
    else:
        if start_wall[1] > end_wall[1]:
            middle_wall.append(start_wall[0])
            middle_wall.append(end_wall[1]+1)
        else:
            middle_wall.append(start_wall[0])
            middle_wall.append(start_wall[1]+1)
    # print(middle_wall)
    # print(answer['data']['field'][start_wall[0]][start_wall[1]])
    # print(answer['data']['field'][middle_wall[0]][middle_wall[1]])
    # print(answer['data']['field'][end_wall[0]][end_wall[1]])
    if answer['data']['field'][start_wall[0]][start_wall[1]] == 3 and answer['data']['field'][end_wall[0]][end_wall[1]] == 3 \
            and answer['data']['field'][middle_wall[0]][middle_wall[1]] == 3:
        path_to_win = if_there_path_to_win(data)
        if path_to_win:
            answer['data']['field'][start_wall[0]][start_wall[1]] = 4
            answer['data']['field'][middle_wall[0]][middle_wall[1]] = 4
            answer['data']['field'][end_wall[0]][end_wall[1]] = 4
            answer["result"] = True
            # print(answer)
    return answer


# def found_walls_around_player(field):
#     players = found_players(field)
#     coordinates_first = [backwards_calculating_point(players['first'][0]),
#                          backwards_calculating_point(players['first'][1])]
#     coordinates_second = [backwards_calculating_point(players['second'][0]),
#                           backwards_calculating_point(players['second'][1])]
#     answer = {"first": [], "second": []}
#     if coordinates_first[0] == 0 and coordinates_first[1] != 0 and coordinates_first[1] != 16:
#         if field[0][coordinates_first[1]+1] == 3:
#             pass
