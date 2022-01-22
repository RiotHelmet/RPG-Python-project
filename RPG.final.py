from cmath import sqrt
import random as rand
import math
import time
import sys

MonsterTypes = ["Ogre", "Skeleton", "Dragon", "Boss"]


location_list = ["Trasmoz", "Bariw", "Istmina", "Bezouce", "Irara", "Quesnel", "Norheimsund", "Ram Ranch", "Desmus"]
weapon_type = ["Sword", "Dagger", "Spear", "Mallet", "Hammer", "Axe"]
first_word = ["Great", "Flawed", "Burning", "Moonlight", "Rock Hard", "Black", "Devoid of any meaning", "Short", "Long", "Huge", "Tiny", "Slightly Bent Left", "Gösta's long lost", "Gargoyle", "Enchanted", "Heavy", "Light"]

write_speed = 0.1
def write(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(write_speed)
    print("")

def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

class Enemy(object):
    Health = int()
    Attack = int()
    Loot = []
    Xp = int()
    Mana = 0 < int() < 100
    Type = str()
    IsShielding = bool

class PlayerClass(object):
    Health = int()
    Attack = int()
    Inventory = []
    Level = 1
    Xp = int()
    Mana = 0 < int() < 100
    IsShielding = bool
    gold = int()
    game_test_mode = bool
    current_damage = int()

player = PlayerClass()
player.Health = 1000
player.Attack = 300
player.Mana = 30

Fighting = False
FightHistoryPlayer = [] 
FightHistoryEnemy = []

class Weapon(object):
    Description = str("")
    Attack_Bonus = int()
    list = []
    is_equiped = bool

class Armor(object):
    Description = str("")
    Health_Bonus = int()
    list = []


class Potion(object):
    Description = str("")
    Attack_Bonus = int()
    Health_Bonus = int()
    list = []

hot_potion = Potion()
hot_potion.name = "test_potion"
hot_potion.Health_Bonus = 1
hot_potion.Attack_Bonus = 1.2
player.Inventory.append(hot_potion)
Potion.list.append(hot_potion)

# -------------------------------- Item List -------------------

broken_sword = Weapon()
broken_sword.Attack_Bonus = 1
Weapon.list.append(broken_sword)

not_so_broken_sword = Weapon()
not_so_broken_sword.Attack_Bonus = 1.1
Weapon.list.append(not_so_broken_sword)

artins_kebabspätt = Weapon()
artins_kebabspätt.name = f"Artin's Kebabspätt  -  ( + {100 * (artins_kebabspätt.Attack_Bonus - 1)}% damage)"
artins_kebabspätt.Attack_Bonus = 2
Weapon.list.append(artins_kebabspätt.name)



bastard_bagua = Weapon()
bastard_bagua.Attack_Bonus = 5
Weapon.list.append(bastard_bagua)

def Spawn_Enemy(type, difficulty):
    Current_Enemy = Enemy()
    Current_Enemy.Type = type
    if Current_Enemy.Type == "Ogre":
        Current_Enemy.Health = int((math.sqrt(difficulty) * 1000))
        Current_Enemy.Attack = (math.sqrt(difficulty) * 150)
        Current_Enemy.Xp = (difficulty * 100)
        Current_Enemy.Mana = 50
        Current_Enemy.Loot = []
        Current_Enemy.IsShielding = False
        Current_Enemy.tier = difficulty
    elif Current_Enemy.Type == "Skeleton":
        Current_Enemy.Health = int((math.sqrt(difficulty) * 750))
        Current_Enemy.Attack = (math.sqrt(difficulty) * 225)
        Current_Enemy.Xp = (difficulty * 100)
        Current_Enemy.Mana = 50
        Current_Enemy.Loot = []
        Current_Enemy.IsShielding = False
    return Current_Enemy, Current_Enemy.Health, Current_Enemy.Attack, Current_Enemy.Xp, Current_Enemy.Mana, Current_Enemy.Loot, Current_Enemy.IsShielding
# Current_Enemy, Current_Enemy.Health, Current_Enemy.Attack, Current_Enemy.Xp, Current_Enemy.Mana, Current_Enemy.Loot, Current_Enemy.IsShielding = Spawn_Enemy("Ogre", 1)

def random_weapon(tier):
    location = location_list[rand.randint(0, 8)]
    weapon = weapon_type[rand.randint(0, 5)]
    strength = round((rand.uniform((math.sqrt(math.sqrt(tier))), (math.sqrt(tier) + 0.2))), 3)
    name = (f"{first_word[rand.randint(0, 16)]} {weapon} of {location}  -  ( + {round(100 * (strength - 1), 3)}% damage)")
    description = (f"A handcrafted {weapon} from the regions of {location}. Created through hard work and dedication by some of {location}'s finest blacksmiths. This weapon carries the strength power of {strength}")
    
    item = Weapon()
    item.Attack_Bonus = strength
    item.Description = description
    item.name = name
    Weapon.list.append(item.name)   
    return item


def show_inventory(y):
    clear()
    print(f"Your bag contains: \n\n - {player.gold} gold")
    for x in player.Inventory:
        if x.name in Weapon.list:
            if x.is_equiped == True:
                print(f" {player.Inventory.index(x) + 1}. {x.name} - Equiped")
            else:
                print(f" {player.Inventory.index(x) + 1}. {x.name}")
        else:
            print(f" {player.Inventory.index(x) + 1}. {x.name}")
    print("\n\n")
    if y == 2:
        temp_val = input("Do you wish to manage your inventory? Y/N -> ").lower()
        if temp_val == "y":
            print("\n\n\n")
            manage_inventory(2)


def loot(enemy_tier):
    gold = round((rand.uniform(((enemy_tier * 10) - 5), ((enemy_tier * 10) + 5))), 1)
    temp_val = rand.randint(0, 1)
    if player.game_test_mode == True:
        temp_val = 1
    player.Xp += Current_Enemy.Xp
    if player.Xp > 10000:
        player.Level = 10
    elif player.Xp > 7000:
        player.Level = 9
    elif player.Xp > 5000:
        player.Level = 8
    elif player.Xp > 3400:
        player.Level = 7
    elif player.Xp > 2400:
        player.Level = 6
    elif player.Xp > 1500:
        player.Level = 5
    elif player.Xp > 700:
        player.Level = 4
    elif player.Xp > 300:
        player.Level = 3
    elif player.Xp > 100:
        player.Level = 2
    elif player.Xp > 0:
        player.Level = 1
    if temp_val == 1:
        item = random_weapon(Current_Enemy.tier)
        # item.name, item.strength, item.description = random_weapon(Current_Enemy.tier)
    if temp_val == 1:
        clear()
        write(f"\n\n\n\nYou have slain the ferocious beast. \n\n The enemy dropped:\n - {gold} gold\n - {item.name}\n")
        input()
        while True:
            temp_val2 = input(f"\nDo you wish to loot the {item.name} Y/N -->  ").lower()
            player.gold += gold
            if temp_val2 == "y":
                if len(player.Inventory) < 4:
                    player.Inventory.append(item)
                    break
                else:
                    temp_val2 = input("Your inventory is full, do you want to manage it? Y/N -> ").lower()
                    if temp_val2 == "y":
                        manage_inventory(1)
            elif temp_val2 == "n":
                break
            else:
                break
    else:
        write(f"You have slain the ferocious beast.")
        print(f"\n The enemy dropped: \n - {gold} gold\n")
        input()
        player.gold += gold

def manage_inventory(y):
    clear()
    if y == 1:
        show_inventory(1)
    while True:
        show_inventory(1)
        temp_val = input("What do you want to do?\n\n 1. Drop an Item\n 2. Equip an item\n 3. Cancel\n\n")
        if temp_val == "1":
            while True:
                temp_val2 = int(input("Which item do you want to drop? (0 to cancel) -> "))
                if temp_val2 == 0:
                    break
                try:
                    temp_var = player.Inventory[temp_val2 - 1]
                    print(f"You dropped: {temp_var.name}")
                    player.Inventory.pop(temp_val2 - 1)
                    manage_inventory(1)
                    break
                except:
                    print("Specified Item doesnt exist, try again!")
                    input()
            break
        elif temp_val == "2":
            show_inventory(1)
            while True:
                try:
                    temp_val2 = int(input("Which item do you want to equip? -> "))
                    if player.Inventory[temp_val2 - 1].name in Weapon.list:
                        for x in player.Inventory:
                            x.is_equiped = False
                        player.Inventory[temp_val2 - 1].is_equiped = True
                        manage_inventory(1)
                        break
                    elif temp_val2 == 0:
                        break
                    else:
                        print("You cant equip this item (Type 0 to cancel)")
                        input()
                except:
                    print("Specified Item doesnt exist, try again!")
                    input()
            break
        elif temp_val == "3":
            break
        else:
            print("You need to pick a valid number, try again!")
            input()


def Enemy_Turn(Mana):
    enemy_attack = ""
    if Mana < 26:
        enemy_attack = "Shield"
    elif 25 < Mana < 51:
        choice = rand.randint(0,2)
        print(choice)
        if choice == 0:
            enemy_attack = "Shield"
        else:
            enemy_attack = "Light"
    elif 50 < Mana:
        choice = rand.randint(0,5)
        print(choice)
        if choice < 3:
            enemy_attack = "Heavy"
        elif 2 < choice <5:
            enemy_attack = "Light"
        else:
            enemy_attack = "Shield"
    return enemy_attack

def Fighting():
    player.IsAlive = True
    player.Mana = 30
    if player.game_test_mode == True:
        player.Health = round((1000000 * math.sqrt(player.Level) + 300), 3)
    else:
        player.Health = round((1000 * math.sqrt(player.Level) + 300), 3)
    Current_Enemy.IsAlive = True
    winner = ""
    Fighting = True
    loot = Current_Enemy.Loot
    clear()
    print(f"\nYou encountered an {Current_Enemy.Type}!\n")
    input()
    if player.game_test_mode == True:
        player.Attack = 100000
    else:
        player.Attack = 300
    for x in player.Inventory:
        if x.name in Weapon.list:
            if x.is_equiped == True:
                player.Attack = player.Attack * x.Attack_Bonus
    for x in player.Inventory:
        if x in Potion.list:
            val = input("You have a potion, do you wish to use it? - Y/N - ").lower()
            if val == "y":
                print("You take a sip.")
                player.Attack = player.Attack * x.Attack_Bonus
                player.Health = player.Health * x.Health_Bonus
                player.Inventory.remove(x)
            else:
                print("You reject the potion!")
    
    input()
            
    while Fighting == True:
        clear()
        if Current_Enemy.Health < 1:
            if player.Health < 1:
                win = True
                break
        if Current_Enemy.Health < 1:
            Current_Enemy.IsAlive = False
            win = True
            break
        elif Current_Enemy.Health > 0:
            Current_Enemy.IsAlive = True
        if player.Health < 1:
            player.IsAlive = False
            win = False
            print("You died!")
            exit()
            break
        elif player.Health > 0:
            player.IsAlive = True

        Current_Enemy.IsShielding = False
        player.Mana = player.Mana + 20
        Current_Enemy.Mana = Current_Enemy.Mana + 20
        print("\n\n\n\n\n")
        print(f"---------Player---------\n\nMana - {player.Mana}\nHealth - {player.Health}\n\n---------Enemy---------\n\nEnemy Health - {Current_Enemy.Health}\n\n")
        val = input("Choose an attack \n - 1. Shield (15) - 2. Light Attack (25) - 3. Heavy Attack (50) -\n\n\n\n\n\n\n")

        # The  main fighting mechanics, has an if statement to check for the players fighting choice. Checks everything using attributes and variables. 
        # IsShielding tells the program if you or the enemy is shielding which returns True or false.

        # Enemy -------------------¨
        TempChoice = Enemy_Turn(Current_Enemy.Mana)
        Damage = int()
        if TempChoice == "Shield":
            FightHistoryEnemy.append("Current_Enemy.Shield")
            Current_Enemy.Mana = Current_Enemy.Mana - 15
            Current_Enemy.IsShielding = True

        elif TempChoice == "Light":
            FightHistoryEnemy.append("Current_Enemy.Light")
            Current_Enemy.Mana = Current_Enemy.Mana - 25
            if  player.IsShielding == True:
                player.Health = player.Health - ((Current_Enemy.Attack)*0.3333)
                player.IsShielding = False
            if player.IsShielding == False:
                player.Health = player.Health - (Current_Enemy.Attack)

        elif TempChoice == "Heavy":
            FightHistoryEnemy.append("Current_Enemy.Heavy")
            Current_Enemy.Mana = Current_Enemy.Mana - 50
            if  player.IsShielding == True:
                player.Health = player.Health - (((Current_Enemy.Attack)*1.5)*0.3333)
                player.IsShielding = False
            if player.IsShielding == False:
                player.Health = player.Health - ((Current_Enemy.Attack)*1.5)

        player.IsShielding = False

        if val == "1":
            print("You draw your shield!")
            FightHistoryPlayer.append("Player.Shield")
            player.Mana = player.Mana - 15
            player.IsShielding = True
            input()

        elif val == "2":
            if player.Mana < 25:
                print("You dont have enough mana!")
            else:
                print("You swing you sword lightly!")
                FightHistoryPlayer.append("Player.Light")
                player.Mana = player.Mana - 25
                if Current_Enemy.IsShielding == True:
                    Damage = player.Attack / 3
                    print(f"Current_Enemy blocked your attack! - You dealt {Damage}")
                    Current_Enemy.Health = Current_Enemy.Health - Damage
                    Current_Enemy.IsShielding = False
                    input()
                elif Current_Enemy.IsShielding == False:
                    Damage = player.Attack
                    Current_Enemy.Health = Current_Enemy.Health - Damage
                    print(f"You hit the Current_Enemy - You dealt {Damage} Damage")
                    input()

        elif val == "3":
            if player.Mana < 50:
                print("You dont have enough mana!")
            else:
                print("You swing heavily!")
                FightHistoryPlayer.append("Player.Heavy")
                player.Mana = player.Mana - 50
                if Current_Enemy.IsShielding == True:
                    Damage = player.Attack * 1.5 / 3
                    print(f"Current_Enemy blocked your attack! - You dealt {Damage} Damage")
                    player.Mana = player.Mana - 5
                    Current_Enemy.Health = Current_Enemy.Health - Damage
                    Current_Enemy.IsShielding = False
                    input()
                elif Current_Enemy.IsShielding == False:
                    Damage = player.Attack * 1.5
                    Current_Enemy.Health = Current_Enemy.Health - Damage
                    print(f"You hit the Current_Enemy - You dealt {Damage} Damage")
                    input()
        if Current_Enemy.Health < 0:
            if TempChoice == "Light":
                print(f"The enemy swung and slashed you lightly for {(Current_Enemy.Attack)} damage!")
            if TempChoice == "Heavy":
                print(f"The enemy swung with massive force and dealt {(Current_Enemy.Attack) * 1.5}")
    
    print("\n\n\n\n\n\n\n\n\n\n\n\n")
    return winner

def artin():
    player.Xp += 1000
    clear()
    write("Disclaimer: Everything said here has been approved by Artin himself.")
    input()
    write("After traversing through the thick jungle you lay your eyes upon a little hut.")
    write("As the fog clears, you see it. Artin's kebab!")
    write("You carefully open the door and take a step inside")
    input()
    write(f" - Artin - : Heyy {player.name}, what brings you here.")
    while True:
        dialouge_choice = input("1. Im looking for something to purchase. 2. I was just swinging by. --> ")
        if dialouge_choice == "1":
            write(" - Artin - : Cool! I am currently having a deal.")
            write(" - Artin - : I will sell my finest kebabspätt for only 25 gold coins. Deal?\n\n")
            if input(f"You currently have {player.gold} gold. Do you wish to purchase Artins Kebabspätt - +{100 * (artins_kebabspätt.Attack_Bonus - 1)}% Damage Y/N\n").lower() == "y":
                if player.gold > 99:
                    player.gold -= 100
                    player.Inventory.append(artins_kebabspätt)
                    write(" - Artin - : Sweet!")
                    write("Artin hands you his kebabspätt and you are on your way.")
                    break
                else:
                    write(" - Artin - : It seems you dont have enought money, thats fine. Have a good one!")
                    write("You say your goodbyes and you are on your way")
                    break

            else:
                write(" - Artin - : Thats fine, have a good one!")
                write("You say your goodbyes and you are on your way")
                break
        elif dialouge_choice == "2":
            write(" - Artin - : Let me offer you some kebab, its on me.")
            write("You two sit down to talk and eat.")
            write(".....")
            write(".....")
            write(".....")
            write(" - Artin - : Have you heard about my deal?")
            write(" - Artin - : I will sell my finest kebabspätt for only 25 gold coins. Deal?\n\n")
            if input(f"You currently have {player.gold} gold. Do you wish to purchase Artins Kebabspätt - +{100 * (artins_kebabspätt.Attack_Bonus - 1)}% Damage Y/N\n").lower() == "y":
                if player.gold > 99:
                    player.gold -= 100
                    player.Inventory.append(artins_kebabspätt)
                    write(" - Artin - : Sweet!")
                    write("Artin hands you his kebabspätt and you are on your way.")
                    break
            else:
                write(" - Artin - : Thats fine, have a good one!")
                write("You say your goodbyes and you are on your way")
                break
        else:
            write(" - Artin - : I cant understand you, please can you repeat that?")
    show_inventory(2)


def gösta():
    write("After traversing even further into the wilderness you come to a sudden stop.")
    write("There he is, you are looking at him")
    write("The menace, the godlike being himself.")
    time.sleep(2)
    write("Ha ha ha, grabbar!")
    time.sleep(1)
    write("To be continued...")
    input("Press any key to continue")
    exit()


# -----------Level 1-------------
temp_choice = input("Do you wish to enter game_test mode? Y/N --> ").lower()
if temp_choice == "y":  
    player.Attack = 100000
    player.Health = 100000
    player.game_test_mode = True
    write_speed = 0
else:
    player.game_test_mode = False
    

write("Hey, youre finally awake!\n")
write("You were trying to cross the border")
time.sleep(1)
write(", right?\n")
time.sleep(1)
write("Walked right into that Imperial ambush\n")
write("same as us\n")
time.sleep(1)
write("and that thief over there!!\n")
time.sleep(1.5)
write("Anyways, whats your name traveler?")
player.name = input("--> ")
write(f"Well greetings {player.name}")
time.sleep(0.5)
write("sounds familiar")
write("wait...")
time.sleep(0.5)
write(f"Youre not that {player.name} right?")
write(f"The one that slayed the dragon!")
write(f"The one that survived Göstas wrath!")
write(f"It cant be...")
write("We all thought you were dead")
write("Its written in the books...")
write("You moved to brazil!!!")
print("---------------------------")
write(f"Suddenly, the carriage collapses. You hear a vine boom sound and look to your right!")




Current_Enemy, Current_Enemy.Health, Current_Enemy.Attack, Current_Enemy.Xp, Current_Enemy.Mana, Current_Enemy.Loot, Current_Enemy.IsShielding = Spawn_Enemy("Ogre", 1)
Current_Enemy.Loot
result = Fighting()
loot(Current_Enemy.tier)
show_inventory(2)

while True:
    print(f"Your level is currently: {player.Level}")
    if player.Level == 10:
        gösta()
    if player.Level == 5:
        artin()
    input()
    Current_Enemy, Current_Enemy.Health, Current_Enemy.Attack, Current_Enemy.Xp, Current_Enemy.Mana, Current_Enemy.Loot, Current_Enemy.IsShielding = Spawn_Enemy("Ogre", player.Level)
    Current_Enemy.Loot
    result = Fighting()
    loot(Current_Enemy.tier)
    show_inventory(2)
    
