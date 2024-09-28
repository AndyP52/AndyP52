"""
Name: dragon_slayer.py
Author: Andrew Peterson
Date: 09/26/2024
Purpose: play a an adventure game
"""
from random import randint

health = 10
dragon_health = 10

name = input("Enter your username: ")
print(f"The princess has been captured by a dragon its up to you to save her, Sir {name}")
print("You face the dragon!")
while health > 0 and dragon_health > 0:
    print(f"Sir {name}'s health: {health}")
    print(f"the dragons health: {dragon_health}")
    choice = input("Do you (a)ttack or (d)efend: ")
    dragon_choice = randint(1,2)
    if choice == "a":
        if dragon_choice == 1:
            print(f"Both Sir {name} and the dragon attack each other.")
            damage = randint(0,3)
            dragon_damage = randint(0,3)
            print(f"Sir {name} deals the dragon {damage} damage")
            print(f"the dragon deals Sir {name} {dragon_damage} damage")
            health -= dragon_damage
            dragon_health -= damage
        else:
            print(f"Sir {name} attacks and the dragon defends.")
            damage = randint(0,3)
            dragon_damage = randint(0,3)
            print(f"Sir {name} deals the dragon {damage} damage")
            print(f"the dragon blocks {dragon_damage} damage")
            dragon_health = dragon_health - (damage - dragon_damage)
    elif choice == "d":
        if dragon_choice == 1:
            print(f"the dragon attacks and Sir {name} defends.")
            damage = randint(0,3)
            dragon_damage = randint(0,3)
            print(f"the dragon deals Sir {name} {dragon_damage} damage")
            print(f"Sir {name} blocks {damage} damage")
            health = health - (dragon_damage - damage)
        else:
            print(f"both Sir {name} and the dragon defend and nothing happens.")
    else:
        print("Not an option")
if health <= 0:
    print(f"Sir {name} died valliantly fighting the dragon")
elif dragon_health <= 0:
    print(f"Sir {name} slayed the dragon")
else:
    print(f"Sir {name} and the dragon felled each other")
