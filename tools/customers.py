import sqlite3 

conn = sqlite3.connect('library.db')

cur = conn.cursor()
class Customers:
    
    def createTcustomers(self):
      
        try:
            cur.execute("""CREATE TABLE Customers(
                ID INTEGER PRIMARY KEY ,
                Name TEXT NOT NULL,
                City TEXT NOT NULL,
                Age INTEGER NOT NULL
                )""")  
            conn.commit()
            
        except:
            print("Customers Table has already been created")
        else:
            print("Customers Table created")     
            
    def __init__(self,customerID,customerName,customerCity,customerAge):
        self.customerID = customerID
        self.customerName = customerName
        self.customerCity = customerCity
        self.customerAge = customerAge
    
    def addNewCustomer(self):
        self.customerName = input("Please enter customer name ")
        self.customerCity = input("Please enter customer city ")
        self.customerAge = input("Please enter customer age ")
        cur.execute("INSERT INTO Customers(Name,City,Age) VALUES (?,?,?)",
        (self.customerName,self.customerCity,self.customerAge))
        conn.commit()
        
    def displayAllCustomers(self):
        for row in cur.execute("SELECT * FROM Customers ORDER BY ID"):
            print("customer_ID:",row[0]," customer_Name:",row[1]," customer_City:",row[2]," customer_Age:",row[3])      
    
    def findCustomerByName(self):
        self.customerName = input("Please enter Customer name ")
        for row in cur.execute(f"SELECT * FROM Customers WHERE Name LIKE \"%{self.customerName}%\""):
            print("custmoer_ID:",row[0]," customer_Name:",row[1]," customer_City:",row[2]," customer_Age:",row[3])
        
    def removeCustomer(self):
        Customers.displayAllCustomers(Customers)
        self.customerID = input("Please enter customer ID ")
        for row in cur.execute(f"DELETE FROM Customers WHERE ID= {self.customerID}"):
            print(row)
        conn.commit()
       