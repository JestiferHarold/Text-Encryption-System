import mysql.connector as mysql

database = mysql.connect(
    host = "localhost",
    user = "root",
    password = "2012"
    # database = "accounts"
)

cursor = database.cursor()

def fetch() -> list:
    try:
        l = cursor.fetchall()
        return l
    except:
        return list([])

def databaseExists() -> bool:
    cursor.execute("show databases")
    for x in cursor:
        if 'encryptiondata' in x:
            return True
    return False

def createDatabase() -> bool:
    if not databaseExists():
        fetch()
        cursor.execute("create database encryptionData")
        return False
    return True    

def tableExists() -> bool:
    fetch()
    cursor.execute("use encryptiondata")
    if createDatabase():
        fetch()
        cursor.execute("show tables")
        for x in cursor:
            if "accounts" in x:
                return True
    return False    

def createTable() -> bool:
    if not tableExists():
        fetch()
        cursor.execute("create table Accounts (Username varchar(225) PRIMARY_KEY, Email varchar(225), Password varchar(225))")
        return False
    return True

def checkIfUserExists() -> bool:
    # cursor.fetchall()
    cursor.execute("select * from accounts")
    for x in fetch():
        pass
    print(cursor)

def addUser(username : str, email : str, password : str):
    fetch()
    mysqlQuery = f"insert into Accounts values ({username}, {email}, {password})"
    cursor.execute(mysqlQuery)
    cursor.commit()

def userLoginPractice(username : str, password : str):
    fetch()
    mysqlQuery = f"select "

createTable()
addUser("asd","asd1","asd2")
checkIfUserExists()