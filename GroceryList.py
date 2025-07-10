# grocery_list.py

class GroceryList:
  def __init__(self):
    self.items = {}


  # Add item to list
  def addItem(self, name, quantity, category=None):
    # add quantities
    if name in self.items:
      (self.items[name]["quantity"]) = int(self.items[name]["quantity"]) + int(quantity)

    # create new key value pairs & print item name
    else:
      self.items[name] = {
        # "quantity": int(quantity),
        "quantity": quantity,
        "category": category,
      }
    print(f"\n'{name}' added!")


  # Remove item from list
  def removeItem(self, name):
    # delete item & print "removed"
    if name in self.items:
      del self.items[name]
      print(f"\n'{name}' removed!")

    # print "not in list"
    else:
      print(f"\n'{name}' is not in your list!")


  # Display list
  def displayList(self):
    # print list
    if self.items:
      print("\n\tYour grocery list:")
      for name, details in self.items.items():
        category = details.get("category")
        quantity = details.get("quantity")
        print("\t - " + name + " (" + category + ")" + ": " + str(quantity))

    # print "empty"
    else:
      print("\nYour list is empty!")


  # Find item in list
  def findItem(self, name):
    # print details
    if name in self.items:
      print("\nFound:")
      details = self.items[name]
      category = details.get("category")
      quantity = details.get("quantity")
      print("- " + name + " (" + category + ")" + ": " + str(quantity))
      
    # print "not found"
    else:
      print(f"\n'{name}' was not found in your list!")