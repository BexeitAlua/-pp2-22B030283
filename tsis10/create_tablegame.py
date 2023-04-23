from config import data
import psycopg2

sql = '''
    CREATE TABLE users(
        id NUMERIC primary key,
        username VARCHAR,
        score INTEGER,
        highscore INTEGER,
        level INTEGER
    );
'''

db = psycopg2.connect(**data)
cursor = db.cursor()

cursor.execute(sql)

cursor.close()
db.commit()
db.close()
