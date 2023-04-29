import psycopg2
from config import data



sql1= ''' 
CREATE OR REPLACE PROCEDURE deletename(name varchar, surname varchar)
AS
$$
BEGIN
    DELETE from phonebook2 as p
    where (p.name = $1) and (p.surname = $2);
END;
$$
LANGUAGE plpgsql;
'''

sql2= '''
CREATE OR REPLACE PROCEDURE deletename(num varchar)
AS
$$
BEGIN
    DELETE FROM phonebook2 as p
    where (p,number=$1);
END;
$$
    LANGUAGE plpgsql;
'''




db = psycopg2.connect(**data)
cursor = db.cursor()

command =input("Delete by[name/number]: ")

if command == 'name':
    name = input("input the name: ")
    surname = input('surname: ')
    cursor.execute(sql1)
    cursor.execute('CALL deletename(%s,%s)',(name,surname))

elif command == 'number':
    number = input('num:')
    cursor.execute(sql2)
    cursor.execute('CALL deletename(%s)',(number))



cursor.close()
db.commit()
db.close()

