from estd_connection import estd_connections
cursor = estd_connections()

sql = """
CREATE TABLE INFO(
    HONOUR VARCHAR(10),
    FULLNAME VARCHAR(20),
    LASTNAME VARCHAR(20),
    AGE INT,
    NATIONALITY VARCHAR(20),
    REGISTRATION_STATUS,
    COMPLETED_COURSE INT,
    SEMESTERS INT 
  ) 
 """

cursor.execute(sql)
print("Table created successfully")