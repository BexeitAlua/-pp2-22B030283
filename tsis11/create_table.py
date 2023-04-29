from config import data
import psycopg2

sql = '''
    CREATE TABLE phonebook2(
        name VARCHAR,
        surname VARCHAR,
        number VARCHAR(11)
    );
'''

db = psycopg2.connect(**data)
cursor = db.cursor()

cursor.execute(sql)

cursor.close()
db.commit()
db.close()