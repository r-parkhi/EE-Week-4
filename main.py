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
      "\nActions: add, remove, display, find, save, quit.\n" \
      "What would you like to do? Type help for more details. " + RESET)
    
    # Add item - ask for item details
    if action == "add":
      print(CYAN + "\nWhat item would you like to add?" + RESET)
      name = input("\tItem name: ").lower()
      quantity = input("\tQuantity: ")
      category = input("\tCategory: ")
      grocery.addItem(name, quantity, category)

    # Remove item - ask for item name
    elif action == "remove":
      print(CYAN + "\nWhat item would you like to remove?" + RESET)
      name = input("\tItem name: ").lower()
      grocery.removeItem(name)

    # Display list
    elif action == "display":
      grocery.displayList()

    # Find item - ask for item name
    elif action == "find":
      print(CYAN + "\nWhat item would you like to find?" + RESET)
      name = input("\tItem name: ").lower()
      grocery.findItem(name)

    # Save list - ask for file name
    elif action == "save":
      print(CYAN + "\nWhat would you like to name the file?" + RESET)
      file_name = input("\tFile name: ").lower()
      grocery.saveList(file_name)
    
    # Quit program loop
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
        "Save - save your list to a JSON file\n" \
        "Quit - quit the program"
      + RESET)


if __name__ == "__main__":
    main()