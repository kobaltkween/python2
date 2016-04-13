"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""

import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        os.chdir(self.dirname)
        
    def test1(self):
        "Verify creation of files is possible"
        files = ("this.txt", "that.txt", "theOther.txt")
        for filename in files:
            f = open(filename, "w")
            f.write("Some text\n")
            f.close()
            self.assertTrue(f.closed)
        "Verify that only the files in the directory are the ones created"
        allFiles = os.listdir()
        self.assertEqual(sorted(list(files)), sorted(list(allFiles)), "The list of files created and the list of all files should be the same.")
    
    def test2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [], "Directory not empty")
        
    def test3(self):
        fb = open("testbin.dat", "wb")
        fb.write(b'0' * 1000000)
        fb.close()
        statinfo = os.stat("testbin.dat")
        self.assertEqual(statinfo.st_size, 1000000, "Size should be exactly 1,000,000 bytes.")

    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
        
        
if __name__ == "__main__":
    unittest.main()