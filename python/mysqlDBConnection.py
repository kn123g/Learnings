''' Database Connection '''
import mysql.connector

#test_config = {'user': 'root', 'port':3306, 'host':'localhost','password':'root','auth_plugin':'mysql_native_password'}
#connection= mysql.connector.connect(**test_config)
connection = mysql.connector.connect(host="localhost",user="root",password="root",database="karthi")
#cursor = connection.cursor()
#cursor.execute("show Tables")
selectcursor = connection.cursor()
selectcursor.execute("select * from employee")
#for i in cursor:
  #  print(i)

for i in selectcursor:
    print(i)
    
