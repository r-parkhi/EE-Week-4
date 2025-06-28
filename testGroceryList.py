# test_grocery_list.py
# DONT CHANGE THIS FILE
# to run these tests and check if your functions work correctly
# use: py testGroceryList.py

import unittest
from GroceryList import GroceryList

class TestGroceryList(unittest.TestCase):
  def testAddItem(self):
    g = GroceryList()
    g.addItem("apple", 2, "fruits")
    self.assertEqual(g.items["apple"]["quantity"], 2)

  def testAddItemTwice(self):
    g = GroceryList()
    g.addItem("apple", 2, "fruits")
    g.addItem("apple", 3, "fruits")
    self.assertEqual(g.items["apple"]["quantity"], 5)

  def testRemoveItem(self):
    g = GroceryList()
    g.addItem("milk", 1, "drinks")
    g.removeItem("milk")
    self.assertNotIn("milk", g.items)

  def testFindItemFound(self):
    gl = GroceryList()
    gl.addItem("apple", 3, "fruit")
    result = gl.findItem("apple")
    self.assertIsNotNone(result)
    self.assertEqual(result, "apple(fruit): 3")
    
  def testFindItemNotFound(self):
    gl = GroceryList()
    result = gl.findItem("banana")  # banana isn’t in the list
    self.assertEqual(result, "banana not found")   

if __name__ == '__main__':
    unittest.main()
