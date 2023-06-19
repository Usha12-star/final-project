from estd_connection import estd_connections
cursor = estd_connections()

sql = """
CREATE TABLE INFO(
    HONOUR CHAR(10),
    FULLNAME CHA(20),
    LASTNAME CHAR(20)
    AGE INTEGER(2),
    NATIONALITY CHAR(20),
    REGISTRATION STATUS CHAR(0),
    COMPLETED COURSE INT(2),
    SEMESTERS INT(2)
  ) 
 """

cursor.execute(sql)
print("Table created successfully")