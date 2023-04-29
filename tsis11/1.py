from config import data
import psycopg2, csv

sql = '''
    INSERT INTO phonebook2 
    Values(%s,%s,%s);
'''

db = psycopg2.connect(**data)
cursor = db.cursor()


with open("input.csv","r") as f:
    data = csv.reader(f, delimiter = ',')
    for row in data:
        cursor.execute(sql,row)


cursor.close()
db.commit()
db.close()
