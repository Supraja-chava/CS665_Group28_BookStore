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


# Home page
@app.route('/')
def home():
    return render_template('Home.html')

# Display all publishers
@app.route('/publishers')
def display_publishers():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Publisher')
    publishers = cursor.fetchall()
    return render_template('publishers.html', publishers=publishers)

# Add a new publisher
@app.route('/publishers/add', methods=['GET', 'POST'])
def add_publisher():
    if request.method == 'POST':
        conn = get_db()
        cursor = conn.cursor()
        publisher_name = request.form['publisher_name']
        publication_address = request.form['publication_address']
        publication_phone = request.form['publication_phone']
        publication_email = request.form['publication_email']  # Corrected line
        publication_web = request.form['publication_web']

        # Generate a 6-digit unique publisher ID
        publisher_id = str(uuid.uuid4().int)[:7]

        cursor.execute('INSERT INTO Publisher (publisher_id, publisher_name, publication_address, publication_phone, publication_email, publication_web) VALUES (?, ?, ?, ?, ?, ?)',
                       (publisher_id, publisher_name, publication_address, publication_phone, publication_email, publication_web))
        conn.commit()
        return redirect('/publishers')

    return render_template('add_publisher.html')

# Update a publisher
@app.route('/publishers/update/<string:publisher_id>', methods=['GET', 'POST'])
def update_publisher(publisher_id):
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        publisher_name = request.form['publisher_name']
        publication_address = request.form['publication_address']
        publication_phone = request.form['publication_phone']
        publication_email = request.form['publication_email']  # Added this line
        publication_web = request.form['publication_web']

        cursor.execute('UPDATE Publisher SET publisher_name=?, publication_address=?, publication_phone=?, publication_email=?, publication_web=? WHERE publisher_id=?',
                       (publisher_name, publication_address, publication_phone, publication_email, publication_web, publisher_id))
        conn.commit()
        return redirect('/publishers')

    cursor.execute('SELECT * FROM Publisher WHERE publisher_id=?', (publisher_id,))
    publisher = cursor.fetchone()
    return render_template('update_publisher.html', publisher=publisher, publisher_id=publisher_id)

# Delete a publisher
@app.route('/publishers/delete/<string:publisher_id>', methods=['POST'])
def delete_publisher(publisher_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Publisher WHERE publisher_id=?', (publisher_id,))
    conn.commit()
    return redirect('/publishers')




    

# Run the application
if __name__ == '__main__':
    app.run(debug=True)