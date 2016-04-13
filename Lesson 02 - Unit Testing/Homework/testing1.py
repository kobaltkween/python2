"""Working with unittest."""
import unittest

def title(s):
    "How close is this function to str.title()?"
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha += alpha.lower()
    title = ""
    for i,l in enumerate(s):
        if i == 0:
            title += l.upper()
        elif (s[i - 1] not in alpha) and (l in alpha):
            title += l.upper()
        else: 
            title += l
    return title

class TestTitle(unittest.TestCase):
    
    def testSingle(self):
        self.assertEqual(title("foobar"), "foobar".title(), "The result is supposed to be \"Foobar\"")
    def testMulti(self):
        s = "the hitchhiker's guide to the galaxy"
        self.assertEqual(title(s), s.title(), "The result is supposed to be the same as the str.title method.")
    def testComplex(self):
        s = "this is crazy s**t"
        self.assertEqual(title(s), s.title(), "The function should handle multiple symbols.")
    def testBadInput(self):
        self.assertRaises(TypeError, title, 300)
            
if __name__ == "__main__":
    unittest.main()