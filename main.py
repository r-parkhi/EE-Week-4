from GroceryList import GroceryList

def main():
  grocery = GroceryList()

  print("No main!")
  grocery.addItem("item", 0, "category")
  grocery.removeItem("item")
  grocery.displayList()
  grocery.findItem("item")
  # ask user for their choice 
  # use a loop to ask for constant input 
  # use conditionals

if __name__ == "__main__":
    main()