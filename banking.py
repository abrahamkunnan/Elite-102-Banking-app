import mysql.connector

sl = int(input("Type a ID: "))
slname = input("Type a Username: ")

connection = mysql.connector.connect(user = "root", database = "banks", password = "popgamer#10")

cursor = connection.cursor()

addData = ("INSERT INTO bankaccount (ID, Username) VALUES ('{}', '{}')".format (sl, slname))

returnpin = ("select PIN from bankaccount where username=('{}')".format(slname))

returnbalance =  ("select Balance from bankaccount where username=('{}')".format(slname))

cursor.execute(addData)

cursor.execute(returnpin)

for item in cursor:
    print("Your PIN is " + str(item))

cursor.execute(returnbalance)

for money in cursor:
    print("Your balance is " + str(money))

connection.commit()

cursor.close()

connection.close()