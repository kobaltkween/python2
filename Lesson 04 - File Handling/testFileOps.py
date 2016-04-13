import unittest
import os
import fileops

class TestReadWriteFile(unittest.TestCase):
    
    def setUp(self):
        """ This function is run before each test"""
        self.fixtureFile = r"v:\workspace\FileHandling\src\test-read-write.txt"
        self.fixtureList = ["my", "written", "text"]
        self.fixtureListEmptyStrings = ["my", "", "", "written", "text"]
        self.fixtureListTrailingEmptyString = ["my", "written", "text", "", ""]
        
    def verifyFile(self, fixtureList):
        """Verifies that a given list, when written to a file, 
        is returned by reading the same file."""
        fileops.writeList(self.fixtureFile, fixtureList)
        observed = fileops.readList(self.fixtureFile)
        self.assertEqual(observed, fixtureList, "%s does not equal %s" % (observed, fixtureList))
    
    def testReadWriteList(self):
        self.verifyFile(self.fixtureList)
        
    def testReadWriteListEmptyStrings(self):
        self.verifyFile(self.fixtureListEmptyStrings)
    
    def testReadWriteListTrailingEmptyStrings(self):
        self.verifyFile(self.fixtureListTrailingEmptyString)
      
    def tearDown(self):
        """This function is run after each test."""
        try:
            os.remove(self.fixtureFile)
        except OSError:
            pass
        
if __name__ == "__main__":
    unittest.main() 