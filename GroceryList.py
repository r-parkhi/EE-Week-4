# grocery_list.py

class GroceryList:
  def __init__(self):
    self.items = {}

  def addItem(self, name, quantity, category):
    if name in self.items:
      self.items[name]["quantity"] += (quantity) # BROKEN, DOES NOT ADD INTEGERS
    else :
      self.items[name] = {
        "quantity": quantity,
        "category": category,
      }
    print(name + " added")

  def removeItem(self, name):
    if name in self.items:
      del self.items[name]
      print(name + " removed")

  def displayList(self):
    if not self.items:
      print("Your grocery list is empty!")
    else:
      print("\nYour grocery list:")
      for name, details in self.items.items():
        category = details.get("category")
        quantity = details.get("quantity")
        print(name + "(" + category + ")" + ": " + str(quantity))

  def findItem(self, name):
    if name in self.items:
      print("Found!")
      details = self.items[name]
      category = details.get("category")
      quantity = details.get("quantity")
      print(name + "(" + category + ")" + ": " + str(quantity))
    else:
      return name + "not found"