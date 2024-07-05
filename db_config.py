# For direct db Connection 
import pyodbc
import pandas as pd
from dotenv import load_dotenv, find_dotenv
import os

# load dotenv 
load_dotenv(find_dotenv())
# print(os.getenv('DB_SERVER'))
con_string = 'DRIVER=ODBC Driver 18 for SQL Server;'+'SERVER='+os.getenv('DB_SERVER') +';'+'Database='+os.getenv('DB_NAME') +';'+'UID='+os.getenv('DB_USERNAME') +';' +'PWD='+os.getenv('DB_PWD') +';'
# print(con_string) #for debugging only
global conn 
conn = pyodbc.connect(con_string)

# Only works on sql query
def get_data(sql:str):
    df = pd.read_sql(sql=sql, con=conn)
    # print(df)
    return df.to_json(indent=4, date_format='iso' ,index=False, orient='records')