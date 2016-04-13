"""
Create the food table and add all the necessary data.
Note that the foods are identified by the animal's
name and family, so we have to look up the primary key.
"""

import mysql.connector
from database import loginInfo

db = mysql.connector.Connect(**loginInfo)
cursor = db.cursor()
cursor.execute("""DROP TABLE IF EXISTS food""")
cursor.execute("""
    CREATE TABLE food (
        id INTEGER PRIMARY KEY AUTO_INCREMENT,
        anid INTEGER,
        feed VARCHAR(20),
        FOREIGN KEY (anid) REFERENCES animal(id)) ENGINE = MYISAM
    """)

data = [('Ellie', 'Elephant', ['hay', 'peanuts']),
        ('Gerald', 'Gnu', ['leaves', 'shoots']),
        ('Gerald', 'Giraffe', ['hay', 'grass']),
        ('Leonard', 'Leopard', ['meat']),
        ('Sam', 'Snake', ['mice', 'meat']),
        ('Steve', 'Snake', ['mice', 'meat', 'insects', 'spiders']),
        ('Zorro', 'Zebra', ['grass', 'leaves'])]

for name, family, foods in data:
    cursor.execute("SELECT id FROM animal WHERE name = %s and family = %s", 
                (name, family))
    ii = cursor.fetchone()[0]
    for food in foods:
        cursor.execute("""INSERT INTO food (anid, feed)
                        VALUES (%s, %s)""", (ii, food))
    db.commit()
    print("Processed", name, family, ii)