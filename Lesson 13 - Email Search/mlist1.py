"""
Sample program to list subjects by date.
"""
from database import loginInfo
import mysql.connector
from email import message_from_string

conn = mysql.connector.Connect(**loginInfo)
curs = conn.cursor()
curs.execute("SELECT msgText FROM testMessage ORDER BY msgDate")
for text, in curs.fetchall():
    msg = message_from_string(text)
    print(msg['date'], msg['subject'])