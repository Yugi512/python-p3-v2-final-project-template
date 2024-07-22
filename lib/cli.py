from helpers import (
    exit_program,
    all_genres,
    ab_genres,
    all_books,
    create_genre,
    delete_genre,
    book_by_num,
    create_book,
    delete_book,
    update_book_info,
    space
)

# nested if statements and different 
def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "E":
            exit_program()
        elif choice == "A":
            all_genres()
            bookshelf_loop()
        else:
            print("Invalid choice")


def bookshelf_loop():
    while True:
        bookshelf_menu()
        choice = input("> ")
        if choice.isnumeric():
            if ab_genres(choice) == True:
                books_loop(choice)
            else:
                space()
                print("Error: Invalid Choice")
                space()
        elif choice == "A":
            all_books()
            path_a_loop()
        elif choice == "C":
            create_genre()
        elif choice == "D":
            delete_genre()
        elif choice == "U":
            pass
        elif choice == "E":
            exit_program()
        elif choice == "B":
            main() 
        else:
            space()
            print("Invalid choice")
            space()


def books_loop(choice=None):
    while True:
        books_menu()
        bl_choice = input("> ")
        if bl_choice.isnumeric():
            if book_by_num(choice,bl_choice) == True:
                update_book_loop(choice,bl_choice)
            else:
                space()
                print("Invalid choice")
                space()
        elif bl_choice == "B":
            bookshelf_loop()
        elif bl_choice == "C":
            create_book()
        elif bl_choice == "D":
            delete_book()
        elif bl_choice == "M":
            main()
        elif bl_choice == "E":
            exit_program()
        else:
            space()
            print("Invalid choice")
            space()
        
def path_a_loop(choice=None):
    while True:
        path_a_menu()
        bl_choice = input("> ")
        if bl_choice == "B":
            bookshelf_loop()
        elif bl_choice == "C":
            create_book()
        elif bl_choice == "D":
            delete_book()
        elif bl_choice == "M":
            main()
        elif bl_choice == "E":
            exit_program()
        else:
            space()
            print("Invalid choice")
            space()

def path_a_menu():
    print("B to go back to previous menu")
    print("C to create a new book")
    print("D to delete a book")
    print("M to go back main menu")
    print("E to exit program")

def books_menu():
    print("Enter a number associated with book to see the details of that book")
    print("B to go back to previous menu")
    print("C to create a new book")
    print("D to delete a book")
    print("M to go back main menu")
    print("E to exit program")

def bookshelf_menu():
    print("Enter the number associated with the genre to see books in that section")
    print('A to see all books')
    print("B to go back to previous menu")
    print("C to add a new genre to the shelf")
    print("D to delete a genre, enter number associated with the genre")
    print("E to exit program")

def update_book_loop(g_choice,bl_choice):
    while True:
        update_book_menu()
        u_choice = input(">")
        if u_choice == "U":
            update_book_info(g_choice,bl_choice)
            books_loop()
        elif u_choice == "E":
            exit_program()
        elif u_choice == "B":
            books_loop()
        else:
            print("Invalid choice")
        

def update_book_menu():
    print("U to update book")
    print("B to go back to previous menu")
    print("E to exit program")


def menu():
    print("Please select an option:")
    print("E to exit the program")
    print("A to see all genres in the bookshelf")
    
    

if __name__ == "__main__":
    main()
