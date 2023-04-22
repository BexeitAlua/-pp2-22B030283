from config import data
import psycopg2

sql = '''
    INSERT INTO phonebook
    VALUES(%s,%s)
'''

db = psycopg2.connect(**data)
cursor = db.cursor()

print("Please enter information about contact:")
name = input("Name:")
number = int(input("Number:"))

cursor.execute(sql,(name,number))

cursor.close()
db.commit()
db.close()