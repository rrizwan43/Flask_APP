from flask import Flask
from flask import render_template
import sqlite3

#creating Database connection

def get_db_connection():
    conn=sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


conn = sqlite3.connect('database.db')
cur = conn.cursor()
# Creating TABLE
#cur.execute("""
#CREATE TABLE CUSTOMERS(
#ID INTEGER PRIMARY KEY AUTOINCREMENT,
#created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#NAME TEXT NOT NULL,
#PHOTO blob
#)
#""")
#print('table created successfully')

#Inserting into Customers Table

#Inserting into Customers Table
#cur.execute("""
#INSERT INTO CUSTOMERS (ID,NAME,PHOTO)
#VALUES(1001,'Rizwan',''),(1003,'KHAN','')
#""")

#selecting data from database
cur.execute("""
select * from customers;
""")
results = cur.fetchall()
for i in results:
    print(i[1])

print('Data Inserted Successfully')
print('connected successully')

app = Flask(__name__)

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM customers').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run()






# Create Tables
#cur.execute("""
#CREATE TABLE IF NOT EXISTS my_table(id int not null,
#name text,
#photo blop)
#""")

with open('1.jpg', 'rb') as f:
    data=f.read()

conn.commit()
cur.close()
conn.close()

