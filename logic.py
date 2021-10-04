from field import get_connected_points, field_preparation, fill_the_field, found_players, print_field
from graph import create_nodes_from_field, update_connections_from_field, create_graph
from messages import choose_action_message, move_player_message, print_places_to_move, wrong_action_message, \
    place_the_wall_message, win_message
from move import move_player, places_to_move
from utils import clear_console
from walls import set_wall, check_if_it_wall


def check_for_win(field):
    answer = {"win": False, "who": ''}
    players = found_players(field)
    if players["first"][0] == 0:
        answer["win"] = True
        answer["who"] = 'First'
    if players["second"][0] == 16:
        answer["win"] = True
        answer["who"] = 'Second'
    return answer


def move_player_action(data, player):
    clear_console()
    final_field = data['field']
    print_field(final_field)
    move_player_message()
    places = places_to_move(data['field'], player)
    print_places_to_move(places)
    move_player_input = input()
    try:
        if move_player_input == 'back':
            choose_action_input(data, player)
        elif int(move_player_input) in range(1, len(places) + 1):
            move_player_result = move_player(data['field'], player, places[int(move_player_input) - 1])
            # print(move_player_result['field'])
            data['field'] = move_player_result['field']
            data['result'] = move_player_result['result']
            return data
        else:
            wrong_action_message()
            move_player_action(data, player)

    except Exception:
        wrong_action_message()
        move_player_action(data, player)


def place_the_wall_action(data, player):
    clear_console()
    final_field = data['field']
    print_field(final_field)
    place_the_wall_message()
    wall_input = input()
    if wall_input == 'back':
        choose_action_input(data, player)
    elif wall_input == '':
        wrong_action_message()
        place_the_wall_action(data, player)
    else:
        coordinates_split = wall_input.split(' ')
        # print(coordinates_split)
        # print(len(coordinates_split))
        if len(coordinates_split) == 4:
            try:
                # print([int(coordinate) for coordinate in coordinates_split])
                coordinates = [int(coordinate) for coordinate in coordinates_split]
                start_wall = [coordinates[0], coordinates[1]]
                end_wall = [coordinates[2], coordinates[3]]
                # print(check_if_it_wall(start_wall, end_wall))
                if check_if_it_wall(start_wall, end_wall):
                    # print(data)
                    data = set_wall(data, start_wall, end_wall)
                    if data['result']:
                        return data['data']
                    else:
                        wrong_action_message()
                        place_the_wall_action(data, player)
                else:
                    wrong_action_message()
                    place_the_wall_action(data, player)
            except Exception as e:
                wrong_action_message()
                place_the_wall_action(data, player)
        else:
            wrong_action_message()
            place_the_wall_action(data, player)


def choose_action_input(data, player):
    clear_console()
    final_field = data['field']
    print_field(final_field)
    choose_action_message(player)
    action_input = input()
    if action_input == "1":
        return move_player_action(data, player)
    elif action_input == "2":
        return place_the_wall_action(data, player)
    else:
        wrong_action_message()
        choose_action_input(data, player)


def start_game():
    clear_console()
    field = field_preparation(fill_the_field())
    nodes = create_nodes_from_field(field)
    graph = update_connections_from_field(get_connected_points(field), create_graph(nodes), nodes)
    data = {'field': field, 'nodes': nodes, 'graph': graph}
    win_status = check_for_win(field)
    players = ['first', 'second']
    counter = 0
    final_field = field_preparation(field)
    print_field(final_field)
    while not win_status['win']:
        data = choose_action_input(data, players[counter])
        win_status = check_for_win(data['field'])
        if counter == 0:
            counter += 1
        else:
            counter -= 1
    win_message(win_status)
    play_again_input = input()
    if play_again_input == 'yes':
        start_game()



start_game()
