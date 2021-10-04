def choose_action_message(player):
    print(f"{player.capitalize()} player turn, choose action.\n1 - Move hero.\n2 - Place the wall.")


def move_player_message():
    print("Choose action:\nChoose coordinates from list below or type 'back' for returning to choosing between moving "
          "hero or placing wall")


def print_places_to_move(places_to_move):
    counter = 1
    for place in places_to_move:
        print(f"{counter} - {place}")
        counter += 1


def wrong_action_message():
    print("You entered wrong action")


def place_the_wall_message():
    print("Enter wall start coordinates and end coordinates(like '0 1 2 1') or type 'back' for returning to choosing "
          "between moving hero or placing wall")


def win_message(win_status):
    print(f"{win_status['player'].capitalize()} won. Do you want to play again(type yes for playing again).")
