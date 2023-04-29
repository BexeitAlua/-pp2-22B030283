import psycopg2
from config import data

sql = ''' 
SELECT * FROM phonebook2 limit 1 offset 2;

CREATE OR REPLACE Function contacts(lim integer, ofs integer)
RETURNS SETOF phonebook2
AS
$$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook2 limit $1 offset $2;
END;
$$
LANGUAGE plpgsql;

SELECT * from contacts(1,2);
'''

db = psycopg2.connect(**data)
cursor = db.cursor()

limit = int(input("limit: "))
offset=int(input("offset: "))

cursor.execute(sql)

cursor.execute('SELECT * from contacts(%s,%s)',(limit,offset))
print(cursor.fetchall())

cursor.close()
db.commit()
db.close()

