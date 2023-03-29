import pyodbc
from django.conf import settings

is_home = False
def get_db():
    try:
        user = settings.SQL_SERVER['user']
        pwd = settings.SQL_SERVER['pwd']
        driver = settings.SQL_SERVER['driver']
        server = settings.SQL_SERVER['server']
        database = settings.SQL_SERVER['database']

        if is_home:
            con = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='localhost', database='eHospital_NgheAn',
                                    trusted_connection='yes')
        else:
            con = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database};UID={user};PWD={pwd}')
        
        return con
    except:
        print("Không kết nối được với sql server")
        return None
        

# Query for home