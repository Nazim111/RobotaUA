import psycopg2

# connection
con = psycopg2.connect(
    database="db1",
    user="user1",
    password="1111",
    host="127.0.0.1",
    port="5432"
)

print("Database opened successfully")

# create table
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS ROBOTA 
     (NAME CHAR (100) NOT NULL,
     AGE INT NOT NULL,
     VACANCY CHAR (100) NOT NULL,
     NUMBER CHAR (100) NOT NULL);''')

print("Table created successfully")


#insert data
a = 'qwe33eqwew'
b = 60
c = 'qweweQewe'
d = '99875'

cur = con.cursor()

ins = "INSERT INTO ROBOTA (NAME,AGE,VACANCY,NUMBER) VALUES (%s, %s, %s, %s)"
data = (a, b, c, d)

cur.execute(ins, data)
con.commit()
print("Record inserted successfully")

# execute data
# cur = con.cursor()
# cur.execute("SELECT NAME, AGE, VACANCY, NUMBER from ROBOTA")
# rows = cur.fetchall()
# for row in rows:
#     print("NAME =", row[0])
#     print("AGE =", row[1])
#     print("VACANCY =", row[2])
#     print("NUMBER =", row[3], '\n')
#
# print("Operation done successfully")

con.close()
