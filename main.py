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


# Display all books
@app.route('/books')
def display_books():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Books')
    books = cursor.fetchall()
    return render_template('books.html', books=books)

# Add a new book
@app.route('/books/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        conn = get_db()
        cursor = conn.cursor()
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        published_year = request.form['published_year']
        publisher_id = request.form['publisher_id']  # Get the selected publisher_id from the form

        # Generate a 6-digit unique book ID
        book_id = str(uuid.uuid4().int)[:6]

        cursor.execute('INSERT INTO Books (book_id, book_title, book_author, book_price, published_year, publisher_id) VALUES (?, ?, ?, ?, ?, ?)',
                       (book_id, title, author, price, published_year, publisher_id))
        conn.commit()
        return redirect('/books')

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('SELECT publisher_id, publisher_name FROM Publisher')
    publishers = cursor.fetchall()  # Fetch all the publishers to display in the dropdown select field

    return render_template('add_book.html', publishers=publishers)

# Update a book
@app.route('/books/update/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    conn = get_db()
    cursor = conn.cursor()

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        price = request.form['price']
        published_year = request.form['published_year']
        publisher_id = request.form['publisher_id']  # Get the selected publisher_id from the form

        cursor.execute('UPDATE Books SET book_title=?, book_author=?, book_price=?, published_year=?, publisher_id=? WHERE book_id=?',
                       (title, author, price, published_year, publisher_id, book_id))
        conn.commit()
        return redirect('/books')

    cursor.execute('SELECT * FROM Books WHERE book_id=?', (book_id,))
    book = cursor.fetchone()

    cursor.execute('SELECT publisher_id, publisher_name FROM Publisher')
    publishers = cursor.fetchall()  # Fetch all the publishers to display in the dropdown select field

    return render_template('update_book.html', book=book, publishers=publishers)

# Delete a book
@app.route('/books/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Books WHERE book_id=?', (book_id,))
    conn.commit()
    return redirect('/books')

# Search books
@app.route('/books/search', methods=['GET'])
def search_books():
    search_query = request.args.get('query', '').strip()

    if not search_query:
        # If the search query is empty, display all books
        return redirect('/books')

    conn = get_db()
    cursor = conn.cursor()

    # Perform the search query using SQL LIKE clause to filter the results
    cursor.execute('SELECT * FROM Books WHERE book_id LIKE ? OR book_title LIKE ? OR book_author LIKE ?', ('%' + search_query + '%', '%' + search_query + '%', '%' + search_query + '%'))
    books = cursor.fetchall()

    return render_template('books.html', books=books)

# Function to open the modal and load publisher details
@app.route('/publishers/<int:publisher_id>')
def open_publisher_details(publisher_id):
    conn = get_db()
    cursor = conn.cursor()

    # Fetch publisher details
    cursor.execute('SELECT * FROM Publisher WHERE publisher_id=?', (publisher_id,))
    publisher = cursor.fetchone()

    # Render the publisher details template
    return render_template('publisher_details.html', publisher=publisher)




    

# Run the application
if __name__ == '__main__':
    app.run(debug=True)