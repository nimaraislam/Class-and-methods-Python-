from library import Library
def main():
    my_library = Library()
    while True:
        print("*****************Welcome to the library*******************")
        print("1. Press A to add a book title.")
        print("2. Press B to borrow a book.")
        print("3. Press R to return a book.")
        print("4. Press L to see list of available book.")
        print("5. Press Q to exit.")
        input_library=input("> ").upper().strip()
        if input_library == "A":
            try:
                title = input("Enter book title: ").lower().strip()
                message_add = my_library.add_book(title)
                print(message_add)
            except ValueError:
                print("Invalid title.")
        elif input_library == "B":
            print(my_library.show_available_book())
            try:
                title = input("Enter book title: ").lower().strip()
                message_borrow = my_library.borrow_a_book(title)
                print(message_borrow)
            except ValueError:
                print("Invalid title.")
        elif input_library == "R":
            print(my_library.show_borrowed_book())
            try:
                title = input("Enter book title: ").lower().strip()
                message_return = my_library.return_book(title)
                print(message_return)
            except ValueError:
                print("Invalid title.")
        elif input_library == "L":
           print(my_library.show_available_book()) 
        elif input_library == "Q":
            break
        else:
            print("Invalid input.")
if __name__ == "__main__":
    main()