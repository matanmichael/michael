import os
import tools.books as mbook
import tools.customers as mcustomer
import tools.loans as mloan
import tools.unitTest as AD

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

def main(): 
    mbook.Books.createTBooks(mbook.Books)
    mcustomer.Customers.createTcustomers(mcustomer.Customers)
    mloan.Loans.createTLoans(mloan.Loans)
    
    msg ="please enter your choice"
    while(True):
        print(msg)
        print("ac - add a new customer")
        print("ab - add a new book")
        print("lb - loan a book")
        print("reb - return a book")
        print("dab - display all books")
        print("dc - display all customers")
        print("dal - display all loans")
        print("dll - display late loans")
        print("fb - find book by name")
        print("fc - find customer by name")
        print("deb - remove book")
        print("rc - remove customer")
        print("ad - Add Data")
        print("q - to quit app")
        userChoice=input('Please enter your choice ')
        clearConsole()

        if userChoice == "ac":
            mcustomer.Customers.addNewCustomer(mcustomer.Customers)
            msg = "customer added"
        elif userChoice == "ab":
            mbook.Books.addANewBook(mbook.Books)
            msg = "book added"
        elif userChoice == "lb":
            mloan.Loans.loanBook(mloan.Loans)
            msg = "book loan finished"
        elif userChoice == "reb":
            mloan.Loans.returnBook(mloan.Loans)
            msg = "book return done"
        elif userChoice == "dab":
            mbook.Books.displayAllBooks(mbook.Books)
            msg = "books disaply done"
        elif userChoice == "dc":
            mcustomer.Customers.displayAllCustomers(mcustomer.Customers)
            msg = "customers display done"
        elif userChoice == "dal":
            mloan.Loans.displayAllLoans(mloan.Loans)
            msg = "loans display done"
        elif userChoice == "dll":
            mloan.Loans.displayLateLoans(mloan.Loans)
            msg = "display late loans done"
        elif userChoice == "fb":
            mbook.Books.findBookByName(mbook.Books)
            msg = "book search completed"
        elif userChoice == "fc":
            mcustomer.Customers.findCustomerByName(mcustomer.Customers)
            msg = "customer search completed"      
        elif userChoice == "deb":
            mbook.Books.reomveBook(mbook.Books)
            msg = "book removed"            
        elif userChoice == "rc":
            mcustomer.Customers.removeCustomer(mcustomer.Customers)
        elif userChoice == "ad":
            AD.dataAdder() 
            msg = "Data Added" 
        elif userChoice == "q":
            return
            

if __name__ == '__main__':
    main()
   