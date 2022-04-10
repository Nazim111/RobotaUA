import db1

cur = db1.con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS ROBOTA 
     (NAME CHAR (100) NOT NULL,
     AGE INT NOT NULL,
     VACANCY CHAR (100) NOT NULL,
     NUMBER CHAR (100) NOT NULL);''')


print("Table created successfully")
db1.con.commit()
db1.con.close()