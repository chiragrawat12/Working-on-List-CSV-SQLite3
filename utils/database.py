books=[]
def prompt_add_book():
    name = input("Enter Name of Book: ").lower()
    author = input("Enter Book's Author: ").lower()
    books.append({'name':name,'author':author,'read':False})
def list_book():
    for book in books:
        print("Name={}\nAuthor={}".format(book['name'].capitalize(),book['author'].title()))


def prompt_read_book():
    name = input("Enter Book name to read: ").lower()
    for book in books:
        if book["name"]==name:
            if book["read"]==False:
                print("Name={}\nAuthor={}".format(book['name'].capitalize(),book['author'].title()))
                book["read"]=True
            else:
                print("You already Read this book")


def prompt_delete_book():
    name=input("Enter Name of the Book: ").lower()
    for book in books:
        if name==book["name"]:
            books.remove(book)

