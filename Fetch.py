import mysql.connector
from mysql.connector import Error
import pyodbc


def fetch(query):
    try:
        connection = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                "Server=WKWIN9148129;"
                                "Database=Trade;"
                                "Trusted_Connection=yes;")
        
        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()     
        return records
    except Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        #if (connection.is_connected()):
        connection.close()       
        print("MySQL connection is closed")