# main.py
from flask import Flask, render_template, request, redirect, g
import sqlite3
import uuid
from flask import render_template

app = Flask(__name__)

# Database connection helper function
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('Group28_Bookstore.db')
    return db

# Create the database tables
with app.app_context():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Publisher (
                        publisher_id TEXT PRIMARY KEY,
                        publisher_name TEXT,
                        publication_phone TEXT,
                        publication_email TEXT,
                        publication_web TEXT,
                        publication_address TEXT
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
                        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        book_title TEXT,
                        book_author TEXT,
                        book_price REAL,
                        published_year INTEGER,
                        publisher_id INTEGER,
                        FOREIGN KEY (publisher_id) REFERENCES Publisher (publisher_id) 
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Publisher_Books_Junction (
                        publisher_id TEXT,
                        book_id INTEGER,
                        FOREIGN KEY (publisher_id) REFERENCES Publisher (publisher_id),
                        FOREIGN KEY (book_id) REFERENCES Books (book_id),
                        PRIMARY KEY (publisher_id, book_id)
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
                        customer_id INTEGER PRIMARY KEY,
                        customer_name TEXT,
                        customer_email TEXT,
                        customer_phone TEXT,
                        customer_adress TEXT
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Orders (
                        order_id INTEGER PRIMARY KEY,
                        customer_id INTEGER,
                        book_id INTEGER,
                        quantity INTEGER,
                        order_date TEXT,
                        Total_price INTEGER,
                        FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
                        FOREIGN KEY (book_id) REFERENCES Books (book_id)
                    )''')
    conn.commit()
    cursor.close()
    conn.close()




    

# Run the application
if __name__ == '__main__':
    app.run(debug=True)