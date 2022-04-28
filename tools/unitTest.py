import sqlite3 

conn = sqlite3.connect('library.db')

cur = conn.cursor()
# run unit test throw main write "ad" and it will had data.
def dataAdder():

  cur.execute("INSERT INTO Customers(Name,City,Age) VALUES ('matan','karmiel','33')")
  cur.execute("INSERT INTO Customers(Name,City,Age) VALUES ('moran','jerusalem','45')")
  cur.execute("INSERT INTO Customers(Name,City,Age) VALUES ('shahar','ashdod','55')")
  cur.execute("INSERT INTO Customers(Name,City,Age) VALUES ('hen','haifa','32')")
  cur.execute("INSERT INTO Customers(Name,City,Age) VALUES ('shalom','tel aviv','21')")
  cur.execute("INSERT INTO Customers(Name,City,Age) VALUES ('Thomas','petah tikva','1')")

  cur.execute("INSERT INTO Books(Name,Author,Year_Published,Book_Type) VALUES ('moby dick','herman','1851','1')")
  cur.execute("INSERT INTO Books(Name,Author,Year_Published,Book_Type) VALUES ('star wars','lucas','1951','2')")
  cur.execute("INSERT INTO Books(Name,Author,Year_Published,Book_Type) VALUES ('titanic','shuster','1988','3')")
  cur.execute("INSERT INTO Books(Name,Author,Year_Published,Book_Type) VALUES ('avatar','ronaldo','1700','1')")
  cur.execute("INSERT INTO Books(Name,Author,Year_Published,Book_Type) VALUES ('the giant','javier','1990','2')")
  cur.execute("INSERT INTO Books(Name,Author,Year_Published,Book_Type) VALUES ('the friendly tree','jose','1902','3')")

  try:
    cur.execute("INSERT INTO Loans(Customer_ID,Book_ID ,Loan_Date,Return_Date) VALUES ('1','2','2022-02-01','2022-02-11')")
    cur.execute("INSERT INTO Loans(Customer_ID,Book_ID ,Loan_Date,Return_Date) VALUES ('2','1','2022-03-01','2022-03-06')")
    cur.execute("INSERT INTO Loans(Customer_ID,Book_ID ,Loan_Date,Return_Date) VALUES ('3','3','2022-03-18','2022-03-20')")
  except:
    ("books already on loan")
  
  conn.commit()

  