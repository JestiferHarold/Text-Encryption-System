import mysql.connector as mysql
from os import sep, path, listdir, remove, mkdir, system, getenv
from shutil import rmtree

class Database:

    def __init__(self, user : str, password : str):
        
        self.database = mysql.connect(
            host = "localhost",
            user = user,
            password = password
        # database = "accounts"
        )

        self.cursor = self.database.cursor()


    def lockFolder(self, folderName : str):
        absolutePath = path.abspath(f"Accounts{sep}{folderName}")
        cmd = f'icacls "{absolutePath}{sep}asdasd.txt" /deny Everyone:(F)'
        system(cmd)

    # lockFolder("asd")

    def unlockFolder(self, folderName : str):
        relativePath = f"Accounts{sep}{folderName}"
        cmd = f'icacls "{relativePath}" /grant Everyone:(F)'
        system(cmd)

    def fetch(self) -> list:
        try:
            l = self.cursor.fetchall()
            return l
        except:
            return list([])

    def databaseExists(self) -> bool:
        self.cursor.execute("show databases")
        for x in self.cursor:
            if 'encryptiondata' in x:
                return True
        return False

    def createDatabase(self) -> bool:
        if not self.databaseExists():
            self.fetch()
            self.cursor.execute("create database encryptionData")
            return False
        return True    

    def tableExists(self) -> bool:
        self.fetch()
        self.cursor.execute("use encryptiondata")
        if self.createDatabase():
            self.fetch()
            self.cursor.execute("show tables")
            for x in self.cursor:
                if "accounts" in x:
                    return True
        return False    

    def createTable(self) -> bool:
        if not self.tableExists():
            self.fetch()
            self.cursor.execute("create table Accounts (Username varchar(225) PRIMARY KEY, Email varchar(225), Password varchar(225))")
            return False
        return True

    def checkIfUserExists(self) -> bool:
        # cursor.fetchall()
        self.cursor.execute("select * from accounts")
        for x in self.fetch():
            if not path.exists("Accounts" + sep + x[0]):
                self.createANewAccount(x[0])

    def addUser(self, username : str, email : str, password : str):
        self.fetch()
        mysqlQuery = f"insert into Accounts values ({username}, {email}, {password})"
        self.cursor.execute(mysqlQuery)
        self.cursor.commit()
        self.createANewAccount(username)

    def userLoginPractice(self, username : str, password : str):
        self.fetch()
        mysqlQuery = f"select username, password from accounts where username = '{username}'"
        self.cursor.execute()
        asd = self.fetch()
        if asd[1] == password:
            return True
        return False

    #I need new glasses I lost the other one toooo sangeeeeeeeeeee

    def changeUserName(self, oldUsername : str, newUsername : str, password : str):
        self.fetch()
        mysqlQuery = f"select username, password from accounts where username = '{oldUsername}'"
        self.cursor.execute(mysqlQuery)
        asd = self.fetch()
        if asd[1] == password:
            self.cursor.execute(f"update accounts set username = {newUsername} where username = {oldUsername}")
            return True
        return False

    def changePassword(self, userName : str, email : str, newPassword : str):
        self.fetch()
        mysqlQuery = f"select * from accounts where username = {userName}"
        self.cursor.execute(mysqlQuery)
        for x in self.cursor:
            if x[0] == userName and x[1] == email:
                mysqlQuery = f"update accounts set password  = {newPassword} where username = {userName}"
                self.cursor.execute(mysqlQuery)
                return True
        return False

    def deleteUserFromDatabase(self, userName : str, password : str, conform : bool) :
        if not conform:
            return False

        if not self.checkIfUserExists():
            return False

        self.fetch()
        mysqlQuery = f"delete from accounts where username = {userName} and password = {password}"
        self.cursor.execute(mysqlQuery)
        return True

    def createAccountsFolder(self):
        if not path.exists("Accounts"):
            mkdir("Accounts")
        
    def checkAllAccounts(self):
        self.fetch()
        self.cursor.execute("select * from accounts")
        accounts = self.fetch()
        for x in accounts:
            self.createANewAcount(x)
    
    def createANewAccount(self ,folderName : str):
        if not path.exists("Accounts" + sep + folderName):
            mkdir("Accounts" + sep + folderName)

    def deleteAAccount(self ,folderName : str):
        if path.exists("Accounts" + sep + folderName):
            rmtree("Accounts" + sep + folderName)

    def listAllFiles(self, foldername : str):
        if path.exists("Accounts" + sep + folderName):
            listdir("Accounts" + sep + folderName)

    def doesFileExists(self, folderName : str, fileName : str):
        if fileName + ".txt" in listdir("Accounts" + sep + folderName):
            return True
        return False

    def createAFile(self ,fileName : str, folderName : str):
        if not self.doesFileExists(folderName, fileName):
            with open("Accounts" + sep + folderName + sep + fileName + ".txt", "w+") as file:
                pass
        
    def createAFileWithContents(self, fileName : str, folderName : str, contents : str):
        if not self.doesFileExists(folderName, fileName):
            with open("Accounts" + sep + fileName + ".txt", "w+") as file:
                file.write(contents)

    def deleteAFile(self, fileName : str, folderName : str):
        if self.doesFileExists(folderName, fileName):
            remove(folderName + sep + fileName + ".txt")

    def readContentsFromAFile(self, folderName : str, fileName : str) -> bool:
        try:
            with open("Accounts" + sep + folderName + sep + fileName + ".txt") as file:
                return file.read()
        except:
            return False

    def lockAllFolders(self):
        self.fetch()
        mysqlQuery = f"select * from accounts"
        self.cursor.execute(mysqlQuery)
        for x in cursor:
            self.lockFolder(x[0])

# cursor.execute("use accounts")
# cursor.execute/("select * from accounts")
# lockAllFolders()

# for x in cursor:/
    # print(x)