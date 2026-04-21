print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("""It is a bright evening. You and your pirate crew have landed on the shores of Katowaxhe Island. 
A group of locals dressed in grass skirts inform you that there is enough gold on their island to sink your ship twice over. 
However, most of it is guarded in a secret shrine underneath the Mystic Lake of their god Kataxhe. 
If you wish to find the gold and claim that sweet booty, you must find your way without the locals' help and battle both nature and their god.
Be warned, Kataxhe is the god of trickery and misfortune!""")

challenge = input("Are you up to the challenge? 'Yes' or 'no'?\n").lower()
if challenge == "yes":
    name = input("What is your name, Captain?\n")
    if name == " ":
        print("Restart with valid input.")
    else:
        print(f"""
		Aye aye, Captain {name}! I commend your bravery. 
		The Mystic Lake sits deep within the forest. 
		The locals only visit once a year and so the path is overgrown with weed and uncertainty. 
		You and your crew follow a trail until it disappears underneath a carpet of shrubs.
		Being experienced adventurers, your crew narrows down your options to two. 
		It is sandy up North and muddy due East.
		""")
        choice = input(f"Which path do you take, Captain {name}? 'North' or 'East'?\n").lower()
        if choice == "east":
            print(f"""
			Well done, Captain {name}! 
			The muddy path leads to a river bank. 
			There is a bridge, a boat, and a path along the river.
			Some crewmates want to take the boat, 
			some want to cross the bridge,
			others want to continue along the river.
			""")
            choice = input("Do you choose: 'boat,' 'cross,' or 'walk'?\n").lower()
            if choice == "walk":
                print("""
				Following the river upstream, you find a beautiful lake glowing red in the twilight.
				Is this the Mystic Lake?
				Your crew argues whether to: swim and search the lake or wait and see what happens. 
				They turn to you again, Captain.
				""")
                choice = input("What do you decide? 'Swim' or 'wait'?\n").lower()
                if choice == "wait":
                    print("""
					The group grumbles at your decision but soon the moon rises and the water glows blue. 
					The water recedes, showing gold runes in the sand. It is a golden trapdoor. 
					As you read the runes, the trapdoor opens, revealing a dark tunnel.
					You lead your crew down the tunnel and find three doors: 
					one is red, one is white, and the last is blue.
					""")
                    choice = input("Which door do you open first? Red, white, or blue?\n").lower()
                    if choice == "white":
                        print(f"""
						The door opens, revealing a stockpile of gold far larger than the locals had claimed.
						The trickster god Kataxhe cannot trick you, for this booty is yours to claim.
						Congratulations, Captain {name}! 
						""")
                    elif choice == "red":
                        print("""
						The door leads you down a sinewing path. A pair of gargoyle statues lurk in a corner.
						Flames shoot from their mouths as you approach, setting off explosives. 
						You and your crew are blown to bits.
						Game over.
						""")
                    elif choice == "blue":
                        print("""
						As you travel down this path, roars and shrieks haunt the dark. 
						Soon, you are attacked by vile beasts. 
						They tear you and your crew limb by limb.
						Game over.
						""")
                    else:
                        print("You are burned alive for your indecision. Game over.")
                elif choice == "swim":
                    print("""
					You and your crew begin to swim across, only to be torn to shreds by a shoal of piranhas.
					Bad choice, Captain. You led your crew to their demise.
					Game over.
					""")
                else:
                    print("""
					You have angered Kataxhe with your choice.
					Game over.
					""")
            elif choice == "cross":
                print("""
				You and your crew cross the bridge and continue to explore the forest.
				You get lost and never find your way out.
				Game over.""")
            elif choice == "boat":
                print("""
				You take the boat, attempting to navigate upstream to the lake.
				However, the current proves too strong and you are washed out to sea.
				Game over.
				""")
            else:
                print("""
				You have angered Kataxhe with your choice or lack thereof.
				Game over.
				""")
        elif choice == "north":
            print("""
			Oops, the sandy path turns out to be quicksand! 
			Perhaps if you were alone, you would have survived. 
			But your crew is present and you all die.\nGame over.
			""")
        else:
            print("""
			You have angered Kataxhe with your choice.
			Game over.
			""")
else:
    print(
        "Are you really going to return with your tail between your legs, you fucking coward?\nWell then, have it your way.")
