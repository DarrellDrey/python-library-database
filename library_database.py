import sqlite3

conn = sqlite3.connect('library.db')

cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS books
               (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year_published INTEGER)''')

def add_book(title, author, year_published):
    cur.execute("INSERT INTO books (title, author, year_published) VALUES (?, ?, ?)",
                (title, author, year_published))
    conn.commit()

def get_all_books():
    cur.execute("SELECT * FROM books")
    return cur.fetchall()

def update_book(book_id, title, author, year_published):
    cur.execute("UPDATE books SET title = ?, author = ?, year_published = ? WHERE id = ?",
                (title, author, year_published, book_id))
    conn.commit()

def delete_book(book_id):
    cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
    conn.commit()

add_book('To Kill a Mockingbird', 'Harper Lee', 1960)
add_book('1984', 'George Orwell', 1949)
add_book('Moby Dick', 'Herman Melville', 1851)
add_book('Batman', 'Drey Jacobs', 1990 )

print("All books:")
books = get_all_books()
for book in books:
    print(book)

update_book(1, 'To Kill a Mockingbird', 'Harper Lee', 1961)

print("All books after update:")
books = get_all_books()
for book in books:
    print(book)

delete_book(2)

print("All books after deletion:")
books = get_all_books()
for book in books:
    print(book)

conn.close()
