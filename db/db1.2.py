from db1 import con

a = 'ssds'
b = 25
c = 'zxcvb'
d = '12332523'


try:
    cur = con.cursor()

    ins = "INSERT INTO ROBOTA (NAME,AGE,VACANCY,NUMBER) VALUES (%s, %s, %s, %s)"
    data = (a, b, c, d)

    cur.execute(ins, data)
    con.commit()
    print("Record inserted successfully")

    con.close()
except Exception as e:
    print(e)
