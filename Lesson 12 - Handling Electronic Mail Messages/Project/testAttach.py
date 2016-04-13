import unittest
import os
import attach
import zipfile
import datetime

class TestAttach(unittest.TestCase):
    
    def setUp(self):
        self.to = 'kobaltkween@gmail.com'
        self.fileList = ['test1.jpg', 'test2.png', 'test3.mp3']
        self.testList = []
        self.path = '.\\' # Trying to put in the same folder
        for fn in self.fileList:
            fileName = os.path.join(self.path, fn)
            f = open(fileName, 'wb')
            f.close()
            self.testList.append(fileName)
        zipFn = os.path.join(self.path, 'test4.zip')
        zf = zipfile.ZipFile(zipFn, 'w', zipfile.ZIP_DEFLATED)
        for i, f in enumerate(self.testList):
            zf.write(f, self.fileList[i])      
        zf.close()
        self.testList.append(zipFn)
        self.msgText = """<h1>Big Savings Now!</h1>
                        <p>All inventory 50 to 80% off.</p>
                        <a href="www.bigstore.com">Buy Me!</a>
                        <a href="mailto:unsubscribe@bigstore.com">Unsubscribe from list</a>"""
     
    def testMsg(self):
        self.msg = attach.buildEmail(self.to, self.msgText, self.testList)
        self.date = datetime.datetime.now().strftime("%d %b %Y %H:%M")
        self.assertEqual(self.to, self.msg['To'], "Message should be sent to address given.")
        self.assertEqual('anybody@gmail.com', self.msg['From'], "From address should be anybody@gmail.com")
        self.assertTrue(self.date in self.msg['Date'], "Message date should be about the same time as date set by test.")
        types = ['text/html', 'image/jpeg', 'image/png', 'audio/mpeg', 'application/x-zip-compressed']
        msgTypes = [m.get_content_type() for m in self.msg.get_payload()]
        self.assertEqual(set(types), set(msgTypes), "File types should be as above.")
                       
    def tearDown(self):
        for f in self.testList:
            os.remove(f)
                        
if __name__ == "__main__":
    unittest.main()           