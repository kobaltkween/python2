"""
Demonstrates the fundamentals of unittest.
adder() is a function that lets you 'add' integers, strings, and lists.
"""

from adder import adder # keep the tested code separate from the tests

import unittest

class TestAdder(unittest.TestCase):
    
    def testNumbers(self):
        self.assertEqual(adder(3,4), 7, "3 + 4 should be 7")
    def testStrings(self):
        self.assertEqual(adder('x', 'y'), 'xy', "'x' + 'y' should be 'xy'")
    def testLists(self):
        self.assertEqual(adder([1,2], [3,4]), [1,2,3,4], "[1,2] + [3,4] should be [1,2,3,4]")
    def testNumberNString(self):
        self.assertEqual(adder(1, 'two'), '1two', "1 + 'two' should be '1two'")
    def testNumberNList(self):
        self.assertEqual(adder(4, [1, 2, 3]), [1, 2, 3, 4], "4 + [1, 2, 3] should be [1, 2, 3, 4]")   
    def testStringNList(self):
        self.assertEqual(adder('x', [1, 2, 3]), [1, 2, 3, 'x'], "'x' + [1, 2, 3] should be [1, 2, 3, 'x']")

if __name__ == "__main__":
    unittest.main()