import mysql.connector as c
import pandas as pd
import numpy as np

mydb = c.connect(host = "localhost", user="root", passwd = "IKPatle12@$", database='mldatabase')
cursor = mydb.cursor()

pdData = pd.DataFrame()

def fetch():

    global pdData

    selectQuery = f"select * from creditData"
    cursor.execute(selectQuery)
    data = cursor.fetchall()
    pdData = pd.DataFrame(data)
    pdData = pdData.drop([0], axis = 1)
    
fetch()

print(pdData.head(1))