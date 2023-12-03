CREATE TABLE IF NOT EXISTS Publisher (
    publisher_id TEXT PRIMARY KEY,
    publisher_name TEXT,
    publication_phone TEXT,
    publication_email TEXT,
    publication_web TEXT,
    publication_address TEXT
);

CREATE TABLE IF NOT EXISTS Books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_title TEXT,
    book_author TEXT,
    book_price REAL,
    published_year INTEGER,
    publisher_id TEXT,
    FOREIGN KEY (publisher_id) REFERENCES Publisher (publisher_id)
);

CREATE TABLE IF NOT EXISTS Publisher_Books_Junction (
    publisher_id TEXT,
    book_id INTEGER,
    FOREIGN KEY (publisher_id) REFERENCES Publisher (publisher_id),
    FOREIGN KEY (book_id) REFERENCES Books (book_id),
    PRIMARY KEY (publisher_id, book_id)
);

CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    customer_email TEXT,
    customer_phone TEXT,
    customer_address TEXT
);

CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    book_id INTEGER,
    quantity INTEGER,
    order_date TEXT,
    Total_price INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
    FOREIGN KEY (book_id) REFERENCES Books (book_id)
);

1. Publisher Table:
    Attributes:
       - publisher_id: Primary key uniquely identifying each publisher.
       - publisher_name: Stores the name of the publisher.
       - publication_phone: Represents the phone number of the publisher.
       - publication_email: Stores the email address of the publisher.
       - publication_web: Represents the website of the publisher.
       - publication_address: Holds the address of the publisher.
    Normalization (3NF):
        All attributes are atomic, meaning they cannot be further divided. No transitive dependencies. Each non-prime attribute is fully functionally dependent on the primary key (publisher_id).
2. Books Table:
   Attributes:
       - book_id: Primary key uniquely identifying each book.
       - book_title: Stores the title of the book.
       - book_author: Represents the author of the book.
       - book_price: Stores the price of the book.
       - published_year: Represents the year the book was published.
       - publisher_id: Foreign key referencing the Publisher table.
    Normalization (3NF):
        All attributes are atomic. The foreign key (publisher_id) establishes a relationship with the Publisher table, eliminating the possibility of data redundancy.
3. Publisher_Books_Junction Table:
   Attributes:
       - publisher_id: Foreign key referencing the Publisher table.
       - book_id: Foreign key referencing the Books table.
       - Normalization (3NF):
    The table represents a junction (linking) table for a many-to-many relationship between Publisher and Books. The composite primary key (publisher_id, book_id) ensures uniqueness. Foreign keys establish relationships with their respective tables, avoiding data duplication.
4. Customers Table:
    Attributes:
       - customer_id: Primary key uniquely identifying each customer.
       - customer_name: Stores the name of the customer.
       - customer_email: Represents the email address of the customer.
       - customer_phone: Stores the phone number of the customer.
       - customer_address: Holds the address of the customer.
    Normalization (3NF):
        All attributes are atomic. No transitive dependencies. Each non-prime attribute is fully functionally dependent on the primary key (customer_id).
5. Orders Table:
   Attributes:
       - order_id: Primary key uniquely identifying each order.
       - customer_id: Foreign key referencing the Customers table.
       - book_id: Foreign key referencing the Books table.
       - quantity: Represents the quantity of books in the order.
       - order_date: Stores the date of the order.
       - Total_price: Represents the total price of the order.
    Normalization (3NF):
        All attributes are atomic. Foreign keys establish relationships with their respective tables, avoiding data duplication. No transitive dependencies. Each non-prime attribute is fully functionally dependent on the primary key (order_id).

    In summary, all tables are designed in the Third Normal Form (3NF), ensuring minimal redundancy, atomic attributes, and proper relationships between tables. The structure allows for efficient data retrieval and maintenance.
