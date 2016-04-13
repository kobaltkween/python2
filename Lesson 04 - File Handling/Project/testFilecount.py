import unittest
import filecount
import shutil
import os
import glob

class TestFileList(unittest.TestCase):
    def setUp(self):
        self.path = ""
        self.fileNames = []
            
    def testFullDir(self):
        """
        See if get the proper dictionary from a directory full of files
        """
        self.path = ".\\tmp\\"
        if not os.path.exists(self.path):
            os.makedirs(self.path)
        self.fileNames = ["file1.txt", "file2.txt", "file3.txt", "file4.doc", "file5.doc", "file6.py", "file7.py", "file8.bak"]
        for fn in self.fileNames:
            f = open(self.path + fn, "w")
            f.close()
        os.mkdir(os.path.join(self.path, 'aaa.bbb'))
        expected = {'.txt' : 3, '.doc' : 2, '.py' : 2, '.bak' : 1}
        fileDict = filecount.count(self.path)
        self.assertEqual(expected, fileDict, "The count method should count all the created files correctly.")   
        
    def testEmptyDir(self):
        """
        See if get appropriate response from empty directory
        """
        self.path = ".\\tmp2\\"
        os.makedirs(self.path)
        expected =  "There are no files in the directory."
        files = filecount.count(self.path)
        self.assertEqual(files, expected, "The method should return a message about there being no files.")
         
    def testWrongDir(self):
        """
        See if properly handle a directory that doesn't exit
        """
        self.path = ".\\foo\\"
        expected =  "The directory does not exist."
        files = filecount.count(self.path)
        self.assertEqual(files, expected, "The method should return a message about the directory not existing.")
        
    def tearDown(self):
        if  os.path.exists(self.path):
            shutil.rmtree(self.path)
            
if __name__ == "__main__":
    unittest.main()