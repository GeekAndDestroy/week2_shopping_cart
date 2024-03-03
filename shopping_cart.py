# Define function
def shopping_cart():

# Create empty dictionary to store shopping cart items in
# dict = {item: (qty, price)}
    
    cart = {}

# nested function to display shopping list later in view and quit options
    def view():
        if not cart:
            print('-'*40)
            print("Your cart is empty")
            print('-'*40)
            print('\n')
        else:
            print("Here is your shopping list:\n")
            total = 0
            print('-'*38)
            print("{:<10} {:<20} {:<10}".format("Qty", "Item", "Price"))
            print('-'*38)
            for entry in cart.keys():
                qty, item, price = cart[entry][0], entry, cart[entry][1]
                print("{:<10} {:<20} ${:<10.2f}".format(qty, item, price))
                total += qty * price
            print('-'*38)
            print(f"\t\t\tTotal: ${total:.2f}")
            print('\n')

# Use while loop to add, view, adjust, clear items until loop is terminated with quit option
    while True:

# Use prompt to choose options 
        response = input('What would you like to do? add/adjust/delete/view/quit ').lower()
        print('\n')

# When 'add' is given, ask for item name, quantity, and price, and add all to dictionary
        
        if response == 'add':
                while True:
                    add_response = input("What would you like to add? \nType 'back' to return to main menu ").title()
                    if add_response in cart.keys():
                        print(f"There are already {cart[add_response][0]} {add_response} in your cart. Please use 'adjust' to change quantity or price.")
                    elif add_response.lower() == 'back':
                        print('\n')
                        break
                    else:
                        while True:
                            add_qty = input(f"How many {add_response} would you like to add? ")
                            try:  # Input validation to ensure
                                add_qty = int(add_qty)
                                break
                            except ValueError:
                                print("Please enter a valid numeric value for quantity.")
                        while True:
                            add_price = input(f"How much does a single {add_response} cost? ")
                            try:
                                add_price = float(add_price)
                                break
                            except ValueError:
                                print("Please enter a valid numeric value for price.")

                        cart[add_response] = [add_qty, add_price]
                        print(f"{add_qty} {add_response} have been added to your cart at ${add_price:.2f}\n")
                        break
                    break

# When 'adjust' is given, ask which item to adjust, then if changing qty or price. take in each accordingly and update dicionary
        elif response == 'adjust':
            while True:
                adjust_response = input("What item would you like to adjust?  \nType 'back' to return to main menu ").title()
                if adjust_response not in cart.keys():
                    print(f"There are no {adjust_response} in your cart. Please check spelling and try again\n")
                elif adjust_response.lower() == 'back':
                        break
                else:
                    adjust_response2 = input(f"What would you like to change for {adjust_response}? qty/price ").lower()
                    if adjust_response2 == 'qty':
                        while True:
                            adjust_qty = input(f"How many {adjust_response} would you like in your cart? ")
                            try:
                                adjust_qty = int(adjust_qty)
                                break
                            except ValueError:
                                print("Please enter a valid numeric value for quantity.")
                        cart[adjust_response][0] = adjust_qty
                        print(f"There are now {cart[adjust_response][0]} in your cart\n")
                        break
                    elif adjust_response2 == 'price':
                        while True:
                            adjust_price =input(f"What is the new price for {adjust_response}? ")
                            try:
                                adjust_price = float(adjust_price)
                                break
                            except ValueError:
                                print("Please enter a valid numeric value for price.")
                        cart[adjust_response][1] = adjust_price
                        print(f"The price for {adjust_response} is now ${cart[adjust_response][1]:.2f}\n")
                        break
                    else:
                        print("Invalid response. Please try again.")

 # When delete is given ask if user wants to clear entire list or just one item.  Ask for verification, and clear or delete item accordingly
        elif response == 'delete':
            while True:
                del_response = input("Would you like to delete a single 'item' from your list, or 'clear' list? Please choose: 'item'/'clear' \nType 'back' to return to main menu ").lower()
                if del_response == 'back':
                    break
                elif del_response == 'item':
                    del_item = input("What item would you like to remove from your cart? ").title()
                    if del_item in cart.keys():
                        del_verification = input("This action can not be undone.  Are you sure you would like to proceed? y/n ").lower()
                        if del_verification == 'y':
                            del cart[del_item]
                            print(f"All {del_item} have been removed from your cart.\n")
                            break
                        elif del_verification == 'n':
                            print("Nothing will be removed from your cart.\n")
                            break 
                        else:
                            print("Invalid response. Please try again.")
                    else:
                        print("Invalid response. Please try again.")       
                
                elif del_response == 'clear':
                    del_verification = input("This action can not be undone.  Are you sure you would like to proceed? y/n ").lower()
                    if del_verification == 'y':
                        cart.clear()
                        print("Your cart is now empty\n")
                        break
                    elif del_verification == 'n':
                        print("Nothing will be removed from your cart.\n")
                        break
                    else:
                        print("Invalid response. Please try again.")  
                else:
                    print("Invalid response. Please try again.") 
                
# When 'view' is given, run view function
        elif response == 'view':
            view()
        
# When 'quit' is given, give user final message, run view function, and break loop
        elif response == 'quit':
            while True:
                quit_response = input("Are you sure you would like to quit? y/n ").lower()
                if quit_response == 'y':
                    print("Thank you for using our shopping cart program.\nYour final shopping list is below.\nHave a nice day!\n")
                    view()
                    return
                elif quit_response == 'n':
                    print("Thanks for sticking around!\n")
                    break
                else:
                    print("Invalid response. Please try again.")
        
# If invalid response is given for prompt, tell user to try again
        else:
            print("Invalid response. Please try again.")

"""
       .------..
     -          -
   /              \ 
 /                   \ 
/    .--._    .---.   |
|  /      -__-     \   |
| |                 |  |
 ||     ._   _.      ||
 ||      o   o       ||
 ||      _  |_      ||
 C|     (o\_/o)     |O     Uhhh, this computer
  \      _____      /       is like, busted or
    \ ( /#####\ ) /       something. So go away.
     \  `====='  /
      \  -___-  /
       |       |
       /-_____-\ 
     /           \ 
   /               \ 
  /__|  AC / DC  |__\ 
  | ||           |\ \ 
"""

# Run program
shopping_cart()