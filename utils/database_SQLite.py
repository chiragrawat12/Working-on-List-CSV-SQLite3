import sqlite3
def create_book_table():
    with sqlite3.connect("data.db") as connection:
        cursor=connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)")
        connection.commit()

def prompt_add_book():
    name=input("Enter name of book: ").lower()
    author=input("Enter name of author: ")
    try:
        with sqlite3.connect("data.db") as connection:
            cursor=connection.cursor()
            cursor.execute("INSERT INTO books VALUES(\'{}\',\'{}\',{})".format(name,author,0))
            connection.commit()
    except sqlite3.IntegrityError:
        print("This data Already Exist")

def list_book():
    with sqlite3.connect("data.db") as connection:
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM books")
        books=[{"name":row[0],"author":row[1],"read":row[2]} for row in cursor.fetchall()]
        for book in books:
            print("Name:{} , Author:{}".format(book["name"].title(),book["author"].capitalize()))

def prompt_read_book():
    book_name=input("Enter Name of Book: ").lower()
    with sqlite3.connect("data.db") as connection:
        cursor=connection.cursor()
        cursor.execute("SELECT read FROM books WHERE name=\'{}\'".format(book_name))
        book=cursor.fetchone()
        if book[0]==0:
            cursor.execute("UPDATE books SET read=1 WHERE name=\'{}\'".format(book_name))
            connection.commit()
        else:
            print("Already read this")


def prompt_delete_book():
    name=input("Enter Name of the Book: ").lower()
    with sqlite3.connect("data.db") as connection:
        cursor= connection.cursor()
        cursor.execute("DELETE FROM books WHERE name=\'{}\'".format(name))
        connection.commit()

