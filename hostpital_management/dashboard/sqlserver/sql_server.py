import pyodbc
from django.conf import settings

def get_db():
    user = settings.SQL_SERVER['user']
    pwd = settings.SQL_SERVER['pwd']
    driver = settings.SQL_SERVER['driver']
    server = settings.SQL_SERVER['server']
    database = settings.SQL_SERVER['database']

    con = pyodbc.connect(f'''
    DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={pwd}
    ''')
    
    return con
     