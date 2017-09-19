'''
Created on Sep 17, 2017

@author: nicrodriguez
'''
import mysql.connector


#looking up databases
try: 
    con = mysql.connector.connect(
        user = "root",
        password = "Baseball13#",
        host = "localhost")
except mysql.connector.Error as e:    
    print(e)
c = con.cursor()    
getDatabes = "SHOW DATABASES"
db_name = c.execute(getDatabes)
print("+---------Database List----------+")
for (db_name,) in c:
        print(db_name)


#looking up tables
db = raw_input("Databases to choose from: ")

c.close()
con.close()

try: 
    con = mysql.connector.connect(
    user = "root",
    password = "Baseball13#",
    host = "localhost",
    database = db)
except mysql.connector.Error as e:    
    print(e)
        
c = con.cursor()    
getTables = "SHOW TABLES"
table_name = c.execute(getTables)
    
print("+---------Tables in "+ db+"----------+")
for (table_name,) in c:
    print(table_name)







table = raw_input("Choose a table to update: ")
displayColumns = "SHOW COLUMNS FROM " + table
data = c.execute(displayColumns)
num_fields = len(c.description)
field_names = [i[0] for i in c.description]
columnNames = ""
for field_names in c:
    columnNames += field_names[0]+" "


print("+---------"+table +" Values---------+")
print(columnNames)
displayTable = " SELECT * FROM "+ table
data = c.execute(displayTable)
vals = ""

for data in c:
    for i in range(0,len(data)):
        vals += str(data[i])+"|"
    vals += "\n"  
    
print(vals)     
# for data in c:
#     colList = re.findall('"([^"]*)"',"".join(data))
# print(colList[1])

columns = columnNames.replace(" ", ",")
columns = columns[:-1]
print("Update table values:")
print("("+columns +")")
updatedValues = raw_input("")
parsedValues = updatedValues.split(",")
updateData = "INSERT "+ table+" VALUES ("
    
for i in range(0,len(parsedValues)):
    updateData+="%s,"
updateData = updateData[:-1]+")"
try:
    c.execute(updateData,(parsedValues))
    con.commit()
    print("Update Successfull")
except:
    print("Update Unsuccessfull")
    con.rollback()

while updatedValues != "DONE":
    updatedValues = raw_input("")
    if(updatedValues == "DONE"):
        break
    parsedValues = updatedValues.split(",")
    updateData = "INSERT "+ table+" VALUES ("
    
    for i in range(0,len(parsedValues)):
        updateData+="%s,"
    updateData = updateData[:-1]+")"
    try:
        c.execute(updateData,(parsedValues))
        con.commit()
        print("Update Successfull")
    except:
        print("Update Unsuccessfull")
        con.rollback()

c.close
con.close()







