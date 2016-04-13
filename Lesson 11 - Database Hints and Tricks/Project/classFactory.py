"""
classFactory: function to return tailored classes
"""

def buildRow(table, cols):
    """Build a class that creates instances of specific rows"""
    class DataRow:
        """Generic data row class, specialized by surrounding function."""
        def __init__(self, data):
            """Uses data and column names to inject attributes"""
            assert len(data) == len(self.cols)
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)
        
        def __repr__(self):
            return "{0}Record({1})".format(self.table,
                    ", ".join(["{0!r}".format(getattr(self, c)) for c in self.cols]))
        
        def retrieve(self, curs, condition = None):
            q = "SELECT {0} FROM {1}".format(", ".join(self.cols), self.table)
            if condition:
                q += " WHERE " + condition
            curs.execute(q)
            row = curs.fetchone()
            while row is not None:
                # Take values from row, make it into a a DataRow object
                yield DataRow(row)
                row = curs.fetchone()
              
    DataRow.table = table
    DataRow.cols = cols.split()
    return DataRow


if __name__ == "__main__":
    import mysql.connector
    from database import loginInfo
    db = mysql.connector.Connect(**loginInfo)
    c = db.cursor()
    testQuery = buildRow("animal", "id name family weight")
    """For some reason I cannot determine, 
    the retrieve method requires the self object 
    to be be passed explicitly as an argument.  This works, 
    but it shouldn't. I can't figure out why, or even find
    examples of other people having this problem."""
    results = testQuery.retrieve(testQuery, c)
    for res in results:
        print(res.id, res.name, res.family, res.weight)
    db.commit()
        