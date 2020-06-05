from utils.database_SQLite import *
USER_CHOICE="""
Enter:
    -'a' to add a new book
    -'l' to list all books
    -'r' to mark a book as read
    -'d' to delete a book
    -'q' to quit
"""
def menu():
    create_book_table()
    user_input=input(USER_CHOICE)
    while user_input!='q':
        if user_input=='a':
            prompt_add_book()
        elif user_input=='l':
            list_book()
        elif user_input=='r':
            prompt_read_book()
        elif user_input=='d':
            prompt_delete_book()
        else:
            print("Unknown command please enter again.")
        user_input=input(USER_CHOICE)
if __name__=="__main__":
    menu()