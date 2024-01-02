import psycopg2
from datetime import datetime

from ..configurations.configurations import Settings

def get_settings():
    return Settings()

db_settings = get_settings()

conn = psycopg2.connect(database = db_settings.db_name, 
                        user = db_settings.db_user, 
                        host= db_settings.db_host,
                        password = db_settings.db_password,
                        port = db_settings.db_port)

class Database:
    async def get_last_uploads(total_registries: int):
        cur = conn.cursor()
        query = f"SELECT * FROM upload_dates ORDER BY upload_date DESC LIMIT {total_registries}".format(total_registries=total_registries)
        cur.execute(query=query)
        result = cur.fetchall()
        return result
    
    async def insert_upload(date: datetime):
        cur = conn.cursor()
        query = f"INSERT INTO upload_dates(upload_date) VALUES ({date})".format(date=datetime.strptime(date, '%m/%d/%y %H:%M:%S'))
        cur.execute(query=query)