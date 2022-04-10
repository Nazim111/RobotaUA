from db1 import con

cur = con.cursor()
cur.execute("SELECT NAME, AGE, VACANCY, NUMBER from ROBOTA")

rows = cur.fetchall()
for row in rows:
    print("NAME =", row[0])
    print("AGE =", row[1])
    print("VACANCY =", row[2])
    print("NUMBER =", row[3], '\n')


print("Operation done successfully")
con.close()