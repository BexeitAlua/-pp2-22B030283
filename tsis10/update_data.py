from config import data
import psycopg2

sql_update_by_name = '''
    UPDATE phonebook
    SET number = %s
    WHERE name = %s;
'''
sql_update_by_number = '''
    UPDATE phonebook
    SET name = %s
    WHERE number = %s;
'''

db = psycopg2.connect(**data)
cursor = db.cursor()

command = input("What do you want to update? [name or number]: ")

if command == 'number':
    name = input("Input the name: ")
    new_number = input("New number: ")
    cursor.execute(sql_update_by_name,(new_number,name))
elif command == 'name':
    number = input("Input the number: ")
    new_name = input("New name: ")
    cursor.execute(sql_update_by_number,(new_name,number))
else:
    print("There is no such command")


cursor.close()
db.commit()
db.close()
