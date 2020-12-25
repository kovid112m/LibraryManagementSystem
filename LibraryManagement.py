class Library:
    college = "ABC"
    def __init__(self, listOfBooks):
        self.books = listOfBooks
        self.book_index = range(len(listOfBooks))
        self.bookAlreadyIssued = [0] * len(listOfBooks)
        self.issuedTo = {}
    
    

    def issueBook(self, student, book):
        if book in self.books and self.bookAlreadyIssued[self.books.index(book)]==0:
            print("Issued")
            self.issuedTo[book] = student.name
            self.bookAlreadyIssued[self.books.index(book)] = 1
        else:
            if book not in self.books:
                print("Sorry this book is not in the library")
            else:
                print("Sorry the book is already issued\nPlease issue some other book")

    def returnBook(self, student, book):
        if book in self.books and self.bookAlreadyIssued[self.books.index(book)]==1:
            print("Book returned successfully")
            self.bookAlreadyIssued[self.books.index(book)]=0
        else:
            if book not in self.books:
                print("Sorry the book you are trying to return does not belong to this library")
            else:
                print("Book already returned")



class Student:
    college = "ABC"
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade




if __name__ == "__main__":
    books = ['Astrophysics for People in a Hurry', 'A Brief History of Time', 'The Elegant Universe']
    s1 = Student("Raka",11)
    s2 = Student("Miz",11)
    library = Library(books)
    students = [s1,s2]
    # library.issueBook(s1, 'Astrophysics for people in a hurry')
    # library.returnBook(s1, 'Astrophysics for people in a hurry')
    # library.issueBook(s2, 'Astrophysics for people in a hurry')

    
    while(True):
        action = input("Hello and Welcome to the School Library\nWhat do you want to do? ('Issue' / 'Return' / 'Exit') : ")
        if action == 'Issue':
            name = input("What's your name?")
            studentFound = 0
            for i in range(len(students)):
                if students[i].name == name:
                    bookToIssue = input("Which book do you want to issue?")
                    library.issueBook(students[i],bookToIssue)
                    studentFound = 1
            if studentFound == 0:
                print("Sorry you are not a registered student of this school\nPlease register yourself first")
        elif action == 'Return':
            
            name = input("What's your name?")
            for i in range(len(students)):
                if students[i].name == name:
                    bookToReturn = input("Which book do you want to return?")
                    library.returnBook(students[i],bookToReturn)
        
        elif action == 'Exit':
            print("Thankyou!")
            break
        else:
            print("Invalid Option")
            
            




    