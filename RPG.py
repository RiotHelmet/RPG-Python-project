import random as rand
import math
import module
import time
MonsterTypes = ["Ogre", "Skeleton", "Dragon", "Boss"]

        

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
    Level = int()
    Xp = int()
    Mana = 0 < int() < 100
    IsShielding = bool

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
artins_kebabspätt.Attack_Bonus = 1.3
Weapon.list.append(artins_kebabspätt)



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
    elif Current_Enemy.Type == "Skeleton":
        Current_Enemy.Health = int((math.sqrt(difficulty) * 750))
        Current_Enemy.Attack = (math.sqrt(difficulty) * 225)
        Current_Enemy.Xp = (difficulty * 100)
        Current_Enemy.Mana = 50
        Current_Enemy.Loot = []
        Current_Enemy.IsShielding = False
    return Current_Enemy, Current_Enemy.Health, Current_Enemy.Attack, Current_Enemy.Xp, Current_Enemy.Mana, Current_Enemy.Loot, Current_Enemy.IsShielding
# Current_Enemy, Current_Enemy.Health, Current_Enemy.Attack, Current_Enemy.Xp, Current_Enemy.Mana, Current_Enemy.Loot, Current_Enemy.IsShielding = Spawn_Enemy("Ogre", 1)


def loot(enemy_tier):
    gold = round((rand.uniform((math.sqrt(enemy_tier) - 5), (math.sqrt(enemy_tier) + 5))), 1)

    while True:
        print("")

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
    player.Health = 1000
    player.IsAlive = True
    Current_Enemy.IsAlive = True
    winner = ""
    Fighting = True
    loot = Current_Enemy.Loot
    print(f"You encountered an {Current_Enemy.Type}!\n")
    input()
    for x in player.Inventory:
        if x in Potion.list:
            val = input("You have a potion, do you wish to use it? - Y/N - ")
            if val == "Y":
                print("You take a sip.")
                player.Attack = player.Attack * x.Attack_Bonus
                player.Health = player.Health * x.Health_Bonus
                player.Inventory.remove(x)
            else:
                print("You reject the potion!")
    
    input()
            
    while Fighting == True:
        if Current_Enemy.Health < 1:
            if player.Health < 1:
                win = True
                ("Winner is player")
                break
        if Current_Enemy.Health < 1:
            Current_Enemy.IsAlive = False
            win = True
            print("Winner is player")
            break
        elif Current_Enemy.Health > 0:
            Current_Enemy.IsAlive = True
        if player.Health < 1:
            player.IsAlive = False
            win = False
            print("winner is enemy")
            break
        elif player.Health > 0:
            player.IsAlive = True

        Current_Enemy.IsShielding = False
        player.Mana = player.Mana + 20
        Current_Enemy.Mana = Current_Enemy.Mana + 20
        print("\n\n\n\n\n")
        print(f"---------Player---------\n\nMana - {player.Mana}\nHealth - {player.Health}\n\n---------Enemy---------\n\nEnemy Health - {Current_Enemy.Health}\n\n")
        val = input("Choose an attack \n - Shield (15) - Light Attack (25) - Heavy Attack (50) -\n")

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

        if val == "Shield":
            print("You draw your shield!")
            FightHistoryPlayer.append("Player.Shield")
            player.Mana = player.Mana - 15
            player.IsShielding = True
            input()

        elif val == "Light Attack":
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

        elif val == "Heavy Attack":
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
        if TempChoice == "Light":
            print(f"The enemy swung and slashed you lightly for {(Current_Enemy.Attack)} damage!")
        if TempChoice == "Heavy":
            print(f"The enemy swung with massive force and dealt {(Current_Enemy.Attack) * 1.5}")
    return winner


#-----------Level 1-------------
# module.write("Hey, youre finally awake!\n")
# module.write("You were trying to cross the border")
# time.sleep(1)
# module.write(", right?\n")
# time.sleep(1)
# module.write("Walked right into that Imperial ambush\n")
# module.write("same as us\n")
# time.sleep(1)
# module.write("and that thief over there!!\n")
# time.sleep(1.5)
# module.write("Anyways, whats your name traveler?")
# player.name = input("-->")
# module.write(f"Well greetings {player.name}")
# time.sleep(0.5)
# module.write("sounds familiar")
# module.write("wait...")
# time.sleep(0.5)
# module.write(f"Youre not that {player.name} right?")

# val = input("1 - I was, before the accident. 2 - No idea who youre talking about 3 - No, shut up with that bullshit")
# if val == 1:
#     print("")





Current_Enemy, Current_Enemy.Health, Current_Enemy.Attack, Current_Enemy.Xp, Current_Enemy.Mana, Current_Enemy.Loot, Current_Enemy.IsShielding = Spawn_Enemy("Ogre", 1)
result = Fighting()

if result == True:
    print("")