import psycopg2
import logging
from psycopg2 import Error


class Database:
    def __init__(self):
        # connecting to existing database
        self.connection = psycopg2.connect(database="db1",
                                           user="user1",
                                           password="1111",
                                           host="127.0.0.1",
                                           port="5432")

        self.cursor = self.connection.cursor()

        self.create_table()
        self.execute_data()

    def create_table(self):
        self.cursor = self.connection.cursor()

        sql = '''CREATE TABLE IF NOT EXISTS ROBOTA 
                 (NAME CHAR (100) NOT NULL,
                 AGE INT NOT NULL,
                 VACANCY CHAR (100) NOT NULL,
                 NUMBER CHAR (100) NOT NULL);'''

        self.cursor.execute(sql)
        self.connection.commit()

    def add_record(self, ):
        a = 'AAZA'
        b = 50
        c = 'QwErr'
        d = '74584435435'

        ins = "INSERT INTO ROBOTA (NAME,AGE,VACANCY,NUMBER) VALUES (%s, %s, %s, %s)"
        data = (a, b, c, d)

        self.cursor = self.connection.cursor()
        self.cursor.execute(ins, data)
        self.connection.commit()

    def execute_data(self, cursor):
        asd = self.cursor
        asd.execute("SELECT NAME, AGE, VACANCY, NUMBER from ROBOTA")
        rows = cursor.fetchall()
        for row in rows:
            print("NAME =", row[0])
            print("AGE =", row[1])
            print("VACANCY =", row[2])
            print("NUMBER =", row[3], '\n')

        self.cursor.close()

    def work(self):
        self.__init__()
        self.create_table()
        self.execute_data()
