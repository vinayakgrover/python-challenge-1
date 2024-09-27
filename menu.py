# menu.py

# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("\nFrom which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ").strip()

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Convert the customer's input to an integer
        menu_category = int(menu_category)
        if menu_category in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[menu_category]
            # Print out the menu category name they selected
            print(f"\nYou selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"\nWhat {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("\nItem # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        item_name = f"{key} - {key2}"
                        num_item_spaces = 24 - len(item_name)
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {item_name}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": item_name,
                            "Price": value2
                        }
                        i += 1
                else:
                    item_name = key
                    num_item_spaces = 24 - len(item_name)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {item_name}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": item_name,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_item_selection = input("\nWhat do you want to eat: ").strip()

            # 3. Check if the customer typed a number
            if menu_item_selection.isdigit():
                # Convert the menu selection to an integer
                menu_item_selection = int(menu_item_selection)

                # 4. Check if the menu selection is in the menu items
                if menu_item_selection in menu_items:
                    # Store the item name as a variable
                    item_name = menu_items[menu_item_selection]["Item name"]
                    item_price = menu_items[menu_item_selection]["Price"]
                    # Ask the customer for the quantity of the menu item
                    quant = input(f"How many {item_name} would you like? ").strip()

                    # Check if the quantity is a number, default to 1 if not
                    if quant.isdigit():
                        quant = int(quant)
                    else:
                        quant = 1

                    # Add the item name, price, and quantity to the order list
                    order.append({
                        "Item name": item_name,
                        "Price": item_price, 
                        "Quantity": quant
                    })

                    # Tell the customer that their input isn't valid
                    print(f"Added {quant} x {item_name} to your order.")
                else:
                    print(f"{menu_item_selection} was not a valid item number mate.")
            else:
                print(f"{menu_item_selection} was not a valid item number mate.")
        else: 
            print("You didn't select a valid number.")
            # Tell the customer they didn't select a menu option
    else:
        # Tell the customer they didn't select a number
        print(f"{menu_category} was not a menu option.")
        
    # 5. Check the customer's input using match-case
    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("\nWould you like to keep ordering? (Y)es or (N)o: ").strip().lower()
        match keep_ordering:
            case 'y' | 'yes':
                break  # Continue ordering
            case 'n' | 'no':
                place_order = False  # End the ordering process
                print("Thank you for your order!")
                break  # Exit the loop
            case _:
                print("Please press 'Y' for yes or 'N' for no.")

# Print out the customer's order
print("\nThis is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
# print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item in order:
    # 7. Store the dictionary items as variables
    item_name = item["Item name"]
    item_price = item["Price"]
    item_quantity = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 24 - len(item_name)
    # 9. Create space strings
    item_spaces = " " * num_item_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces} | ${item_price:.2f} | {item_quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum() and print the prices.
total_cost = sum(item["Price"] * item["Quantity"] for item in order)
print("--------------------------|--------|----------")
print(f"Total: ${total_cost:.2f}")
