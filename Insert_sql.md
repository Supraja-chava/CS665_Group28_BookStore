INSERT INTO Publisher (publisher_id, publisher_name, publication_phone, publication_email, publication_web, publication_address)
VALUES
("P1", "Publisher 1", "123-456-7890", "publisher1@example.com", "www.publisher1.com", "123 Main St, Cityville"),
("P2", "Publisher 2", "987-654-3210", "publisher2@example.com", "www.publisher2.com", "456 Oak St, Townsville"),
("P3", "Publisher 3", "555-123-4567", "publisher3@example.com", "www.publisher3.com", "789 Pine St, Villagetown"),
("P4", "Publisher 4", "111-222-3333", "publisher4@example.com", "www.publisher4.com", "101 Cedar St, Hamletville"),
("P5", "Publisher 5", "444-555-6666", "publisher5@example.com", "www.publisher5.com", "202 Birch St, Countryside");

INSERT INTO Books (book_title, book_author, book_price, published_year, publisher_id)
VALUES
("Book 1", "Author 1", 29.99, 2020, "P1"),
("Book 2", "Author 2", 24.99, 2019, "P2"),
("Book 3", "Author 3", 19.99, 2021, "P3"),
("Book 4", "Author 4", 34.99, 2018, "P4"),
("Book 5", "Author 5", 39.99, 2022, "P5");

INSERT INTO Customers (customer_name, customer_email, customer_phone, customer_address)
VALUES
("Customer 1", "customer1@example.com", "111-222-3333", "123 Park Ave, Cityville"),
("Customer 2", "customer2@example.com", "444-555-6666", "456 Grove St, Townsville"),
("Customer 3", "customer3@example.com", "777-888-9999", "789 Forest St, Villagetown"),
("Customer 4", "customer4@example.com", "123-987-6543", "101 River St, Hamletville"),
("Customer 5", "customer5@example.com", "321-555-7890", "202 Lake St, Countryside");

INSERT INTO Publisher_Books_Junction (publisher_id, book_id)
VALUES
('P1', 1),
('P2', 2),
('P3', 3),
('P4', 4),
('P5', 5);

INSERT INTO Orders (customer_id, book_id, quantity, order_date, Total_price)
VALUES
(1, 1, 2, "2023-01-15", 59.98),
(2, 2, 1, "2023-02-20", 24.99),
(3, 3, 3, "2023-03-25", 59.97),
(4, 4, 1, "2023-04-10", 34.99),
(5, 5, 2, "2023-05-05", 79.98);
