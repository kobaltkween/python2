"""
Email message handling module: contains logic to store and retrieve
email messages using a MySQL relational database.
"""
from email import message_from_string
from email.utils import parsedate_tz, mktime_tz, parseaddr
from datetime import datetime, timedelta

def store(msg, conn, curs, table):
    """
    Stores an email message, if necessary, returning its primary key.
    """
    
    messageId = msg['message-id']
    sql1 = "SELECT msgID FROM {0} WHERE msgMessageID = %s".format(table)
    curs.execute(sql1, (messageId, ))
    result = curs.fetchone()
    if result:
        return result[0]
    date = msg['date']
    name, email = parseaddr(msg['from'])
    dt = datetime.fromtimestamp(mktime_tz(parsedate_tz(date)))
    text = msg.as_string()
    sql2 = """INSERT INTO {0} 
            (msgMessageID, msgDate, msgSenderName, msgSenderAddress, msgText) 
            VALUES (%s, %s, %s, %s, %s)""".format(table)
    curs.execute(sql2, (messageId, dt, name, email, text))
    conn.commit()
    curs.execute(sql1, (messageId, ))
    return curs.fetchone()[0]

def msgById(iD, conn, curs, table):
    """
    Return the presumably singleton message whose primary key is given
    or raise KeyError if no such message exists.
    """
    curs.execute("SELECT msgID, msgText FROM {0} WHERE msgID = %s".format(table), (iD, ))
    result = curs.fetchone()
    if not result:
        raise KeyError("Id {0} not found in store.".format(iD))
    iD, text = result
    msg = message_from_string(text)
    return iD, msg

def msgByMessageId(messageId, conn, curs, table):
    """
    Return the presumably singleton message whose "Message-ID" is given
    or raise KeyError if no such message exists.
    """
    curs.execute ("SELECT msgId, msgText FROM {0} WHERE msgMessageID = %s".format(table), (messageId, ))
    result = curs.fetchone()
    if not result:
        raise KeyError("Message-Id {0} not found in store".format(messageId))
    iD, text = result
    msg = message_from_string(text)
    return iD, msg

def msgsByDate(conn, curs, table, mindate = None, maxdate = None):
    if not (mindate or maxdate):
        raise TypeError("Must provide at least one of mindate, maxdate")
    conds = []
    data = []
    if mindate:
        conds.append("msgDate >= %s")
        data.append(mindate)
    if maxdate:
        conds.append("msgDate < %s")
        data.append(maxdate + timedelta(days = 1))
    sql = "SELECT msgID, msgText FROM {0} WHERE ".format(table)
    sql += " AND ".join(conds)
    curs.execute(sql, tuple(data))
    result = []
    for iD, text in curs.fetchall():
        result.append((iD, message_from_string(text)))
    return result

def msgs(conn, curs, table, mindate = None, maxdate = None, namesearch =  None, addsearch = None):
    """
    Return a list o fall messages sent on or after mindate and on or before maxdate.
    If mindate is not specified, there is no lower bound on the date, and similarly
    if maxdate is not specified, no upper bound.  If namesearch is given, the
    result set is restricted to messages with sender names containing that string.  If 
    addsearch is given, the result set is restricted to messages with email
    addresses containing that string.
    """
    conds = []
    data = []
    sql = "SELECT msgID, msgText FROM {0}".format(table)
    if mindate:
        conds.append("msgDate >= %s")
        data.append(mindate)
    if maxdate:
        conds.append("msgDate < %s")
        data.append(maxdate + timedelta(days = 1))
    if namesearch:
        conds.append("msgSenderName LIKE %s")
        data.append("%" + namesearch.strip().lower() + "%")
    if addsearch:
        conds.append("msgSenderAddress LIKE %s")
        data.append("%" + addsearch.strip().lower() + "%")
    if mindate or maxdate or namesearch or addsearch:
        sql += " WHERE " + " AND ".join(conds)
        curs.execute(sql, tuple(data))
    else: 
        curs.execute(sql)
    result = []
    for iD, text in curs.fetchall():
        result.append((iD, message_from_string(text)))
    return result