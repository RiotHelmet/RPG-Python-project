import random as rand
import math
import sys
import time

location_list = ["Trasmoz", "Bariw", "Istmina", "Bezouce", "Irara", "Quesnel", "Norheimsund", "Ram Ranch", "Desmus"]
weapon_type = ["Sword", "Dagger", "Spear", "Mallet", "Hammer", "Axe"]
first_word = ["Great", "Flawed", "Burning", "Moonlight", "Rock Hard", "Black", "Devoid of any meaning", "Short", "Long", "Huge", "Tiny", "Slightly Bent Left", "Gösta's long lost", "Gargoyle", "Enchanted", "Heavy", "Light"]


def random_weapon(tier):
    location = location_list[rand.randint(0, 8)]
    weapon = weapon_type[rand.randint(0, 5)]
    name = (f"{first_word[rand.randint(0, 16)]} {weapon} of {location}")
    strength = round((rand.uniform((math.sqrt(tier) - 0.2), (math.sqrt(tier) + 0.2))), 3)
    description = (f"A handcrafted {weapon} from the regions of {location}. Created through hard work and dedication by some of {location}'s finest blacksmiths. This weapon carries the strength power of {strength}")
    print(name)
    print(description)
    return name, strength, description

random_weapon(100)

MonsterTypes = ["Ogre", "Skeleton", "Dragon", "Boss"]

def write(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")