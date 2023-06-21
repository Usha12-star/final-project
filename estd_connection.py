
import psycopg2
def estd_connections():
    conn = psycopg2.connect(
        database ='students_data_entry',
        user ='postgres',
        password ='password',
        host ='127.0.0.1',
        port =5432
    )
    conn.autocommit = True
    print('connection established successfully')
    cursor = conn.cursor()
    return cursor