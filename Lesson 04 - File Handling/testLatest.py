import unittest
import latest
import time
import os

PATHSTEM = "v:\\workspace\\FileHandling\\src\\"

class TestLatest(unittest.TestCase):
    
    def setUp(self):
        self.path = PATHSTEM
        self.fileNames = ["file.old", "file.bak", "file.new"]
        for fn in self.fileNames:
            f = open(self.path + fn, "w")
            f.close()
            time.sleep(1)
    
    def testLatestNoNumber(self):
        """
        Ensure that calling the function with no arguments returns
        the single most recently-created file.
        """
        expected = [self.path + "file.new"]
        latestFile = latest.latest(path = self.path)
        self.assertEqual(latestFile, expected, )  \
        
    def testLatestWithArgs(self):
        """
        Ensure that calling the function with the arguments of 2 and some 
        directory  returns the two  most recently created files in the directory.
        """
        expected = set([self.path + "file.new", self.path + "file.bak"])
        latestFiles = set(latest.latest(2, self.path))
        self.assertEqual(latestFiles, expected)
        
    def tearDown(self):
        for fn in self.fileNames:
            os.remove(self.path + fn)
            
if __name__ == "__main__":
    unittest.main()