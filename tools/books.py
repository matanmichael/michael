from fileinput import close
from pydoc import describe
import sqlite3
from tkinter.tix import COLUMN

conn = sqlite3.connect('library.db')

cur = conn.cursor()
class Books:
    def createTBooks(self):
        
        try:
            cur.execute("""CREATE TABLE Books(
                ID INTEGER PRIMARY KEY,
                Name TEXT NOT NULL,
                Author TEXT NOT NULL,
                Year_Published INTEGER NOT NULL,
                Book_Type INTEGER NOT NULL
            )""")
            conn.commit()  
        except:
            print("Book Table has already been created")
        else:
            print("Book Table created")     
                   
    def __init__(self, book_id, bookName, bookAuthor, bookYearPublished, bookType):
        self.book_id = book_id
        self.bookName = bookName
        self.bookAuthor = bookAuthor
        self.bookYearPublished= bookYearPublished
        self.bookType = bookType

    def addANewBook(self):
        self.bookName = input("Please enter book name ")
        self.bookAuthor = input("Please enter book author name ")
        self.bookyearPublished= input("Please enter year of publised ")
        self.bookType = input("Please enter book type ")
        cur.execute("INSERT INTO Books(Name,Author,Year_Published,Book_Type) VALUES (?,?,?,?)",
        (self.bookName, self.bookAuthor, self.bookyearPublished, self.bookType))
        conn.commit()
        
    def displayAllBooks(self):
        for row in cur.execute("SELECT * FROM Books ORDER BY ID"):
            print("book_ID:",row[0]," book_Name:",row[1]," book_Author:",row[2]," Year_Published:",row[3]," Book_Type:",row[4])
               
    def findBookByName(self):
        self.bookName = input("Please enter book name ")
        for row in cur.execute(f"SELECT * FROM Books WHERE Name LIKE \"%{self.bookName}%\""):
            print("book_ID:",row[0]," book_Name:",row[1]," book_Author:",row[2]," Year_Published:",row[3]," Book_Type:",row[4])

    def reomveBook(self):
        Books.displayAllBooks(Books)
        self.book_id = input("Please enter Book ID ")
        for row in cur.execute(f"DELETE FROM Books WHERE ID= {self.book_id}"):
            print(row)
        conn.commit()
        