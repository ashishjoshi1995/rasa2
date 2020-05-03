import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def create_table():
	c.execute('CREATE TABLE IF NOT EXISTS CUSTOMERS(NAME TEXT, PASSWORD TEXT, PHONENUM TEXT, ADDRESS TEXT, EMAIL TEXT, CUTOMERTYPE TEXT, CONTRACTNUM TEXT)')
	c.execute('CREATE TABLE IF NOT EXISTS BILLS(NAME TEXT, PHONENUM TEXT, BILLID TEXT, METERREADING TEXT, BILLAMOUNT TEXT, BILL_STATUS INT, PAYMENT_LAST_DATE DATE CONTRACTNUM TEXT)')
	c.execute('CREATE TABLE IF NOT EXISTS SERVICE_REQUESTS(NAME TEXT, PHONENUM TEXT, ADDRESS TEXT, REQUEST_TYPE TEXT, STATUS TEXT, SERVICE_ID TEXT CONTRACTNUM TEXT)')
	c.execute('CREATE TABLE IF NOT EXISTS TOPUPS(NAME TEXT, PHONENUM TEXT, TOPUPID TEXT, CREDIT_VALUE TEXT, RECHARGE_DATE DATE CONTRACTNUM TEXT)')

def data_entry():
	c.execute("INSERT INTO CUSTOMERS VALUES('Ashish Joshi', 'pwd', '9756475739', 'Indore', 'ashish.f.joshi@accenture.com', 'PREPAIDBAD', '97564')")
	c.execute("INSERT INTO CUSTOMERS VALUES('Sarthak', 'pwd', '9899808458', 'Pune', 'sarthak.bhargava@accenture.com', 'PREPAIDGOOD', '98998')")
	c.execute("INSERT INTO CUSTOMERS VALUES('Sweta', 'bhoi', '9620000852', 'Gurugram', 'sweta.bhoi@accenture.com', 'POSTPAIDGOOD', '96200')")
	c.execute("INSERT INTO CUSTOMERS VALUES('Ankit', 'mahajan', '9646074138', 'Mumbai', 'ankit@accenture.com', 'POSTPAIDBAD', '96460')")

def query():
	c.execute("SELECT * FROM CUSTOMERS")
	print(c.fetchall())

def create_Bill():
	c.execute("INSERT INTO BILLS VALUES('Ashish', 'Joshi', '9756475739', 'Bill_123', '4598','$500', 'Pending', '12/05/2020')")
	c.execute("INSERT INTO BILLS VALUES('Sarthak', 'Bhargava', '9899808458', 'Bill_124', '7896', '$500', 'Pending', '12/05/2020')")
	c.execute("INSERT INTO BILLS VALUES('Sweta', 'Bhoi', '9620000852', 'Bill_125', '5679', '$500', 'Pending', '12/05/2020')")

create_table()
data_entry()
query()
#create_Bill()
conn.commit()
c.close()
conn.close()