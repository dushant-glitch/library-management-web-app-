import mysql.connector
from tkinter import *
from tkinter import ttk, messagebox

# ----------------- DATABASE CONNECTION -------------------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",   # <--- Change This
    database="library",
    port=3306
)
cursor = db.cursor()

# ----------------- FUNCTIONS -------------------
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()
    copies = copies_entry.get()

    if title == "" or author == "" or year == "" or copies == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return
    
    cursor.execute("INSERT INTO books(title, author, year, copies) VALUES(%s, %s, %s, %s)",
                   (title, author, year, copies))
    db.commit()
    view_books()
    clear_inputs()
    messagebox.showinfo("Success", "Book Added Successfully")


def delete_book():
    selected = book_table.focus()
    values = book_table.item(selected, 'values')
    if not values:
        messagebox.showwarning("Warning", "Select a book to delete")
        return

    cursor.execute("DELETE FROM books WHERE id=%s", (values[0],))
    db.commit()
    view_books()
    clear_inputs()
    messagebox.showinfo("Success", "Book Deleted Successfully")


def update_book():
    selected = book_table.focus()
    values = book_table.item(selected, 'values')
    if not values:
        messagebox.showwarning("Warning", "Select a book to update")
        return

    id = values[0]
    cursor.execute("UPDATE books SET title=%s, author=%s, year=%s, copies=%s WHERE id=%s",
                   (title_entry.get(), author_entry.get(), year_entry.get(), copies_entry.get(), id))
    db.commit()
    view_books()
    clear_inputs()
    messagebox.showinfo("Success", "Book Updated Successfully")


def view_books():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    book_table.delete(*book_table.get_children())
    for row in rows:
        book_table.insert("", END, values=row)


def fill_inputs(event):
    selected = book_table.focus()
    values = book_table.item(selected, 'values')
    if values:
        title_entry.delete(0, END)
        author_entry.delete(0, END)
        year_entry.delete(0, END)
        copies_entry.delete(0, END)

        title_entry.insert(0, values[1])
        author_entry.insert(0, values[2])
        year_entry.insert(0, values[3])
        copies_entry.insert(0, values[4])


def clear_inputs():
    title_entry.delete(0, END)
    author_entry.delete(0, END)
    year_entry.delete(0, END)
    copies_entry.delete(0, END)


# ----------------- UI DESIGN -------------------
root = Tk()
root.title("📚 Library Management System")
root.geometry("800x500")
root.configure(bg="#f5f5f5")

title_label = Label(root, text="Library Management System", font=("Arial", 20, "bold"), bg="#f5f5f5")
title_label.pack(pady=10)

form_frame = Frame(root, bg="#f5f5f5")
form_frame.pack(fill=X, padx=20)

# Labels + Inputs
Label(form_frame, text="Title:", bg="#f5f5f5", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky=W)
title_entry = Entry(form_frame, width=30)
title_entry.grid(row=0, column=1, padx=10, pady=5)

Label(form_frame, text="Author:", bg="#f5f5f5", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky=W)
author_entry = Entry(form_frame, width=30)
author_entry.grid(row=1, column=1, padx=10, pady=5)

Label(form_frame, text="Year:", bg="#f5f5f5", font=("Arial", 12)).grid(row=0, column=2, padx=10, pady=5, sticky=W)
year_entry = Entry(form_frame, width=20)
year_entry.grid(row=0, column=3, padx=10, pady=5)

Label(form_frame, text="Copies:", bg="#f5f5f5", font=("Arial", 12)).grid(row=1, column=2, padx=10, pady=5, sticky=W)
copies_entry = Entry(form_frame, width=20)
copies_entry.grid(row=1, column=3, padx=10, pady=5)

# Buttons
button_frame = Frame(root, bg="#f5f5f5")
button_frame.pack(pady=10)

ttk.Button(button_frame, text="Add Book", width=20, command=add_book).grid(row=0, column=0, padx=10)
ttk.Button(button_frame, text="Update Book", width=20, command=update_book).grid(row=0, column=1, padx=10)
ttk.Button(button_frame, text="Delete Book", width=20, command=delete_book).grid(row=0, column=2, padx=10)

# Table
table_frame = Frame(root)
table_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

book_table = ttk.Treeview(table_frame, columns=("ID", "Title", "Author", "Year", "Copies"), show="headings")
book_table.pack(fill=BOTH, expand=True)

for col in ("ID", "Title", "Author", "Year", "Copies"):
    book_table.heading(col, text=col)
    book_table.column(col, anchor=CENTER)

book_table.bind("<ButtonRelease-1>", fill_inputs)

view_books()
root.mainloop()
