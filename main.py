#Name: Whitt Hyde
#HW no. and Name: HW 9 Diner - New System
#Due Date: 11/13/2017
#Program Description: The main function calling classses Pizza Slice Entree Plain Burer and Dexlue Burger

#Defining Constants for our program
PIZZA_SLICE = 1
PLAIN_BURGER = 2
DELUXE_BURGER = 3
COMPLETE_ORDER = 4
TAX_RATE = 0.0825
YES = 'Y'
NO = 'N'

#import our files
import entree
import pizzaslice
import plainburger
import deluxeburger

def main():
    
    #establishes the list for objects
    items_purchased = []

    #initialize total items purchases
    total_items = 0
    subtotal = 0
    #prints menu
    print_menu()

    #asks the user for their choice
    option = get_user_option()

    #initiates the while loop for action
    while option != COMPLETE_ORDER:
        #option 1 of the while loop
        if option == PIZZA_SLICE:
            #asks user for qty
            buy_qty = get_amount()
            #asks user how many toppings they would like
            top = int(input("How many toppings would you like?: "))
            while top < 0:
                top = int(input("Invalid amount (must be positive or 0). How many toppings would you like?: "))

            #creates instance of pizza object
            pizza_order = pizzaslice.PizzaSlice("Pizza Slice(s)",buy_qty,top)

            #adds order to the list
            items_purchased.append(pizza_order)

            #adds to total count
            total_items += buy_qty

            
        elif option == PLAIN_BURGER:
            #asks user for qty
            buy_qty = get_amount()
            #asks user for size desired
            what_size = int(input("What size (oz) burger would you like? (Please enter integer 6, 8, or 10): "))
            while not (what_size == 6 or what_size == 8 or what_size == 10):
                what_size = int(input("Invalid amount (must enter either 6,8, or 10). What size (oz) burger would you like? (Please enter integer 6, 8, or 10): "))                

            #creates instance of burger object
            burger_order = plainburger.PlainBurger("Plain Burger", buy_qty, what_size)

            #sets price
            burger_order.set_price()
                
            #adds order to the list
            items_purchased.append(burger_order)

            #adds to total count
            total_items += buy_qty


        elif option == DELUXE_BURGER:
            #asks user for qty
            buy_qty = get_amount()
            #asks user for size desired
            what_size = int(input("What size (oz) burger would you like? (Please enter integer 6, 8, or 10): "))
            while not (what_size == 6 or what_size == 8 or what_size == 10):
                what_size = int(input("Invalid amount (must enter either 6,8, or 10). What size (oz) burger would you like? (Please enter integer 6, 8, or 10): "))

            #creates instance of deluxe burger object
            deluxe_order = deluxeburger.DeluxeBurger("Deluxe Burger",buy_qty,what_size)

            #sets price
            deluxe_order.set_price()
            
            #asks about toppings
            #using if isinstance to filter out only deluxe for these methods
            if isinstance(deluxe_order, deluxeburger.DeluxeBurger):
                cheese = input("Would you like cheese? (Please enter 'Y' or 'N'): ")
                #validation loop
                while not (cheese == YES or cheese == NO):
                    cheese = input("Error. Please enter the letter 'Y' or 'N'")
                #removes cheese if the user asks
                if cheese == NO:
                    deluxe_order.remove_cheese()
                #asks user to remove bacon
                bacon = input("Would you like bacon? (Please enter 'Y' or 'N'): ")
                #validation loop
                while not (bacon == YES or bacon == NO):
                    bacon = input("Error. Please enter the letter 'Y' or 'N'")
                #removes bacon if the user asks
                if bacon == NO:
                    deluxe_order.remove_bacon()
                #asks user to remove avocado
                avocado = input("Would you like avocado? (Please enter 'Y' or 'N'): ")
                #validation loop
                while not (avocado == YES or avocado == NO):
                    avocado = input("Error. Please enter the letter 'Y' or 'N'")
                #removes avocado if the user asks
                if avocado == NO:
                    deluxe_order.remove_avocado()
                
            #adds order to the list
            items_purchased.append(deluxe_order)
            
            #adds to total count
            total_items += buy_qty

    
        #prints blank line and menu
        print("")
        print_menu()
        #calls choice again for the while loop
        option = get_user_option()
        #print blank line
        print('')

    #printing our summary
    if option == COMPLETE_ORDER:
        if total_items > 0:
            #initializing subtotal
            sbtotal = 0
            #for loop to calculate our subtotal
            for y in items_purchased:
                money = float(y.calc_cost())
                sbtotal += money
            #for loop to print items in the list
            for x in items_purchased:
                print(x)
            print("Total Entrees purchased:",total_items)
            #formats sbtotal
            subtotally = format(sbtotal,'.2f')
            print("Subtotal: $", subtotally,sep ='')
            print("Tax Amount: $",calculate_tax(sbtotal),sep='')
            #calculates our total due
            total = float(sbtotal) + float(calculate_tax(sbtotal))
            total = format(total,'.2f')
            print("Total Due: $",total,sep='')
        else:
            print("No items purchased. Please come back later to try our great food! Thank you for visiting!")
            

#defines our menu function
def print_menu():
    #menu title
    print("ENTREE MENU")
    print("1. Pizza Slice(s)")
    print("2. Plain Burger")
    print("3. Deluxe Burger")
    print("4. Complete Order.")
    print("") #prints blank line

#defines getting user menu option
def get_user_option():
    option = int(input("Please select a menu option (1-4): ")) #asks user for option

    #validates the user option
    while not (option == PIZZA_SLICE or option == PLAIN_BURGER or option == DELUXE_BURGER or option == COMPLETE_ORDER):
        option = int(input("Invalid menu entry. You must enter a number 1-4. Try again:"))

    #returns the option
    return option

#defining the qty entered by user
def get_amount():
    option = int(input("Please enter how many you would like (must be positive): ")) #asks user for how much

    #validates the user option
    while option <= 0:
        option = int(input("Error amount must be positive. Please enter how many you would like: "))
    
    #returns the option
    return option

#calculate the tax
def calculate_tax(sub):
    tax = sub * TAX_RATE
    tax = format(tax,'.2f')
    return tax

main()




