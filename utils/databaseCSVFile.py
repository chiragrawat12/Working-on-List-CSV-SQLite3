books_file="database.txt"
def prompt_add_book():
    name = input("Enter Name of Book: ").lower()
    author = input("Enter Book's Author: ").lower()
    with open(books_file,"a") as file:
        file.write("{0},{1},False\n".format(name,author))

def list_book():
    with open(books_file,"r") as file:
        for books in file.readlines():
            books=books.strip().split(",")
            print("Name: {} Author: {}".format(books[0],books[1]))

def prompt_read_book():
    name = input("Enter Book name to read: ").lower()
    with open(books_file,"r") as file:
        B=[]
        for books in file.readlines():
            books=books.strip().split()
            print(B)
            if books[0]==name:
                if books[2]=="False":
                    print("Name={}\nAuthor={}".format(books[0].capitalize(),books[1].title()))
                    B.append(books)
                    with open(books_file,"w"):
                        file.seek()
                        file.write("True")
            else:
                print("You already Read this book")


def prompt_delete_book():
    name=input("Enter Name of the Book: ").lower()
    B=[]
    with open(books_file, "r") as file:
        book=[books.strip().split(",") for books in file.readlines()]
        for line in book:
            if line[0] != name:
                B.append(line)
    with open(books_file, "w") as file:
        for Bk in B:
            file.write(",".join(Bk)+"\n")


