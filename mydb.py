# Install Mysql on the computer

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'root123'

	)

#prepare a cursor object

cursorObject = dataBase.cursor()


#create a database

cursorObject.execute("CREATE DATABASE crmdata")

print("database created")