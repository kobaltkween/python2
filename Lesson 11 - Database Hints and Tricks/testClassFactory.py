import unittest
from classFactory import buildRow

class DBTest(unittest.TestCase):
    
    def setUp(self):
        C = buildRow("user", "id name email")
        self.c = C([1, "Steve Holden", "steve@holdenweb.com"])
    
    def testAttributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "Steve Holden")
        self.assertEqual(self.c.email, "steve@holdenweb.com")
    
    def testRepr(self):
        self.assertEqual(repr(self.c), 
                         "userRecord(1, 'Steve Holden', 'steve@holdenweb.com')")

if __name__ == "__main__":
    unittest.main()