from GroceryList import GroceryList

def main():
  grocery = GroceryList()

  print("\nWelcome to the Grocery List!")
  while True:
    action = input("\nPlease choose an action by #:\n 1. display list\n 2. add item\n 3. remove item\n 4. find item\n 5.  quit program\n")
    if action == "1":
      grocery.displayList()

    elif action == "2":
      name = input("Name: ")
      quantity = input("Quantity: ")
      category = input("Category: ")
      grocery.addItem(name, quantity, category)

    elif action == "3":
      name = input("Name: ")
      grocery.removeItem(name)

    elif action == "4":
      grocery.findItem("apple")

    elif action == "5":
        print("Quitting...")
        break


if __name__ == "__main__":
    main()