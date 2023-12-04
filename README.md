# CS665_Group28_BookStore
CS665 Fall 2023 Project 1 Group 28

Group members:

1) Bhargavi Supraja Chava - N443Q864 (https://github.com/Supraja-chava)

YouTube Link: https://www.youtube.com/watch?v=cz4HIMIUMnE

### Bookstore Management System Description:

#### Overview:

The Bookstore Management System is a web application developed using Python Flask as the backend framework and SQLite3 as the database. The system is designed to manage various aspects of a bookstore, including publisher details, book inventory, customer information, and order processing.

#### Features:

1. **Publisher Management:**
   - **Add New Publisher:** Users can add new publishers to the system by providing details such as publisher name, phone number, email, website, and address.
   - **Update Publisher:** Existing publisher information can be updated, allowing for changes in contact details or address.
   - **Delete Publisher:** Publishers that are no longer relevant can be removed from the system.

2. **Book Management:**
   - **Add New Book:** Users can add new books to the bookstore inventory. Each book is associated with a title, author, price, publication year, and a specific publisher.
   - **Update Book:** Details of existing books can be modified, such as updating the price, author, or associating it with a different publisher.
   - **Delete Book:** Books that are no longer part of the inventory can be deleted.

3. **Customer Management:**
   - **Add New Customer:** Customers can be added to the system by providing their name, email, phone number, and address.
   - **Update Customer:** Information about existing customers can be updated, allowing for changes in contact details or address.
   - **Delete Customer:** Customers who are no longer active can be removed from the system.

4. **Order Management:**
   - **Create Order:** Users can create new orders by selecting a customer, adding books to the order along with the quantity, and specifying the order date.
   - **Update Order:** Details of existing orders can be modified, such as adding or removing books or changing the quantity.
   - **Delete Order:** Orders that are no longer relevant or need correction can be deleted from the system.

#### Technologies Used:

- **Backend Framework:** Python Flask
- **Database:** SQLite3
- **Frontend:** HTML, CSS
- **Additional Libraries:** SQLite3 for database interaction in Python, Jinja2 for template rendering in Flask.

#### How It Works:

The application uses Flask to handle HTTP requests and interact with the SQLite3 database. The frontend is designed using HTML and styled with CSS. Users can navigate through different sections of the application to manage publishers, books, customers, and orders. CRUD (Create, Read, Update, Delete) operations are available for each entity, providing a comprehensive system for bookstore management.

#### Usage Scenario:

1. **Adding a New Book:**
   - Navigate to the "Books Management" section.
   - Click on "Add New Book."
   - Enter details such as title, author, price, publication year, and select a publisher.
   - Submit the form to add the new book to the inventory.

2. **Placing an Order:**
   - Navigate to the "Orders Management" section.
   - Click on "Create Order."
   - Select a customer.
   - Add books to the order, specifying the quantity for each.
   - Confirm the order, and the system will update the inventory and customer records accordingly.

3. **Managing Publishers:**
   - Navigate to the "Publisher Management" section.
   - Add, update, or delete publishers as needed.

4. **Viewing Reports:**
   - Users can view reports of existing books, orders, customers, and publishers to analyze the overall status of the bookstore.

This Bookstore Management System provides a user-friendly interface for efficiently managing bookstore operations, ensuring accurate inventory tracking, and facilitating seamless order processing.
YouTube Link:
