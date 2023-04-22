#This is a surivial based text game about zombies 

from time import sleep 
from sys import exit 

#Zombie Types
deadWalker = True #If false deadWalker is defeated 
alpha_deadWalker = True 
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
    print("It's pitch black, but you see some light coming from 3 doors.")
    print("These doors lead to three directions; north, east, and west.")
    print("What do you do?")
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
    print("These doors lead to three directions; north, east, and west.")
    print("What do you do?")
    print("You chose: north, east, or west")
    choice = input("> ")

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
            of starvation. Now you've become a ....................
            Deadwalker!!! """
        )
        game_over()
    else:
        room_1()

def room_2():
    print(
        "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
    )
    print("You enter this room with a really low ceiling and you must crouched to navigate through.")
    print("You see a passage leading west and a passage leading north.")
    print("On the far end of the west passage you see a bright light.")
    print("On the passage heading east you smell something foul.")
    print("The passage to the east leads to the first room.")
    print("What do you do?")
    print("You chose: north, east, west")
    choice = input("> ")

    if "west" in choice: 
        print(
            "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
        )
        print(
            """ You go down the bright path, and you start hearing some loud noises.
            All of a sudden the floor under you caves in, and you fall into a hole full
            of zombies. You try to fight off the zombies, but eventually you succumb to them. 
            You did screaming in pain and you become a ..................
            Deadwalker!!! """
        )
        game_over()
    elif "north" in choice:
        room_3()
    elif "east" in choice:
        room_1()
    else:
        room_2()

def room_3():
    
    global deadWalker
    global gun 

    if deadWalker:
        print(
            "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
        )
        print("You enter the room where the foul smell came from, and the floor is littered with rooting corpses.")
        print("All of a sudden you hear a loud growl, and an extremely vicious Deadwalker appears in front of you")
        print("You see a passage to the east; there's a lit torch on the ground,")
        print("a Deadwalker holding a sword, and a hole on the far side of the room.")
        print("The passage to the south leads to the second room")
        print("What do you do?")
        print("You choose: east, torch, gun, or south")
        choice = input("> ")

        if "east" in choice:
            print(
                "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
            )
            print(
                """You run towards the east passage, and a Deadwalker leaps in front of you. It catches you off guard, 
                so you don't have time react, and the Deadwalker rips off your head."""
            )
            game_over()
        elif "torch" in choice:
            print(
                "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
            )
            print(
                """ You take the torch and wave it in front of the Deadwalkers. The Deadwalker starts to back away, 
                and you force it back until it stumbles and falls into the hole."""
            )
            deadWalker = False
            room_3()
        elif "gun" in choice:
            print(
                "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
            )
            print(
                """ You see the vicous Deadwalker start to run towards you. 
                You take the gun out of your bag,and start shooting at the 
                Deadwalker and you kill the Deadwalker."""
            )
            deadWalker = False
            gun = True
            room_3()
        elif "hole" in choice:
            print(
                "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
            )
            print(
                """You for whatever reason decide the jump down the hole. 
                The hole is much deeper than you realize, you fall down 
                and end up breaking your leg. All of a sudden a Deadwalker 
                appears and you're too injured to move. You try your best to 
                fight it off, but it overpowers you and kills you."""
            )
            game_over()
        elif "south" in choice:
            room_2()
        else:
            room_3()
    
    else: 
        print(
            "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
        )
        print("You enter the room where the foul smell came from, and the floor is littered with rooting corpses.")
        print("All of a sudden you hear a loud growl, and an extremely vicious Deadwalker appears in front of you")
        print("You see a passage to the east; there's a lit torch on the ground,")
        print("a Deadwalker holding a sword, and a hole on the far side of the room.")
        print("The passage to the south leads to the second room")
        print("What do you do?")
        print("You choose: east, torch, gun, or south")
        choice = input("> ")

        if "east" in choice:
            room_4()
        elif "torch" in choice:
            print(
                "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
            )
            print(
                """You take the torch, but it seems redundant because you can already see, 
                so you decide to put the torch down."""
            )
            room_3()
        elif "gun" in choice:
            print("""You take the gun out of your bag""")
            gun = True
            room_3() 
        elif "hole" in choice:
            print(
                """You for whatever reason decide the jump down the hole. 
                The hole is much deeper than you realize, you fall down 
                and end up breaking your leg. All of a sudden a Deadwalker 
                appears and you're too injured to move. You try your best to 
                fight it off, but it overpowers you and kills you."""
            )
            game_over()
        elif "south" in choice:
            room_2()
        else:
            room_3()

def room_4():

    global alpha_deadWalker

    if alpha_deadWalker:
        print(
            "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
        )
        print(
            """In this room you see an abnormally big zombie. You've heard about these types of Deadwalkers before,
            people call them Alphas. The Alphas are stronger and faster than a regular Deadwalker,
            You can take your gun, or head in other directions."""
        )
        print("You choose: gun, north, east, west, south")
        choice = input("> ")
        if "gun" in choice: 
            print(
                """You and the Alpha lock eyes, it lets out a loud roar, and starts running towards you at an incredible speed.
                You grab your gun from your bag, you shoot it a couple times, but it's not stopping. Just when it's about to hit you, 
                you manage to hit it square in the head. It dies while screaming in agony."""
            )
            alpha_deadWalker = False
            room_4()
        else:
            print(
                "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
            )
            print("There is a passage to the north, a passage to the east,")
            print("one to the west, and another to the south.")
            print("What do you do?")
            print("You choose: north, east, west, south ")
            choice = input("> ")

            if "east" in choice:
                print(
                    "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
                )
                print(
                    """You follow down the passageway heading east, and it leads to a little room. 
                    In the room you see a little desk with a PC and a monitor. You see a man and he's typing
                    and he notices you. He says, 'What are you doing here? You shouldn't have found 
                    me, I'm the coder of the game. Now you must die.' You try to take out your gun, but before
                    you can anything. He types something, and you die. """
                )
                game_over()
            elif "south" in choice:
                room_1()
            elif "west" in choice:
                room_3()
            elif "north" in choice:
                print(
                    "ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ ˬ "
                )
                print(
                    """The passageway leads to the outside, and you hear some noise. 
                    Someone grabs your hand, and takes you in a helicopter. 
                    They tell you, 'You're safe now'.You are free! YOU HAVE WON THE GAME!!! """
                )
                win()
            else:
                room_4()

def start():
    begin()

def win():
    global deadWalker
    global alpha_deadWalker
    global gun 

    deadWalker = True
    alpha_deadWalker = True
    gun = False
    print("Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ Ѱ")
    print("YOU WIN!")
    print("You fly off into the sunset on a helicopter")
    print("Do you want to play again? (y/n)")

    choice = ""
    while choice != "y" and choice != "n":
        choice("> ")
        if choice == "y":
            start()
        elif choice == "n":
            exit(0) 

def game_over():
    global deadWalker
    global alpha_deadWalker
    global gun 

    deadWalker = True
    alpha_deadWalker = True 
    gun = False
    print("ƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔƔ")
    print("GAME OVER")
    print("You are now a Deadwalker")
    print("Do you want ot play again? (y/n)")

    choice = ""
    while choice != "y" and choice != "n":
        choice = input("> ")
        if choice == "y":
            start()
        elif choice == "n":
            exit(0)

start()



    














            

        


        


    





        
    

    











