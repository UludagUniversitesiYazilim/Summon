import mysql.connector
#import os
def connection():

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Qwert12345",
        database="tuborg"
    )
        

    return conn

'''
host="0.0.0.0",
user= os.environ['mysql-user'],
passwd= os.environ['mysql-password'],
database= os.environ['mysql-database']
'''