"""
Read in and parse email messages to verify readability.
NOTE: This test creates a test message table.
"""

from glob import glob
from email import message_from_string
import mysql.connector as msc
from database import loginInfo
import maildb
import unittest
import datetime
from email.utils import parsedate_tz, mktime_tz

conn = msc.Connect(**loginInfo)
curs = conn.cursor()
TBLNM = "testMessage"
TBLDEF = """\
CREATE TABLE {0} (
    msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
    msgMessageID VARCHAR(128),
    msgDate DATETIME,
    msgSenderName VARCHAR(128),
    msgSenderAddress VARCHAR(128),
    msgText LONGTEXT
) ENGINE = INNODB""".format(TBLNM)
FILESPEC = "C:/PythonData/*.eml"

class testRealEmailTraffic(unittest.TestCase):
    def setUp(self):
        """
        Reads an arbitrary number of mail messages and
        stores them in a brand new messages table.
        """
    
        self.conn = msc.Connect(**loginInfo)
        self.curs = self.conn.cursor()
        self.curs.execute("DROP TABLE IF EXISTS {0}".format(TBLNM))
        self.conn.commit()
        curs.execute(TBLDEF)
        conn.commit()
        files = glob(FILESPEC)
        self.msgIds = {} # Keyed by messageId
        self.messageIds = {} # Keyed by id
        self.msgdates = []
        self.rowcount = 0
        for f in files:
            ff = open(f)
            text = ff.read()
            msg = message_from_string(text)
            iD = self.msgIds[msg['message-id']] = maildb.store(msg, self.conn, self.curs, TBLNM)
            self.messageIds[iD] = msg['message-id']
            date = msg['date']
            self.msgdates.append(datetime.datetime.fromtimestamp(mktime_tz(parsedate_tz(date))))
            self.rowcount += 1 # Assuming no duplicated Message-IDs
            ff.close()
            
    def testNotEmpty(self):
        """
        Verify that the setUp method actually created some messages.
        If it finds no files there will be no messages in the table,
        the loop bodies in the other tests will never run, and potential
        errors will never be discovered.
        """
        curs.execute("SELECT COUNT(*) FROM {0}".format(TBLNM))
        messagect = curs.fetchone()[0]
        self.assertGreater(messagect, 0, "Database message table is empty")
        
    def testMessageIds(self):
        """
        Verify that items retrieved by id have the correct Message-ID.
        """ 
        for messageId in self.msgIds.keys():
            pk, msg = maildb.msgById(self.msgIds[messageId], self.conn, self.curs, TBLNM)
            self.assertEqual(msg['message-id'], messageId)
    
    def testIds(self):
        """
        Verify that items retrieved by messageId hvae the correct Message-ID.
        """
        for iD in self.messageIds.keys():
            pk, msg = maildb.msgByMessageId(self.messageIds[iD], self.conn, self.curs, TBLNM)
            self.assertEqual(msg['message-id'], self.messageIds[iD])
    
    def testDates(self):
        """
        Verify that retrieving records between the minimum and maximum dates
        retrieves the appropriate number of records.
        """
        mind = min(self.msgdates)
        mindate = datetime.date(mind.year, mind.month, mind.day)
        maxd = max(self.msgdates)
        maxdate = datetime.date(maxd.year, maxd.month, maxd.day)
        self.assertEqual(self.rowcount, 
                         len(maildb.msgs(self.conn, self.curs, TBLNM, mindate = mindate, 
                            maxdate = maxdate)))
    
    def tearDown(self):
        #curs.execute("DROP TABLE IF EXISTS {0}".format(TBLNM))
        self.conn.close()
        
if __name__ == "__main__":
    unittest.main()