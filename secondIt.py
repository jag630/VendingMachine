#Jacob Goodman
#CSCI-T599 Intro to Comp and Prog
#Assignment 3
#June 21 2022 2:00pm

import random

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

    print("Welcome to the SNACK MACHINE!")
    print("We have all the best snacks. About this, there can be no debate.")

    if input("Would you like to view our inventory? Enter y/n: ") == "y":
        printInventory(items, inventory, prices)
        while input("Would you like to continue making purchases? Enter y/n: ") == "y":
            itemSelected = int(input("Enter the number of the item you desire (1-10). Enter 0 to view inventory: "))
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
            print("Your total is $", "%.2f" %total)
            moneyEntered = userDeposits()
            while moneyEntered < total:
                print("That's not enough money.")
                if input("Press enter to try again or enter 'x' to cancel transaction: ") == "x":
                   return
                else:
                    moneyEntered = userDeposits()
            change = moneyEntered - total
            print("Your change is $","%.2f" %change)
            changeBills(change)
            input("Have a great day and enjoy the fire snacks.")
            
        else:
            input("Wow, all these good treats and you didn't want anything?")
    else:
        input("I'm not sure why you're here then...")
            
                
def printInventory(items, inventory, prices):
    for x in range(10):
            print((str(x + 1)+".").ljust(3)+"   $"+prices[x].rjust(4)+"\t"+items[x].ljust(25)+"Inventory: "+str(inventory[x]))

def userDeposits():
    print("Please specify how you will pay.")
    twenties = int(input("How many 20s? "))
    tens = int(input("How many 10s? "))
    fives = int(input("How many 5s? "))
    ones = int(input("How many 1s? "))
    silverdollars = int(input("How many silver dollars? "))
    fiftycents = int(input("How many 50 cent pieces? "))
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))

    return twenties*20+tens*10+fives*5+ones+silverdollars+fiftycents*.5+quarters*.25+dimes*.1+nickels*.05+pennies*.01

def changeBills(change):
    monies = [20,10,5,1,.5,.25,.1,.05,.01]

    for denom in monies:
        if change/denom >= 1:
            print("Here is", int(change//denom), "$", "\b%.2f" %denom, "bill(s)/coin(s).")
            change -= change//denom * denom

def randInv():
    inventory = []
    for i in range(10):
        inventory.append(random.randint(1,10))

    return inventory

plugIn()
