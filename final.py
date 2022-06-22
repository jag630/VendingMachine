#Jacob Goodman
#CSCI-T599 Intro to Comp and Prog
#Assignment 3
#June 21 2022 2:00pm
#GitHub link: https://github.com/jag630/VendingMachine

#Vending Machine Assignment. Build a vending machine with 10 items and randomized inventory.
#Allow the user to purchase multiple items and pay in any combination of bills/coins.
#Provide change with the least number of bills/coins possible.

#My unique feature: The user gets $1 off for every $10 spent.

import random

#This is the main function that runs at program launch.
def plugIn():
    items = ["Cool Ranch Doritos",
             "Jalapeno Crunchers",
             "Pizza Combos",
             "Gardetto's Rye Chips",
             "Wasabi Peas",
             "Reese's Cups",
             "Tropical Skittles",
             "Raspberry Fig Bars",
             "Chocolate w/Hazelnuts",
             "Pineapple Gummy Bears"]
    inventory = randInv()
    prices = ["1.00", "1.00", "2.00", "2.00", ".75", ".75", ".75", "1.00", "1.00", ".75"]
    itemSelected = 0
    howMany = 0
    total = 0
    moneyEntered = 0
    change = 0

    print("Welcome to the SNACK MACHINE!".center(50))
    print("   __________  ____  ____     _________  ___________")
    print("  / ____/ __ \/ __ \/ __ \   / ____/   |/_  __/ ___/")
    print(" / / __/ / / / / / / / / /  / __/ / /| | / /  \__ \ ")
    print("/ /_/ / /_/ / /_/ / /_/ /  / /___/ ___ |/ /  ___/ / ")
    print("\____/\____/\____/_____/  /_____/_/  |_/_/  /____/  \n")
                                                    
    print("We have all the best snacks.".center(50))
    print("About this, there can be no debate.".center(50))
    print("SPECIAL: Get $1 off for every $10 spent.".center(50))

    if input("\nWould you like to view our inventory? Enter y/n: ") in ["y", "Y"]:
        printInventory(items, inventory, prices)
        while input("Would you like to continue making purchases? Enter y/n: ") in ["y", "Y"]:
            print("Enter the number of the item you desire (1-10),")
            itemSelected = int(input("or enter 0 to view inventory: "))
            if itemSelected == 0:
                printInventory(items, inventory, prices)
            else:
                howMany = int(input("How many would you like? "))
                if howMany <= inventory [itemSelected-1]:
                    total += howMany * float(prices[itemSelected-1])
                    inventory[itemSelected-1] -= howMany
                else:
                    print("Sorry there's not enough of that item.")
        if total != 0:
            print("\nYour total is $", "%.2f" %total)
            if total >= 10.0: #discount applied here
                total = total - total//10
                print("After your discount, your total is $", "%.2f" %total)
            moneyEntered = userDeposits()
            while moneyEntered < total:
                print("\nThat's not enough money!\n")
                if input("Press enter to try again or enter 'x' to cancel transaction: ") in ["x", "X"]:
                   return
                else:
                    moneyEntered = userDeposits()
            change = moneyEntered - total
            print("\nYour change is $","%.2f" %change)
            changeBills(change)
            input("\nHave a great day and enjoy the fire snacks.")
            
        else:
            input("Wow, all these good treats and you didn't want anything?")
    else:
        input("I'm not sure why you're here then...")
            
#This function prints the inventory.                
def printInventory(items, inventory, prices):
    print("\n")
    for x in range(10):
            print((str(x + 1)+".").ljust(3)+"   $"+prices[x].rjust(4)+"\t"+items[x].ljust(25)+"Inventory: "+str(inventory[x]))
    print("\n")

#This function allow the user to enter the specific bills/coins they are paying with.
#It returns the total amount of money entered
def userDeposits():
    print("\nPlease specify how you will pay.")
    twenties = int(input("How many 20s? "))
    tens = int(input("How many 10s? "))
    fives = int(input("How many 5s? "))
    ones = int(input("How many 1s? "))
    silverdollars = int(input("How many silver/Sacagawea dollars? "))
    fiftycents = int(input("How many 50 cent pieces? "))
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    return twenties*20+tens*10+fives*5+ones+silverdollars+fiftycents*.5+quarters*.25+dimes*.1+nickels*.05+pennies*.01

#This function determines the least number of bills/coins to be used when creating change.
def changeBills(change):
    monies = [20,10,5,1,.5,.25,.1,.05,.01]

    for denom in monies:
        if change/denom >= 1:
            print("Here is", int(change//denom), "$", "\b%.2f" %denom, "bill(s)/coin(s).")
            #\b escape sequence doesn't work in IDLE. Works appropriately when run as stand-alone application.
            change -= change//denom * denom

#This function creates a random inventory value for each of the 10 vending machine items.
def randInv():
    inventory = []
    for i in range(10):
        inventory.append(random.randint(1,10))

    return inventory

#Calls the plugIn function.
plugIn()
