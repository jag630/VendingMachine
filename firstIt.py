#Jacob Goodman
#CSCI-T599 Intro to Comp and Prog
#Assignment 3
#June 21 2022 2:00pm

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
    inventory = [9,8,7,8,7,9,8,7,9,5]
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
        else:
            input("Wow, all these good treats and you didn't want anything?")
    else:
        input("I'm not sure why you're here then...")
            
                
def printInventory(items, inventory, prices):
    for x in range(10):
            print((str(x + 1)+".").ljust(3)+"   $"+prices[x].rjust(4)+"\t"+items[x].ljust(25)+"Inventory: "+str(inventory[x]))

def userDeposits():
    twenties = 0
    tens = 0
    fives = 0
    ones = 0
    quarters = 0
    dimes = 0
    nickels = 0

def calcChange(total, moneyEntered):
    twenties = 0
    tens = 0
    fives = 0
    ones = 0
    quarters = 0
    dimes = 0
    nickels = 0

plugIn()
