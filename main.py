from GroceryList import GroceryList

# Colors
GREEN = "\033[32m"
B_GREEN = "\033[1;32m"
CYAN = "\033[36m"
BLUE = "\033[34m"
RED = "\033[31m"
RESET = "\033[0m"


def main():
  grocery = GroceryList()

  print(B_GREEN + "\n~ Welcome to the Grocery List! ~" + RESET)
  # Loop for continuous user input
  while True:
    # Ask for an action
    action = input(GREEN +
      "\nActions: add, remove, display, find, quit.\n" \
      "What would you like to do? Type help for more details. " + RESET)
    
    # Add item - ask for item details
    if action == "add":
      print(CYAN + "\nPlease enter info about the item you'd like to add." + RESET)
      name = input("\tName: ").lower()
      quantity = input("\tQuantity: ")
      category = input("\tCategory: ")
      grocery.addItem(name, quantity, category)

    # Remove item - ask for item name
    elif action == "remove":
      print(CYAN + "\nPlease enter the item you'd like to remove." + RESET)
      name = input("\tName: ").lower()
      grocery.removeItem(name)

    # Display list
    elif action == "display":
      grocery.displayList()

    # Find item - ask for item name
    elif action == "find":
      print(CYAN + "\nPlease enter the item you'd like to find." + RESET)
      name = input("\tName: ").lower()
      grocery.findItem(name)

    # Break loop
    elif action == "quit":
      print(RED + "\nQuitting..." + RESET)
      break
    
    # Print help menu
    elif action == "help":
      print(BLUE +
        "\nAdd - add a new/existing item to your list\n" \
        "Remove - remove an item from your list\n" \
        "Display - display your list\n" \
        "Find - find an item in your list\n" \
        "Quit - quit the program"
      + RESET)


if __name__ == "__main__":
    main()