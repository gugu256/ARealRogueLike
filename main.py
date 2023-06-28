import os
import msvcrt
import random



def clear_screen():
    os.system('cls')

# player class
class player:
    hp = 20
    inv = []
    class attacks:
        names = {"lick": [3, 100], "bite":  [5, 90], "punch": [10, 60], "gigashoot": [50, 20]}

    def show_inv():
        print("INVENTORY\n=========")
        a = 0
        for i in player.inv:
              print(f"Slot {a+1} : {i}")
              a+=1
        input("")

    def add_item(item):
        player.inv.append(item)

    def rmv_item(item):
        player.inv.pop(item)
        print("Removed {item} from the inventory")

def fight(enemyHP: int, enemyATK: list, enemyName: str, msg: list, loot: list):
    monsterHP = enemyHP
    clear_screen()
    print(f"You encountered a {enemyName.upper()} !\n{enemyName.upper()}: '{random.choice(msg)}' !")
    input("\nPress enter to continue.")
    won = False
    over = False
    while over is False:
        clear_screen()
        print(f"STATS:\nYour HP : {player.hp}\n{enemyName}'s HP : {monsterHP}")
        print("\nYour turn!\n")
        for i in player.attacks.names:
            print(i, ": ", player.attacks.names[i][0], " DMG, ", player.attacks.names[i][1], "% chance")
            choice = None
        while choice not in player.attacks.names:

            choice = input("\n > ")


        randomize = random.randint(1, 100)

        if randomize > player.attacks.names[choice][1]:
            input("\n Attack failed!")
            

        else:
            monsterHP -= player.attacks.names[choice][0]
            input(f"\n You dealt {player.attacks.names[choice][0]} damages to {enemyName} !\n They now have {monsterHP} HP !")


        if monsterHP <= 0:
            print(f"\nThe {enemyName.upper()} died!\n")
            print("You obtained :")
            for item in range(0, len(loot)):
                print(f"{loot[item][1]} {loot[item][0]}")
                i = loot[item][1]
                while i > 0:
                    player.add_item(loot[item][0])
                    i-=1
            input("\nPress enter to continue.")
            over = True
            won = True
            break

        clear_screen()

        print(f"STATS:\nYour HP : {player.hp}\n{enemyName}'s HP : {monsterHP}")

        print(f"\n{enemyName.upper()}'s turn !")
        if random.randint(0, 1) == 1: print(random.choice(msg))

        atk = random.randint(enemyATK[0], enemyATK[1])
        player.hp -= atk
        input(f"\n {enemyName.upper()} dealt you {atk} damages !\nYou now have {player.hp} HP !")

        if player.hp <= 0:
            print(f"You died...")
            input("\nPress enter to continue.")

            over = True
            won = False
    
    return won

def extract(path):
    hp = int(open(path + "/HP", "r").read())
    atk = [int(open(path + "/ATK0", "r").read()), int(open(path + "/ATK1", "r").read())]
    name = open(path + "/name", "r").read()
    msgs = open(path + "/msg", "r").read().splitlines()
    loot_final = []
    items = open(path + "/loot", "r").read().splitlines()
    quants = open(path + "/lootnbr", "r").read().splitlines()
    for i in range(0, len(quants)):
        quants[i] = int(quants[i])
    for j in range(0, len(items)):
        loot_final.append((items[j], quants[j]))
    f = fight(hp, atk, name, msgs, loot_final)
    if f:
        return True
    else:
        return False

def die():
    clear_screen()
    print("G A M E     O V E R")
    print("\nSeems like you died. Oops")
    input("Press enter to quit./")
    quit()

def opendung(path):
    global dungeon, ingame, player_y, player_x, current_dung
    if path == current_dung:
        pass
    else:
        current_dung = path
        player_y, player_x = 2, 2
        clear_screen()
        dungeon = open(path, "r").read().splitlines()
        for row in range(len(dungeon)):
            dungeon[row] = dungeon[row].replace("#", "█").replace("u", " ").replace("d", "")
    
    

# Create the player
last_char = ""
player_y, player_x = 2, 2
char =  "@"

current_dung = ""
dungeon = []

opendung("dungeon/center.dng")


def get_key():
    return msvcrt.getch().decode('utf-8').lower()

def main():
    global player_x, player_y, player, last_char, dungeon
    possible_chars = []
    possible_chars += " █⮘⮙⮚⮛"

    while True:
        clear_screen()

        # Draw the dungeon
        for row in dungeon:
            print(row)

        # Clear the previous position of the player
        dungeon[player_y] = dungeon[player_y][:player_x] + last_char + dungeon[player_y][player_x + 1:]

        # Get user input
        key = get_key()

        # Process user input
        if key == 'z' and dungeon[player_y - 1][player_x] != '█':
            player_y -= 1
        elif key == 's' and dungeon[player_y + 1][player_x] != '█':
            player_y += 1
        elif key == 'q' and dungeon[player_y][player_x - 1] != '█':
            player_x -= 1
        elif key == 'd' and dungeon[player_y][player_x + 1] != '█':
            player_x += 1
        elif key == 'i':
            player.show_inv()
        
        if dungeon[player_y][player_x] not in possible_chars:
            f = extract("monsters/" + dungeon[player_y][player_x])
            if f:
                dungeon[player_y] = dungeon[player_y].replace(dungeon[player_y][player_x], " ")
            else:
                die()
            
        # Update the new position of the player
        last_char = dungeon[player_y][player_x]
        if last_char == "": last_char = " "
        dungeon[player_y] = dungeon[player_y][:player_x] + char + dungeon[player_y][player_x + 1:]

main()