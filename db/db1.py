import psycopg2

con = psycopg2.connect(
   database="db1",
   user="user1",
   password="1111",
   host="127.0.0.1",
   port="5432"
)

print("Database opened successfully")