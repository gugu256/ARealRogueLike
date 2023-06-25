import os
import msvcrt

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key():
    return msvcrt.getch().decode('utf-8').lower()

def main():
    # Create the player
    player = '¤'
    player_y, player_x = 1, 1

    # Create the dungeon
    dungeon = [
        "############",
        "#..........############",
        "#..........           ",
        "#..........###########",
        "#..........#",
        "############"
    ]

    while True:
        clear_screen()

        # Draw the dungeon
        for row in dungeon:
            print(row)

        # Clear the previous position of the player
        dungeon[player_y] = dungeon[player_y][:player_x] + '.' + dungeon[player_y][player_x + 1:]

        # Get user input
        key = get_key()

        # Process user input
        if key == 'z' and dungeon[player_y - 1][player_x] != '#':
            player_y -= 1
        elif key == 's' and dungeon[player_y + 1][player_x] != '#':
            player_y += 1
        elif key == 'q' and dungeon[player_y][player_x - 1] != '#':
            player_x -= 1
        elif key == 'd' and dungeon[player_y][player_x + 1] != '#':
            player_x += 1
        elif key == '_':
            break

        # Update the new position of the player
        dungeon[player_y] = dungeon[player_y][:player_x] + player + dungeon[player_y][player_x + 1:]

if __name__ == '__main__':
    main()
