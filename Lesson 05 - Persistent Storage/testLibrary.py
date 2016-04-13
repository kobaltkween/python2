import unittest
import library
import os
import glob

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.libFN = r'v:\workspace\PersistentStorage\src\lib.shelve'
        self.lib = library.Library(self.libFN)
        self.fixtureAuthor1 = library.Author('Octavia', 'Estelle', 'Butler')
        self.fixtureBook1 = library.Book('0807083100', 'Kindred', [self.fixtureAuthor1])
        self.fixtureAuthor2 = library.Author('Robert', 'Anson', 'Heinlein')
        self.fixtureBook2 = library.Book('0441790348', 'Stranger in a Strange Land', [self.fixtureAuthor2])
        self.lib.add(self.fixtureBook1)
        self.lib.add(self.fixtureBook2)
    
    def testByIsbn(self):
        observed = self.lib.getByIsbn(self.fixtureBook1.isbn)
        self.assertEqual(observed, self.fixtureBook1)
     
    def testGetByTitle(self):
        observed = self.lib.getByTitle(self.fixtureBook2.title)
        self.assertEqual(observed, self.fixtureBook2)
        
    def testGetByAuthor(self):
        observed = self.lib.getByAuthor(self.fixtureBook1.authors[0])
        self.assertEqual(observed, self.fixtureBook1)
        
    def tearDown(self):
        self.lib.close()
        shelveFiles = glob.glob(self.libFN + '*')
        for fn in shelveFiles:
            os.remove(fn)
            
            
if __name__ == "__main__":
    unittest.main()