class books:
    def __init__(self):
        self.bookList = {}
    def readBooks(self, fileLocation):
        bookFile = 0
        try:
            bookFile = open(fileLocation)
        except:
            print("Can't open file")
            return False
        for i in bookFile:
            j = i.strip("\r\n").strip("\n")
            if not self.checkAvailability(j):
                self.bookList[j] = ""
        bookFile.close()
        return True
    def printBooks(self):
        print("Here's the list of books:")
        for i in self.bookList.keys():
            print(i)
    def checkAvailability(self, book):
        if book in self.bookList.keys():
            return self.bookList[book] == ""
        else:
            return False
    def borrow(self, user, book):
        if self.checkAvailability(book):
            self.bookList[book] = user
            return True
        else:
            return False
            #print("Your due is 2 weeks from now dear %s." % user)
    def returnBook(self, user, book):
        if self.bookList[book] in self.bookList.keys():
            self.bookList[book] = ""
            return True
            #print("Thanks dear %s. Please come again." % user)
        else:
            #print("No such book available")
            return False
    def printBorrowers(self):
        print("Here's the list of books and their corresponding borrowers:")
        for k in self.bookList.keys():
            if self.bookList[k] != "":
                print("Book %s is borrowed by %s" % (k, self.bookList[k]))
    def addBook(self, book):
        if not self.checkAvailability(book):
            self.bookList[book] = ""
            #print("Book added successfully")
            return True
        else:
            #print("Book already exists!")
            return False
class users:
    def __init__(self):
        self.userList= {}
    def readUsers(self, fileLocation):
        userFile = 0
        try:
            userFile = open(fileLocation)
        except:
            print("Can't open file")
            return False
        for i in userFile:
            j = i.strip("\r\n").strip("\n")
            if not self.checkExistance(j):
                self.userList[j] = []
        userFile.close()
        return True
    def printUsers(self):
        print("Here's the list of users:")
        for i in self.userList.keys():
            print(i)
    def checkExistance(self, user):
        return user in self.userList.keys()
    def borrow(self, user, book):
        if self.checkExistance(user):
            self.userList[user].append(book)
            return True
        else:
            return False
    def returnBook(self, user, book):
        if user in self.userList.keys():
            try:
                self.userList[user].remove(book)
                return True
            except:
                return False
        else:
            #print("No such user available")
            return False
    def printBorrowers(self):
        for k in self.userList.keys():
            if len(self.userList[k]) > 0:
                print("Here's the books borrowed by %s:" % k)
                for j in self.userList[k]:
                    print(j)
    def addUser(self, user):
        if not self.checkExistance(user):
            self.userList[user] = []
            #print("User added successfully.")
            return True
        else:
            #print("User already exists.")
            return False
