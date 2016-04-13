import unittest
import archivenr
import zipfile
import os
import shutil

class testArchiveNR(unittest.TestCase):

    def setUp(self):
        self.home = os.getcwd()
        self.path = r'v:/workspace/ziptest'
        os.mkdir(self.path)
        self.filenames = ['me.txt', 'myself.bak', 'i.inc', 'you', 'yours.txt', 'now.bar']
        for fn in self.filenames:
            f = open(os.path.join(self.path, fn), 'w')
            f.close()
        subdirs = ['sub1A', 'sub2A', 'sub3A']
        subfiles = ['test1.txt', 'test2.txt']
        for d in subdirs:
            os.mkdir(os.path.join(self.path, d))
            for file in subfiles:
                fn = d + file
                f = open(os.path.join(self.path, d, fn), 'w')
                f.close()

    def testZip(self):
        #Get the zip file
        self.assertTrue(os.path.exists(archivenr.zipDir(self.path)), "No zip file created")
        myZip = zipfile.ZipFile(archivenr.zipDir(self.path))
        observed = myZip.namelist()
        myZip.close()
        expected = ['ziptest/' + fn for fn in self.filenames]
        self.assertEqual(set(expected), set(observed), "File list should be the same")
                
    def tearDown(self):
        os.chdir(self.home)
        shutil.rmtree(self.path)
       

if __name__ == "__main__":
    unittest.main()