from config import data
import psycopg2

sql = '''
    INSERT INTO phonebook2 VALUES(DEFAULT,%s, %s);
'''

db = psycopg2.connect(**data)
cursor = db.cursor()


l = [["a",87018486232],["b",5343534]]
for i in range(len(l)):
    if 87000000000<l[i][1]<87790000000:
        cursor.execute(sql,(l[i][0],l[i][1]))
    else:
        print("ERROR!")

cursor.close()
db.commit()
db.close()