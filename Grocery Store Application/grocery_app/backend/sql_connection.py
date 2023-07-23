__cnx=None
import mysql.connector

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx=mysql.connector.connect(user='root',password='your_new_password',
                                    host='127.0.0.1',
                                    database='gs')
    return __cnx
