CRUD Operations:

1. Publisher Table:

    -- Create (Insert)
    INSERT INTO Publisher (publisher_id, publisher_name, publication_phone, publication_email, publication_web, publication_address)
    VALUES ('P6', 'Publisher 6', '666-777-8888', '<publisher6@example.com>', 'www.publisher6.com', '303 Birch St, Newtown');

    -- Read (Select)
    SELECT * FROM Publisher WHERE publisher_id = 'P6';

    -- Update
    UPDATE Publisher
    SET publication_phone = '999-000-1111', publication_address = '555 Pine St, Newville'
    WHERE publisher_id = 'P6';

    -- Delete
    DELETE FROM Publisher WHERE publisher_id = 'P6';
2. Books Table:

    -- Create (Insert)
    INSERT INTO Books (book_title, book_author, book_price, published_year, publisher_id)
    VALUES ('Book 6', 'Author 6', 49.99, 2022, 'P3');

    -- Read (Select)
    SELECT * FROM Books WHERE book_id = 6;

    -- Update
    UPDATE Books
    SET book_price = 59.99, published_year = 2023
    WHERE book_id = 6;

    -- Delete
    DELETE FROM Books WHERE book_id = 6;

3. Publisher_Books_Junction Table:

    -- Create (Insert)
    INSERT INTO Publisher_Books_Junction (publisher_id, book_id)
    VALUES ('P1', 1);

    -- Read (Select)
    SELECT * FROM Publisher_Books_Junction WHERE publisher_id = 'P1' AND book_id = 1;

    -- Update (Not applicable for junction table)

    -- Delete
    DELETE FROM Publisher_Books_Junction WHERE publisher_id = 'P1' AND book_id = 1;

4. Customers Table:

    -- Create (Insert)
    INSERT INTO Customers (customer_name, customer_email, customer_phone, customer_address)
    VALUES ('Customer 6', '<customer6@example.com>', '666-555-4444', '606 Oak St, Newville');

    -- Read (Select)
    SELECT * FROM Customers WHERE customer_id = 6;

    -- Update
    UPDATE Customers
    SET customer_phone = '999-888-7777', customer_address = '707 Maple St, Newtown'
    WHERE customer_id = 6;

    -- Delete
    DELETE FROM Customers WHERE customer_id = 6;

5. Orders Table:

    -- Create (Insert)
    INSERT INTO Orders (customer_id, book_id, quantity, order_date, Total_price)
    VALUES (1, 2, 1, '2023-07-01', 24.99);

    -- Read (Select)
    SELECT * FROM Orders WHERE order_id = 6;

    -- Update
    UPDATE Orders
    SET quantity = 2, Total_price = 49.98
    WHERE order_id = 6;

    -- Delete
    DELETE FROM Orders WHERE order_id = 6;
