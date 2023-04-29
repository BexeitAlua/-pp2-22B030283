import psycopg2
from config import data



sql= ''' 
CREATE OR REPLACE PROCEDURE addPhone(name varchar, surname varchar, number varchar(11))
AS
$$
BEGIN
    UPDATE phonebook2
    SET number = $3
    where (phonebook2.name = $1) and (phonebook2.surname = $2);
    IF NOT FOUND THEN
        INSERT INTO phonebook2(name,surname,number) values($1,$2,$3);
    END IF;
END;
$$
LANGUAGE plpgsql;
'''
db = psycopg2.connect(**data)
cursor = db.cursor()

name = str(input("name: "))
surname=str(input("surname: "))
number = str(input("number: "))
cursor.execute(sql)
cursor.execute('CALL addPhone(%s,%s,%s)',(name,surname,number))



cursor.close()
db.commit()
db.close()
