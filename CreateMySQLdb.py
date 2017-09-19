'''
Created on Sep 17, 2017

@author: nicrodriguez
'''

import mysql.connector

def createNewTable(usr,passwrd, hst, db):
    try:
        con = mysql.connector.connect(
            user = usr,
            password = passwrd,
            host = hst, 
            database = db                         
            )
    except mysql.connector.Error as e:
        print(e)
    c = con.cursor() 

    tableName = raw_input("Enter a name for the table: ")
    columnNamesUnParsed = raw_input("Enter column names (Column 1, Column 2, Column 3, etc): ")
    columnNames = columnNamesUnParsed.split(",")
    executableColList = ""
    
    for i in range(0, len(columnNames)):
        executableColList += columnNames[i]+" varchar(92), "
    
    executableColList += " PRIMARY KEY (id))"    
    tableCreate = "CREATE TABLE IF NOT EXISTS "+tableName +" (id int(11) NOT NULL AUTO_INCREMENT,"
    tableCreate += executableColList
#     print(tableCreate) 
    c.execute(tableCreate)
    return
usr = raw_input("Enter user name: ")
psswrd = raw_input("Enter Password: ")
hst = raw_input("Enter Host: ") 

try:
    con = mysql.connector.connect(
        user = usr,
        password = psswrd,
        host = hst                          
        )
except mysql.connector.Error as e:
    print(e)

print("Connected to server")    
c = con.cursor()    
db = raw_input("Enter name for new database: ")

createDB = "CREATE DATABASE IF NOT EXISTS "+db
c.execute(createDB)
print("Database Created!")
c.close()
con.close()

    
createTable = raw_input("Would you like to create a new table? (y/n): ")
isInputValid = None
if (createTable == "y") or (createTable == "Y"):
    createNewTable(usr,psswrd,hst,db)
    isInputValid = True 
    print("Table created")
elif    (createTable == "n") or (createTable == "N"): 
    print("You're done!")
    isInputValid = True
else: 
    print("Invalid Input!")
    isInputValid = None    
    
while isInputValid == None:
        print("Try Again")
        createTable = raw_input("Would you like to create a new table? (y/n): ")
        isInputValid = None
        if (createTable == "y") or (createTable == "Y"):
            createNewTable(usr,psswrd,hst,db)
            isInputValid = True 
            print("Table created!")
        elif    (createTable == "n") or (createTable == "N"): 
            print("You're done!")
            isInputValid = True
        else: 
            print("Invalid Input")
            isInputValid = None   
    
c.close()
con.close()



