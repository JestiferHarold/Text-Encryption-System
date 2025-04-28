import mysql.connector as mysql
from os import sep, path, listdir, remove, mkdir, rmdir
# from base64 import 
# from pylocker import ServerLocker

#02121956

database = mysql.connect(
    host = "localhost",
    user = "root",
    password = "2012"
    # database = "accounts"
)

cursor = database.cursor()

locker = ServerLocker()

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
    mysqlQuery = f"select username, password from accounts where username = '{username}'"
    cursor.execute()
    asd = fetch()
    if asd[1] == password:
        return True
    return False

def changeUserName(oldUsername : str, newUsername : str, password : str):
    fetch()
    mysqlQuery = f"select username, password from accounts where username = '{oldUsername}'"
    cursor.execute(mysqlQuery)
    asd = fetch()
    if asd[1] == password:
        cursor.execute(f"update accounts set username = {newUsername} where username = {oldUsername}")
        return True
    return False

def createAccountsFolder():
    if not path.exists("Accounts"):
        mkdir("Accounts")
    
def checkAllAccounts():
    fetch()
    cursor.execute("select * from accounts")
    accounts = fetch()
    for x in accounts:
        pass

def createANewAccount(folderName : str):
    if not path.exists("Accounts" + sep + folderName):
        mkdir()

def deleteAAccount(folderName : str):
    if path.exists("Accounts" + sep + folderName):
       rmdir()

def listAllFiles(fileName : str):
    if path.exists("Accounts" + sep + fileName):
        listdir()

def doesFileExists(folderName : str, fileName : str):
    if fileName + ".txt" in listdir("Accounts" + sep + folderName):
        return True
    return False

def createAFile(fileName : str, folderName : str):
     if not doesFileExists(folderName, fileName):
        with open("Accounts" + sep + fileName + ".txt") as file:
            pass
    
def createAFileWithContents(fileName : str, folderName : str, contents : str):
     if not doesFileExists(folderName, fileName):
        with open("Accounts" + sep + fileName + ".txt") as file:
            file.write(contents)

def deleteAFile(fileName : str, folderName : str):
    if doesFileExists(folderName, fileName):
        remove(folderName + sep + fileName + ".txt")

createTable()
addUser("asd","asd1","asd2")
checkIfUserExists()