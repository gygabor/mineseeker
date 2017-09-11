import random
from letters_of_map import letters

def start():
    map_height = 5
    map_width = 5
    mine_count = 10

    game_map = create_map(map_height, map_width)
    map_letters = letters[:len(game_map[0])]
    mines_positions = create_mines(mine_count, map_height, map_width)
    game_controller(game_map, mines_positions, map_letters)

def create_map(map_height, map_width):
    map_array = []
    for i in range(map_height):
        map_row = []
        for j in range(map_width):
            map_row.append('X')
        map_array.append(map_row)
    return map_array

def create_mines(mine_count, map_height, map_width):
    mines_positions = []
    while mine_count > 0:
        mine_position = [random.randrange(0, map_width), random.randrange(0, map_height)]
        if not mine_position in mines_positions:
            mines_positions.append(mine_position)
            mine_count -= 1
    return mines_positions

def game_controller(game_map, mines_positions, map_letters):
    player_is_alive = True
    print_map(game_map, map_letters)

    while player_is_alive:
        player_guess = get_player_guess(len(game_map), map_letters)
        if player_guess in mines_positions:
            print("You are dead")
            game_map = show_end_result(game_map, mines_positions, player_guess)
            player_is_alive = False
        else:
            calculate_mines_nearby()
        print_map(game_map, map_letters)

def print_map(game_map, map_letters):
    print("X", map_letters)
    for i in range(len(game_map)):
        print(i, game_map[i])

def get_player_guess(map_height, map_letters):
    right_guess = False
    while not right_guess:
        guessY = input("Give the Y position (e.g. \"C\"): ")
        guessX = int(input("Give the X position (e.g. 2): "))
        if not guessY in map_letters:
            print("The Y position should be between:", map_letters)
        elif guessX < 0 or guessX > map_height:
            print("The X position should be between: 0-" + str(map_height))
        else:
            right_guess = True
    return [map_letters.index(guessY), guessX]

def show_end_result(game_map, mines_positions, player_guess):
    for position in mines_positions:
        game_map[position[0]][position[1]] = "O"
    game_map[player_guess[0]][player_guess[1]] = "!"
    return game_map

def calculate_mines_nearby():
    pass

start()
