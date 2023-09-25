import mysql.connector as c
import pandas as pd

mydb = c.connect(host = "localhost", user="root", passwd = "IKPatle12@$", database='mldatabase')
cursor = mydb.cursor()

def insert( row, i ):

    ins = f"{i}, ";
    for r in row:
        ins += f"{r},"

    ins = ins[:-1]

    insertQuery = f"insert into creditData values({ins})"
    cursor.execute(insertQuery)
    mydb.commit()

def readcsv():

    data = pd.read_csv("./CreditCardDefault.csv")
    data = data.values

    i = 0
    for row in data:

        insert(row, i)
        i+= 1
    
    print("CSV Data Inserted Sucessfully.")

readcsv()
