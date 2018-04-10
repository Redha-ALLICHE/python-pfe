import sqlite3
import hashlib
import regex

class Database():
    """this class handles the creation of the users database and login verification process"""
    def __init__(self, path="users/login.db"):
        self.path = path
        self.conn = sqlite3.connect(self.path)
        self.cur = self.conn.cursor()

    def hashFunction(self, password):
        """convert password into sha256 hash"""
        return hashlib.sha256((password).encode()).hexdigest()

    def createDb(self):
        """create the database"""
        self.cur.execute(
            "CREATE TABLE USERS (id INTEGER PRIMARY KEY AUTOINCREMENT ,username TEXT NOT NULL,email TEXT)")
        self.cur.execute(
            "CREATE TABLE PASSWORDS (id INTEGER PRIMARY KEY AUTOINCREMENT ,password TEXT NOT NULL)")
        self.conn.commit()

    def closeDb(self):
        """close the connection"""
        self.conn.close()
    
    def getUsers(self):
        """retrieve an array of users"""
        usernames = []
        users = self.cur.execute("SELECT * FROM USERS")
        if users:
            for data in users:
                usernames.append(data[1])
        return usernames

    def checkInput(self, text, textOrEmail):
        """checks the validity of the input """
        if textOrEmail == "email":
            pattern = regex.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
            return regex.fullmatch(pattern, text)
        elif textOrEmail == "text":
            pattern = regex.compile(r"(^[a-zA-Z0-9.-_+]+$)")
            return regex.fullmatch(pattern, text)
        return None

    def addUser(self, username, password, email):
        """insert login informations to the database"""
        if not (self.checkInput(username, "text") and self.checkInput(password,"text")):
            print("Verify the username and password please !\nIt must consist only of numbers or letters")
            return False
        elif not self.checkInput(email, "email"):
            print("invalid email !!")
            return False
        elif username in self.getUsers():
            print("username already exists !")
            return False
        else:
            self.cur.execute("INSERT INTO USERS (username,email) VALUES (?,?)",(username,email))
            self.cur.execute("INSERT INTO PASSWORDS (password) VALUES (?)",(self.hashFunction(password),))
            print("Operation done!! ")
            return True

    def getPass(self, index):
        """get the password by the id"""
        data = self.cur.execute("SELECT * FROM PASSWORDS WHERE id = ?",(index,)).fetchall()
        if data and index:
            return data[0][1]
        else:
            return False

    def getUserid(self, username):
        """returns the username id """ 
        users = self.getUsers()
        if username in users:
            return users.index(username)+ 1
        return None

    def checkLogin(self, username, password):
        """return True if the login succeed"""
        index = self.getUserid(username)
        if self.checkInput(username,"text") and self.checkInput(password,"text"):
            if index and self.getPass(index) == self.hashFunction(password):
                print("Login successful !!!")
                return True
        print("Incorrect username or password !!!")
        return False

    def deleteUser(self, username, password):
        """delete a user from the database"""
        if self.checkLogin(username, password):
            index = self.getUserid(username)
            self.cur.execute("DELETE FROM USERS WHERE id = (?)",(index,))
            self.cur.execute("DELETE FROM PASSWORDS WHERE id= (?)",(index,))
            print("The user: " + username +" is deleted !")
            return True
        else:
            print("Error! verify the login information")
            return False

    def save(self):
        """Saves the changes done in the database"""
        self.conn.commit()
        return None


