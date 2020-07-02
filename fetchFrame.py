from sqlalchemy import create_engine
import pandas as pd

def fetch(query):
    sqlEngine       = create_engine('mssql+pyodbc://WKWIN9148129/Trade?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')
    dbConnection    = sqlEngine.connect()
    frame           = pd.read_sql(query, dbConnection);
    pd.set_option('display.expand_frame_repr', False)   
    dbConnection.close()
    return frame