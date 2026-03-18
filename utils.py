#Imports
import time
import random
#Colours
RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
YELLOW = '\033[33m'
#Format
BOLD = '\033[1m'
#Reset formatting
DEFAULT = '\033[0m'
#settings
TYPECOLOUR = YELLOW
#Version
version="v0.3.0"
print("\n---------------------------------------------")
print(f"As of this version ({RED}{version}{DEFAULT}), the tools are: ")
print(f"Random number generator ({GREEN}type rng, rng tool or random number generator{DEFAULT})")
print(f"Printer ({GREEN}type printer or print{DEFAULT})")
print(f"Random name generator ({GREEN}type random name generator or name{DEFAULT})")
print(f"{DEFAULT}Type settngs to edit {YELLOW}settings {DEFAULT}and more.")
print(f"Type{RED}{BOLD} STOP{DEFAULT} to exit the app.")
print(f"That's all for now! {CYAN}Made by Sushibunny1150{DEFAULT}")
print("----------------------------------------------")

while True:
    tool=input(f"\nWhich tool will you be using now? {TYPECOLOUR}")

    #random number generator
    if tool=="random number generator" or tool=="rng" or tool=="rng tool":
        rangehigh=int(input(f"{DEFAULT}Highest possible number? {TYPECOLOUR}"))
        rangelow=int(input(f"{DEFAULT}Lowest possible number? {TYPECOLOUR}"))
        repeat=int(input(f"{DEFAULT}How many rolls? {TYPECOLOUR}"))

        count = {}

        for i in range(repeat):
            roll=random.randint(rangelow, rangehigh)
            print(DEFAULT, roll)

            if roll in count:
                count[roll] += 1
            else:
                count[roll] = 1
        query=input(f"{DEFAULT}Would you like to know how many times a number was rolled? {TYPECOLOUR}")

        if query=="yes":
            again="yes"
            while again=="yes":
                num=int(input(f"{DEFAULT}Which number would you like to know about? {TYPECOLOUR}"))
                print(f"{DEFAULT}{num} was rolled {count.get(num, 0)} times.")
                again=input(f"{DEFAULT}Would you like know about another number? {TYPECOLOUR}")
            print(f"{DEFAULT}ok.")
        else:
            print(f"{DEFAULT}ok.")
    


    #printer
    elif tool=="printer":
        again="yes"
        while again=="yes":
            phrase=input(f"{DEFAULT}What would you like to print? {TYPECOLOUR}")
            times=int(input(f"{DEFAULT}How many times? {TYPECOLOUR}"))
            for i in range(times):
                print(f"{DEFAULT}{phrase}")
            again=input(f"{DEFAULT}Do you require more printing? {TYPECOLOUR}")
        print(f"{DEFAULT}ok.")

    #random name generator
    elif tool=="name generator" or tool=="name":
        again="yes"
        while again=="yes":
            names = []
            print(f"{DEFAULT}Enter names into the generator. Ensure to press enter after each name and enter done when finished.")
            while True:
                name = input(f"{DEFAULT}Name: {TYPECOLOUR}")
                if name.lower() == "done":
                    break
                names.append(name)

            if names:
                print(f"{DEFAULT}Random name:{GREEN}{BOLD}", random.choice(names), DEFAULT)
            else:
                print(f"{DEFAULT}No names were entered.")
            again=input(f"{DEFAULT}Would you like to go again? {TYPECOLOUR}")
        print(f"{DEFAULT}ok.")

    #settings
    elif tool=="settings":
        print(DEFAULT,f"\n{BOLD}Settings{DEFAULT}\n")
        field=input(f"{DEFAULT}Which field?\n  Update\n  Typecolour\n{TYPECOLOUR}\n").lower()
        if field=="update":
            print(f"{DEFAULT}\nUpdate or get more python apps at link.link")
        elif field=="typecolour":
            color_map = {
                'RED': RED,
                'GREEN': GREEN,
                'CYAN': CYAN,
                'YELLOW': YELLOW
            }
            new_color = input(f"{DEFAULT}Enter a new valid colour (RED, GREEN, CYAN, YELLOW).\n{TYPECOLOUR}").upper()
            if new_color in color_map:
                TYPECOLOUR = color_map[new_color]
                print(f"\n{DEFAULT}Type colour updated to {new_color}.")
            else:
                print(f"{DEFAULT}Invalid color. Keeping current.")
    
    #What cool mapping app I use
    elif tool=="what app you use?":
        print("It goes by the name of Karabiner Elements.")
    
    
    #STOP
    elif tool.lower()=="stop":
        break
    else:
        print(f"{DEFAULT}This utility is not active or does not exist!")
    
