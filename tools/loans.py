import sqlite3
from datetime import datetime,timedelta,date
import tools.books as mbook
import tools.customers as mcustomer

conn = sqlite3.connect('library.db')

cur = conn.cursor()

class Loans():

    def createTLoans(self):
    
        try:
            cur.execute("""CREATE TABLE Loans(
            Customer_ID INTEGER NOT NULL,
            Book_ID INTEGER NOT NULL unique,
            Loan_Date INTEGER NOT NULL,
            Return_Date INTEGER NOT NULL
            )""")
            conn.commit() 
            
        except:
            print("Loans Table has already been created")
        else:
            print("Loans Table created")
        
    def __init__(self, custid, book_id, loandate, returndate):
        self.custid = custid
        self.book_id = book_id
        self.loandate = loandate
        self.returndate = returndate
        
    def loanBook(self):
        mcustomer.Customers.displayAllCustomers(mcustomer.Customers)
        self.custid = input("Please enter Customer ID ")
        mbook.Books.displayAllBooks(mbook.Books)
        self.book_id = input("Please enter Book ID ")  
        self.loandate = date.today()
        self.returndate = input("Please enter number of loan days by book type - \nbook type 1 - 10 days loan\nbook type 2 - 5 days loan\nbook type 3 - 2 days loan ")
        self.returndate=date.today()+timedelta(days=int(self.returndate))
        try:
            cur.execute("INSERT INTO Loans(Customer_ID, Book_ID, Loan_Date,Return_Date) VALUES(?,?,?,?)"
                        ,(self.custid,self.book_id,self.loandate,self.returndate)) 
        except:
            print("Book already on loan")
        else:
            print("Done")                
    
            conn.commit()
    
    def returnBook(self):
        Loans.displayAllLoans(Loans)
        self.book_id = input("Please enter Book ID ")
        self.returndate = datetime.now()
        cur.execute(f"DELETE FROM Loans WHERE Book_ID= {self.book_id}")
        conn.commit()
        
    def displayAllLoans(self):  
        for row in cur.execute("SELECT * FROM Loans ORDER BY Loan_Date"):
            print("Customer_ID:",row[0]," Book_ID:",row[1]," Loan_Date:",row[2]," Return_Date:",row[3])
           
    def displayLateLoans(self): 
        global book_id , type , loandate , row 
        for row in cur.execute("""SELECT Book_ID , Book_Type , Loan_Date FROM Loans
                                  INNER JOIN Books ON Books.ID = Loans.Book_ID
                                  INNER JOIN Customers ON Customers.ID = Loans.Book_ID 
                                  ORDER BY Book_ID"""):
            book_id = row[0]
            type = row[1]
            loandate = row[2] 
                                        
            ldate = datetime.now() - datetime.strptime(loandate, '%Y-%m-%d')   
            btype1 = (ldate).days > 10
            btype2 = (ldate).days > 5
            btype3 = (ldate).days > 2
            if type == 1 and btype1:
                print("book id number:", (book_id) ,"is late", ((ldate).days-10), "days")
            elif type == 2 and btype2:
                print("book id number:", (book_id) ,"is late", ((ldate).days-5), "days")
            elif type == 3 and btype3:
                print("book id number:", (book_id) ,"is late", ((ldate).days-2), "days")
            else:
                print("loan is not late")