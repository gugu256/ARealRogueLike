import os
import msvcrt

# player class
class player:
    hp = 20
    inv = []

    def show_inv():
        print("INVENTORY\n=========")
        a = 0
        for i in player.inv:
              print(f"Slot{a+1} : {i}")
        input("")

    def add_item(item):
        player.inv.append(item)
        print("Player obtained {item}")

    def rmv_item(item):
        player.inv.pop(item)
        print("Removed {item} from the inventory")

# Create the player
last_char = ""
player_y, player_x = 2, 2
char = "¤"

dungeon = open("dungeon.dng", "r").read().splitlines()

def clear_screen():
    os.system('cls')

def get_key():
    return msvcrt.getch().decode('utf-8').lower()

def main():
    global player_x, player_y, player, last_char

    while True:
        clear_screen()

        # Draw the dungeon
        for row in dungeon:
            print(row.replace("#", "█"))
            #print(row)

        # Clear the previous position of the player
        dungeon[player_y] = dungeon[player_y][:player_x] + last_char + dungeon[player_y][player_x + 1:]

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
        elif key == 'i':
            player.show_inv()

        # Update the new position of the player
        last_char = dungeon[player_y][player_x]
        if last_char == "": last_char = " "
        dungeon[player_y] = dungeon[player_y][:player_x] + char + dungeon[player_y][player_x + 1:]
        
main()