import unittest
import mysql.connector
from database import loginInfo
from classFactory import buildRow

class DBTest(unittest.TestCase):
    
    def setUp(self):
        self.cols = ["id", "name", "email"]
        C = buildRow("user", " ".join(self.cols))
        self.c = C([1, "Steve Holden", "steve@holdenweb.com"])
        self.db = mysql.connector.Connect(**loginInfo)
        self.cursor = self.db.cursor()
        self.tableName = "dbTest"
        # Make sure table isn't there, so don't create duplicate data
        sql0 = "DROP TABLE IF EXISTS {0}".format(self.tableName)
        self.cursor.execute(sql0)
        sql1 = """CREATE TABLE IF NOT EXISTS {0} (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(50),
                email VARCHAR(50)) ENGINE = MYISAM;
                """.format(self.tableName)
        self.cursor.execute(sql1)
        self.db.commit()
        sql2 = """INSERT INTO {0} (name, email) VALUES (%s, %s)""".format(self.tableName)
        self.entries = [
                        ("Peter Parker", "sciencegeek@dailybugle.com"),
                        ("Barry Allen", "reallywally@starlabs.com"),
                        ("Clark Kent", "sman@dailyplanet.com"),
                        ("Steve Rodgers", "cap@shield.gov"),
                        ("Ororo Munroe", "storm@giftedyoungsters.edu"),
                        ("Cassandra Cain", "bestbatgirl@wayneindustries.com"),
                        ("Maya Lopez", "ronin@theavengers.com"),
                        ("Rachel Roth", "raven@teentitans.com"),
                        ("Jean Grey", "phoenix@giftedyoungsters.edu"),
                        ("Natasha Romanov", "bwidow@shield.gov"),
                        ("Scott Summers", "cyclops@giftedyoungsters.edu"),
                        ]
        self.cursor.executemany(sql2, self.entries)
        self.db.commit()
    
    def testRetrieve(self):
        self.dr = buildRow(self.tableName, "id name email")
        results = self.dr.retrieve(self.dr, self.cursor)
        for ent in self.entries:
            self.assertEqual(next(results).name, ent[0], "Name should be {0}".format(ent[0]))
        results = self.dr.retrieve(self.dr, self.cursor, "email LIKE '%shield.gov' ORDER BY id")
        subset = self.entries[3:10:6]
        for s in subset:
            self.assertEqual(next(results).name, s[0], "Name should be {0}".format(s[0]))
        results = self.dr.retrieve(self.dr, self.cursor, "email LIKE '%giftedyoungsters.edu' ORDER BY id")
        subset = self.entries[4:9:4]
        subset.append(self.entries[10])
        for s in subset:
            self.assertEqual(next(results).name, s[0], "Name should be {0}".format(s[0]))
    
    def tearDown(self):
        sql = "DROP TABLE IF EXISTS {0}".format(self.tableName)
        self.cursor.execute(sql)
        self.db.commit()
        self.db.close()

if __name__ == "__main__":
    unittest.main()