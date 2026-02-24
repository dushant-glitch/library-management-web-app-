# Library Management Web Application

A basic Library Management Web Application developed using Python and MySQL.  
The application provides a GUI-based interface for managing library records with real-time database updates.

## Features
- Add, update, delete, and view books
- GUI built using Tkinter
- Real-time data synchronization with MySQL database
- Input validation and user-friendly alerts

## Technologies Used
- Python
- Tkinter
- MySQL
- MySQL Connector

## Database Design
- Single table: `books`
- Stores book title, author, publication year, and available copies

## How to Run the Project
1. Install Python (3.x)
2. Install dependencies:
   pip install -r requirements.txt

3. Import `database.sql` into MySQL
4. Update database credentials in `app.py`
5. Run the application:

python app.py


## Project Purpose
This project was created to understand backend database integration, CRUD operations, and real-time data handling using Python and MySQL.
