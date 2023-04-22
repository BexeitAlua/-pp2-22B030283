from config import data
import psycopg2

sql_delete_by_name = '''
    DELETE FROM phonebook WHERE name = %s;  
'''
sql_delete_by_number = '''
    DELETE FROM phonebook WHERE number = %s;
'''

db = psycopg2.connect(**data)
cursor = db.cursor()

command = input("What do you want to delete?[name or number]: ")

if command == 'number':
    number = input("input the phone number: ")
    cursor.execute(sql_delete_by_number,(number,))
elif command == 'name':
    name = input("Input the name: ")
    cursor.execute(sql_delete_by_name,(name,))
else:
    print("There is no such command")


cursor.close()
db.commit()
db.close()