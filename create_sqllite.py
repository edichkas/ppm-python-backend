import sqlite3
from sqlite3 import Error

class CreateDB:
    def create_db_connection(db_file):
        """ sukuriam prisijungima prie lokalios DB SQLite  
		:param db_file: DB failas
		:return: Prisijungimo prie DB objektas arba None
		"""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
