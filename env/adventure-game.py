#This is a surivial based text game about zombies 

from time import sleep 
from sys import exit 

#Zombie Types
deadWalker = True #If false deadWalker is defeated 
deadKing = True 
#Weapon
gun = False

def begin():
    print(
        "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
     )
    print("Welcome to the Undead Survival Game")
    print(
        "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
     )
    print(
        "A virus created in a lab was accdientally released and now the world is full of zombies a.k.a Deadwalkers."
    )
    print("It's been 2 years since the outbreak and you are scavenging for food.")
    print("You enter a room with blood stained walls, and you have a gun in your bag.")
    print("It's pitched black, but you see some light coming from 3 doors.")
    print("These doors lead to three directions; north, east, and west. You choose to enter one of the doors.")
    print("You chose: north, east, or west")
    choice = input(">")
    
    if "west" in choice:
        room_2()
    elif "north" in choice:
        room_4()
    elif "east" in choice:
        print(
             "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
         )
        print(
            """ You carefully enter a passageway heading east. 
            After walking for a couple minutes, you run into a dead-end. 
            You turn around and you run into another dead-end. 
            You've somehow managed to trap yourself!
            You haven't found any food or water, and you end up dying 
            of starvation. Now you've become a Deadwalker! """
        )
        game_over()
    else:
        room_1()

def room_1():
    print("It's been 2 years since the outbreak and you are scavenging for food.")
    print("You enter a room with blood stained walls, and you have a gun in your bag.")
    print("It's pitched black, but you see some light coming from 3 doors.")
    print("These doors lead to three directions; north, east, and west. You choose to enter one of the doors.")
    print("You chose: north, east, or west")
    choice = input(">")

    if "west" in choice:
        room_2()
    elif "north" in choice:
        room_4()
    elif "east" in choice:
        print(
             "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
         )
        print(
            """ You carefully enter a passageway heading east. 
            After walking for a couple minutes, you run into a dead-end. 
            You turn around and you run into another dead-end. 
            You've somehow managed to trap yourself!
            You haven't found any food or water, and you end up dying 
            of starvation. Now you've become a Deadwalker! """
        )
        game_over()
    else:
        room_1()
    




        
    

    











