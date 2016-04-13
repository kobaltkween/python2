import unittest
import latest
import time
import os
import shutil
import zipfile

class TestZip(unittest.TestCase):
    
    def setUp(self):
        self.path = r'v:\workspace\Archives\src\zipTest'
        self.zipFilename = os.path.join(self.path, 'testZipLatest.zip')
        os.mkdir(self.path)
        self.filenames = ['old', 'newer', 'newest']
        for fn in self.filenames:
            f = open(os.path.join(self.path, fn), 'w')
            f.close()
            time.sleep(1)
        
     
    def testZipLatest(self):
        latest.zipLatest(self.zipFilename, 2, self.path)
        zf = zipfile.ZipFile(self.zipFilename, 'r')
        filesInArchive = zf.namelist()
        zf.close()
        observed = set([os.path.basename(f) for f in filesInArchive])
        expected = set(self.filenames[1:3])
        self.assertEqual(observed, expected)
        
    def tearDown(self):
        os.remove(self.zipFilename)
        try:
            shutil.rmtree(self.path, ignore_errors = True)
        except IOError:
            pass
        
if __name__ == "__main__":
    unittest.main()