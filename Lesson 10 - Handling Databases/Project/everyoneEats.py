import mysql.connector
from database import loginInfo

db = mysql.connector.Connect(**loginInfo)
cursor = db.cursor()

getCount = "SELECT COUNT(*) "
getNames = "SELECT animal.name, animal.family "
constraints = "FROM animal WHERE animal.id NOT IN (SELECT food.anid FROM food)"

cursor.execute(getCount + constraints)
if cursor.fetchone()[0]:
    print("These animals do not have feed records")
    cursor.execute(getNames + constraints)
    for row in cursor:
        print(row[0], row[1])
else:
    print("All animals have food preferences.")
db.commit()