import mysql.connector
import config

def getConnection():
    connection = mysql.connector.connect(**config.DATABASE_CONFIG)
    return connection