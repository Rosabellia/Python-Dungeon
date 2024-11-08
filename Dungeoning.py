#Variables
response = "yes"
name = ""
skill = ""
rock = ""
hasRock = False
hasStick = False
stick = ""
weapon = ""
hasWeapon = False
roll = 0

# Greet the player
print("Welcome to the Dungeon,\n")
print("In the Dungeon, you will create your character and help them finish their quest.\n")

while (response == "yes"):
    #reset variables
    name = ""
    skill = ""
    rock = ""
    hasRock = False
    hasStick = False
    stick = ""
    weapon = ""
    hasWeapon = False
    roll = 0
    # Have the player create a simple character
    name = input("First thing, what would you like your character to be called? ")
    while skill not in ("Strength", "Magic", "Stealth"):
        skill = input("\nWhat skillset are they going to major in? Strength, Magic, or Stealth? ")

    # Give the player an intro and then their first choice
    print("\nKnight: Wecome adventure. You have been given a task by the King himself to defeat the Minotaur.")
    print("Knight: This foul beast has been tormenting the townsfolk for too long. I wish you best on your adventures.\n")

    print("The knight sends you on your way. You leave the castle gates and head towards the forest.\n")
    print("On the outskirts of the forest, you stuble upon a strange rock.")
    if skill == "Strength":
        print("\n" + name + ": Why is this rock glowing? rocks are't supposed to glow.")
        
        while rock not in ("pick it up", "throw it", "ignore it"):
            rock = input("\nWhat do you do with this rock? do you pick it up, throw it, or ignore it? ")
            if rock == "pick it up":
                print("\n" + name + ": It's always good to keep some rocks on you. You never know when you may need it.")
                hasRock = True
            elif rock == "throw it":
                print("\n" + name + ": Away foul rock!")
                print("You hear an explosion from where you threw the rock.")
            elif rock == "ignore it":
                print("\n" + name + ": There is no use for a glowing rock when I have my sword!")

    elif skill == "Magic":
        print("\n" + name + ": Strange, I feel some magic leaking out of this rock.")

        while rock not in ("pick it up", "throw it", "ignore it"):
            rock = input("\nWhat do you do with this rock? do you pick it up, throw it, or ignore it? ")
            if rock == "pick it up":
                print("\n" + name + ": I must study this when I get back.")
                hasRock = True
            elif rock == "throw it":
                print("\n" + name + ": Eh, I have no ues fore this.")
                print("You hear an explosion from where you threw the rock.")
            elif rock == "ignore it":
                print("\n" + name + ": I better just leave it alone.")

    elif skill == "Stealth":
        print("\n" + name + ": Strange glowing rock. I wonder if this has anything to do with the Minotaur.")

        while rock not in ("pick it up", "throw it", "ignore it"):
            rock = input("\nWhat do you do with this rock? do you pick it up, throw it, or ignore it? ")
            if rock == "pick it up":
                print("\n" + name + ": Who knows how much this would go for.")
                hasRock = True
            elif rock == "throw it":
                print("\n" + name + ": It's just a useless trinket. Some mage must have left it.")
                print("You hear an explosion from where you threw the rock.")
            elif rock == "ignore it":
                print("\n" + name + ": I'll be too obvious with that stone.")
                
    else:
        print("An error has occured. Please restart the game.")

    # Give them their second choice
    print("\nYou continue into the forest, following the trail of destruction.")
    print("You trumble upon a cave. You assume this is the Minotaur's hideout.")
    print("Outside of the cave you see good sized stick.")
    

    if skill == "Strength":
        while stick not in ("yes", "no"):
            stick = input("\nDo you take the stick? ")
            if stick == "yes":
                print("You pick up the stick.")
                print(name + ": I can use this as a wapon.")
                hasStick = True
            elif stick == "no":
                print(name + ": I have no use for a measly stick like that.")

    elif skill == "Magic":
        while stick not in ("yes", "no"):
            stick = input("\nDo you take the stick? ")
            if stick == "yes":
                print("You pick up the stick")
                print(name + ": This shoule be useful.")
                hasStick = True
            elif stick == "no":
                print(name + ": What would I need a stick for?")

    elif skill == "Stealth":
        while stick not in ("yes", "no"):
            stick = input("\nDo you take the stick? ")
            if stick == "yes":
                print("You pick up the stick")
                print(name + ": Eh, better than my rusty knife.")
                hasStick = True
            elif stick == "no":
                print("You walk by the stick.")
    else:
        print("An error has occured. Please restart the game.")

    if hasRock == True and hasStick == True:
        while weapon not in ("yes", "no"):
            print("You look at your stick and your glowing rock and wonder if you can make a weapon out of this.")
            weapon = input("\nDo you? ")
            if weapon == "yes":
                print("You put the rock on the top of your stick and old them together with some rope.")
                if skill == "Strength":
                    print("You watch as your makeshift weapon glows and turns into a sword.")
                    print(name + ": Finally! A worthy weapon!")

                elif skill == "Magic":
                    print("You watch as your makeshift weapon glows and turns into a staff.")
                    print(name + ": This will do nicely.")

                elif skill == "Stealth":
                    print("You watch as your makeshift weapon glows and turns into a daggar.")
                    print(name + "Sweet! I knew that rock was good for something!")
                else:
                    print("An error has occured. Please restart the game.")
                hasWeapon = True
                hasRock = False
                hasStick = False

    # Give the player their last choice
    print("\nYou walk into the cave. After a wile you see a fire in the distance.")
    print(name + (": That must be the Minotaur. Let's see what I've got."))
    
    roll = int(input("One last question before the fight, what did you roll? (1-20)"))

    if hasRock == True:
        print("You take out your rock.")
        print(name + ": I wonder how hard I can throw this?")
        roll = roll + 2
    elif hasStick == True:
        print("You take out your stick.")
        print(name + "It's better than nothing.")
        roll = roll + 3
    elif hasWeapon == True:
        print("You take our your weapon")
        print(name + ": I am ready.")
        roll = roll + 5
    else:
        print(name + ": I hope I'm ready")

    if roll < 14:
        if skill == "Strength":
            if hasRock == True:
                print("You run in, preparing to throw the rock-\n")
            elif hasStick == True:
                print("You run in, stick in hand -\n")
            elif hasWeapon == True:
                print("You run in, shiny new sword in hand -\n")
            else:
                print("You run in, old sword in hand -\n")
            print("\n- and the Minotuar swats you to the side. You hit the wall.")


        elif skill == "Magic":
            if hasRock == True:
                print("You slowly walk up to the Minotuar, preparing to throw the rock when-\n")
            elif hasStick == True:
                print("You slowly walk up to the Minotuar, trying to figure out how to cast spells with the stick when-\n")
            elif hasWeapon == True:
                print("You slowly walk up to the Minotuar, preparing a spell with your new staff when-\n")
            else:
                print("You slowly walk up to the Minotuar, preparing a spell when-\n")
            print("\n- the Minotuar throws a huge rock in your direction. It goes through your spell barrior and you roll out of the cave")

        elif skill == "Stealth":
            if hasRock == True:
                print("You sneak around the room, rock in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you throw the rock at him.")
                print("He catches the rock and throws it back with more force. The rock explodes on the wall.")
            elif hasStick == True:
                print("You sneak around the room, stick in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you run up to hit him with the stick.")
                print("He catches the stick and crushes it in his hand. You stare at him before running out")

            elif hasWeapon == True:
                print("You sneak around the room, brand new weapon in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you run up to hit him with the sword.")
                print("\nHe catches the the sword with his hand and tries to crush it. When that doesn't work, he pulls it out of you hand")
                print("and throws it to the other side of the cave. You stare at him before running away.")
            else:
                print("You sneak around the room, rusty daggar in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you run up to hit him with the daggar.")
                print("\nHe catches the the sword with his hand and pulls the blade from the hilt.")
                print("You stare at your suddenly bladeless daggar, and run away.")
        print("\nPride ruined, you leave the cave and go to a town far from here.")

    elif roll > 14 and roll < 18:
        if skill == "Strength":
            if hasRock == True:
                print("You run in, preparing to throw the rock-\n")
                print("you hit him on the head, it explodes in dust and sparkles, stunning him.")
                print("Not thinking this far ahead, you look for anything that you could use to help you fight.")
                print("You find a bone and hit him with it.")
                print("He is injrued, but when you go to hit him again, he catches the bone.")
                print("He takes the bone away and hits you with it. You fall over near the enterance.")
                print("You look for any other kind of weapon you could use, and find none.")
            elif hasStick == True:
                print("You run in, stick in hand -\n")
                print("you hit him on the side. Stunned, the Minotuar looks back at you.")
                print("You take your chance and hit again.")
                print("He is injrued, but when you go to hit him once again, he catches the stick.")
                print("He takes the stick away and hits you with it before he snaps it in half. You fall over near the enterance.")
                print("You look for any other kind of weapon you could use, and find none.")
            elif hasWeapon == True:
                print("You run in, shiny new sword in hand -\n")
                print("you hit him on the side, cutting him. Stunned, the Minotuar looks back at you.")
                print("You take your chance and hit again on his other side gettins a more narrow cut.")
                print("He is injrued, but when you go to hit him once again, he catches the sword.")
                print("He goes to pull the sword away, but as soon as he touched it, he pulled his hand away.")
                print("Frustrated, he grabs a club that was sitting next to him, and walks towards you.")
                print("He swings and you narrowly dodged. He swings again and hits you, flinging you towards the enterance.")
            else:
                print("You run in, old sword in hand -\n")
                print("you hit him on the side, grazing him. Startled, the Minotuar looks back at you.")
                print("You take your chance and hit again on his other side gettins a small cut.")
                print("He is injrued, but when you go to hit him once again, he catches the sword.")
                print("He pulls the sword away and swings it at you. You dodge the first attack, but not the second")
                print("He swings and hits you. You stagger back towards the enterance.")

        elif skill == "Magic":
            if hasRock == True:
                print("You slowly walk up to the Minotuar, preparing to throw the rock when-\n")
                print("\n- the Minotuar throws a huge rock in your direction. You dodge out of the way and throw the rock.")
                print("It lands at the Minotuar's feet and explodes into sparkles and dust.")
                print("You walk farther into the cave to see where he might have gone, when the Minotuar grabs you from the back")
                print("and throws you back towards the enterance.")
                print("As you get up, you see him walking towards a giant club up against the wall.")

            elif hasStick == True:
                print("You slowly walk up to the Minotuar, trying to figure out how to cast spells with the stick when-\n")
                print("\n- the Minotuar throws a huge rock in your direction. You dodge out of the way and cast you spell.")
                print("The spell misses, but hits the rock next to him, exploding in sparkles and dust.")
                print("You walk farther into the cave to see where he might have gone, when the Minotuar grabs you from the back")
                print("and throws you back towards the enterance.")
                print("As you get up, you see him walking towards a giant club up against the wall.")
            elif hasWeapon == True:
                print("You slowly walk up to the Minotuar, preparing a spell with your new staff when-\n")
                print("\n- the Minotuar throws a huge rock in your direction. You dodge out of the way and cast you spell.")
                print("The spell misses, but hits the rock next to him, exploding in sparkles and dust.")
                print("You walk farther into the cave to see where he might have gone, when the Minotuar grabs you from the back.")
                print("You hit him with the staff and he drops you.")
                print("As you get up, you see him walking towards a giant club up against the wall.")
                print("You go to grab your weapon, but it's fallen near the Minotuar, and he has gotten his club")
            else:
                print("You slowly walk up to the Minotuar, preparing a spell when-\n")
                print("\n- the Minotuar throws a huge rock in your direction. You dodge out of the way and cast you spell.")
                print("The spell misses, but hits the rock next to him, exploding in sparkles and dust.")
                print("You walk farther into the cave to see where he might have gone, when the Minotuar grabs you from the back")
                print("and throws you back towards the enterance.")
                print("As you get up, you see him walking towards a giant club up against the wall.")


        elif skill == "Stealth":
            if hasRock == True:
                print("You sneak around the room, rock in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you throw the rock at him.")
                print("It lands at his feet, and explodes into sparkles and dust.")
                print("You use this as a distraction and jump at him with your rusty knife.")
                print("You manage to get a couple of its on him before he shakes you off.")
                print("Cocky, you run in again, but he swats you away and you hit the wall near the enterance.")
            elif hasStick == True:
                print("You sneak around the room, stick in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you run up to hit him with the stick.")
                print("You hit him in the head and then his side.")
                print("You use this as a distraction and jump at him with your stick.")
                print("You manage to get a couple of its on him before he shakes you off.")
                print("Cocky, you run in again, but he swats you away and you hit the wall near the enterance.")
            
            elif hasWeapon == True:
                print("You sneak around the room, brand new weapon in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you run up to hit him with the sword.")
                print("You hit him in the head and then his side, cutting him.")
                print("You use this as a distraction and jump at him with your sword.")
                print("You manage to get a couple of its on him before he shakes you off.")
                print("Cocky, you run in again, but he swats you away and you hit the wall near the enterance.")
            else:
                print("You sneak around the room, rusty daggar in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you run up to hit him with the daggar.")
                print("You hit him in the head and then his side.")
                print("You use this as a distraction and jump at him with your rusty knife.")
                print("You manage to get a couple of its on him before he shakes you off.")
                print("Cocky, you run in again, but he swats you away and you hit the wall near the enterance.")
        print("You decide to leave and come back more prepared.")

    elif roll >= 18:
        if skill == "Strength":
            if hasRock == True:
                print("You run in, preparing to throw the rock-\n")
                print("you hit him on the head, it explodes in dust and sparkles, stunning him.")
                print("Not thinking this far ahead, you look for anything that you could use to help you fight.")
                print("You find a bone and hit him with it.")
                print("He is injrued, but when you go to hit him again, he catches the bone.")
                print("He tries to take the bone away, but you swing around and hit him in the head again.")
                print("The Minotuar staggers back and you get one final blow on him.")

            elif hasStick == True:
                print("You run in, stick in hand -\n")
                print("you hit him on the side. Stunned, the Minotuar looks back at you.")
                print("You take your chance and hit again.")
                print("He is injrued, but when you go to hit him once again, he catches the stick.")
                print("He tries to take the stick away, but you swing around and hit him in the head again.")
                print("The Minotuar staggers back and you get one final blow on him.")
            elif hasWeapon == True:
                print("You run in, shiny new sword in hand -\n")
                print("you hit him on the side, cutting him. Stunned, the Minotuar looks back at you.")
                print("You take your chance and hit again on his other side gettins a more narrow cut.")
                print("He is injrued, but when you go to hit him once again, he catches the sword.")
                print("He goes to pull the sword away, but as soon as he touched it, he pulled his hand away.")
                print("Frustrated, he goes to grab a club, you take this opertunity to hit him in the back")
            else:
                print("You run in, old sword in hand -\n")
                print("you hit him on the side, grazing him. Startled, the Minotuar looks back at you.")
                print("You take your chance and hit again on his other side gettins a small cut.")
                print("He is injrued, but when you go to hit him once again, he catches the sword.")
                print("He tries to take the sword away, but you swing around and hit him in the head again.")
                print("The Minotuar staggers back and you get one final blow on him.")
            print("He collapses and you have defeated the Minotuar.")

        elif skill == "Magic":
            if hasRock == True:
                print("You slowly walk up to the Minotuar, preparing to throw the rock when-\n")
                print("\n- the Minotuar throws a huge rock in your direction. You dodge out of the way and throw the rock.")
                print("It lands at the Minotuar's feet and explodes into sparkles and dust.")
                print("Not risking it, you send a spell towards where you last saw him.")
                print("It does not hit, but you see movement from behind you and dodge the Minotuar's attack.")
                print("You send a well aimed spell at him and he collapses. You have defeated the Minotuar.")

            elif hasStick == True:
                print("You slowly walk up to the Minotuar, trying to figure out how to cast spells with the stick when-\n")
                print("\n- the Minotuar throws a huge rock in your direction. You dodge out of the way and cast you spell.")
                print("The spell misses, but hits the rock next to him, exploding in sparkles and dust.")
                print("Not risking it, you use the stick to send another spell towards where you last saw him.")
                print("It does not hit, but you see movement from behind you and dodge the Minotuar's attack.")
                print("You send a well aimed spell at him and he collapses. You have defeated the Minotuar.")
            elif hasWeapon == True:
                print("You slowly walk up to the Minotuar, preparing a spell with your new staff when-\n")
                print("\n- the Minotuar throws a huge rock in your direction. You dodge out of the way and cast you spell.")
                print("The spell misses, but hits the rock next to him, exploding in sparkles and dust.")
                print("You walk farther into the cave to see where he might have gone, when the Minotuar grabs you from the back.")
                print("You hit him with the staff and he drops you.")
                print("As you get up, you see him walking towards a giant club up against the wall.")
                print("You grab your staff, and dodge an attack.")
                print("Remembering his reaction, you send in an explosion spell and hit him in the head with your staff.")
                print("He collapses and you have defeated the Minotuar.")
            else:
                print("You slowly walk up to the Minotuar, preparing a spell when-\n")
                print("\n- the Minotuar throws a huge rock in your direction. You dodge out of the way and cast you spell.")
                print("The spell misses, but hits the rock next to him, exploding in sparkles and dust.")
                print("Not risking it, you send in another spell towards where you last saw him.")
                print("It does not hit, but you see movement from behind you and dodge the Minotuar's attack.")
                print("You send a well aimed spell at him and he collapses. You have defeated the Minotuar.")

        elif skill == "Stealth":
            if hasRock == True:
                print("You sneak around the room, rock in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you throw the rock at him.")
                print("It lands at his feet, and explodes into sparkles and dust.")
                print("You use this as a distraction and jump at him with your rusty knife.")
                print("You manage to get a couple of its on him before he shakes you off.")
                print("Cocky, you run in again and hit at him until he collapses")
            elif hasStick == True:
                print("You sneak around the room, stick in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you run up to hit him with the stick.")
                print("You hit him in the head and then his side.")
                print("You use this as a distraction and jump at him with your stick.")
                print("You manage to get a couple of its on him before he shakes you off.")
                print("Cocky, you run in again and hit at him until he collapses")
            
            elif hasWeapon == True:
                print("You sneak around the room, brand new weapon in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you run up to hit him with the sword.")
                print("You hit him in the head and then his side, cutting him.")
                print("You use this as a distraction and jump at him with your sword.")
                print("You manage to get a couple of its on him before he shakes you off.")
                print("Cocky, you run in again, but he swats you away and you hit the wall near the enterance.")
            else:
                print("You sneak around the room, rusty daggar in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you run up to hit him with the daggar.")
                print("You hit him in the head and then his side.")
                print("You use this as a distraction and jump at him with your rusty knife.")
                print("You manage to get a couple of its on him before he shakes you off.")
                print("Cocky, you run in again and hit at him until he collapses")

    else:
        print("\nDebug: If this shows, invalid number was given\n")
        if skill == "Strength":
            if hasRock == True:
                print("You run in, preparing to throw the rock-\n")
            elif hasStick == True:
                print("You run in, stick in hand -\n")
            elif hasWeapon == True:
                print("You run in, shiny new sword in hand -\n")
            else:
                print("You run in, old sword in hand -\n")
            print("\n- and the Minotuar swats you to the side. You hit the wall.")


        elif skill == "Magic":
            if hasRock == True:
                print("You slowly walk up to the Minotuar, preparing to throw the rock when-\n")
            elif hasStick == True:
                print("You slowly walk up to the Minotuar, trying to figure out how to cast spells with the stick when-\n")
            elif hasWeapon == True:
                print("You slowly walk up to the Minotuar, preparing a spell with your new staff when-\n")
            else:
                print("You slowly walk up to the Minotuar, preparing a spell when-\n")
            print("\n- the Minotuar throws a huge rock in your direction. It goes through your spell barrior and you roll out of the cave")

        elif skill == "Stealth":
            if hasRock == True:
                print("You sneak around the room, rock in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you throw the rock at him.")
                print("He catches the rock and throws it back with more force. The rock explodes on the wall.")
            elif hasStick == True:
                print("You sneak around the room, stick in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you run up to hit him with the stick.")
                print("He catches the stick and crushes it in his hand. You stare at him before running out")

            elif hasWeapon == True:
                print("You sneak around the room, brand new weapon in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you run up to hit him with the sword.")
                print("\nHe catches the the sword with his hand and tries to crush it. When that doesn't work, he pulls it out of you hand")
                print("and throws it to the other side of the cave. You stare at him before running away.")
            else:
                print("You sneak around the room, rusty daggar in hand-\n")
                print("\n- then the Minotuar turns in your direction. Frozen, you run up to hit him with the daggar.")
                print("\nHe catches the the sword with his hand and pulls the blade from the hilt.")
                print("You stare at your suddenly bladeless daggar, and run away.")
        print("\nPride ruined, you leave the cave and go to a town far from here.")
    
    response = input(print("Would you like to play again? yes/no: "))

print("Thank you for playing!")