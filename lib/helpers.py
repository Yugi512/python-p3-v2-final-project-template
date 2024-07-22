# lib/helpers.py
from models.bookshelf import Bookshelf
from models.book import Book
# we need to create an object, delete an object, display all objects, view related objects, find an object by attribute

def exit_program():
    print("Goodbye!")
    exit()

# any code with an id refactor it to not take an id, or foreign keys
#bookshelf methods
def all_genres():
    genres = Bookshelf.get_all()
    space()
    for i,genre in enumerate(genres, start=1):
        print(f"{i}) {genre.genre}")
    space()
    return genres

def ab_genres(choice):
    num = int(choice)
    genre = Bookshelf.get_all()
    if num <= len(genre):
        try:
            genres_book = genre[num - 1]
            space()
            for i,book in enumerate(genres_book.books(),start=1):
                print(f"{i}) {book.title} by ")
            space()
        except Exception as exc:
            space()
            print("An Error has occured: ", exc)
            space()
        return True

def create_genre():
    genre = input("Enter new genre: ")
    if genre.isalpha():
        try:
            bookshelf = Bookshelf.create(genre)
            space()
            print(f"{bookshelf.genre} section has been created")
            space()
        except Exception as exc:
            print("Error adding category: ", exc)
    elif genre.isalpha():
        space()
        print("Error input must be valid string input")
        space()
    else:
        space()
        print("Error input must be valid string input")
        space()
    
def delete_genre():
    # to delete the whole genre we should take the genre input convert it to an int and then do the var = genres[num -1] and then do that var.books() and then look through it and delete that book
    genres = all_genres()
    gen = input("Enter a number associated with a Genre from the list above: ")
    if gen.isnumeric():    
        num = int(gen)
        if num <= len(genres):
            genre = genres[num - 1]
            for i,book in enumerate(genre.books(),start=1):
                if book.genre_id == genre.id:
                    book.delete()
                    genre.delete()
                    print(f"Genre associated with the number {num} has been deleted")
                    space()
    elif gen.isalpha():    
        space()
        print("Error input must be a integer")
        space()
    else:
        space()
        print("Error input must be a integer")
        space()


# #book methods
#need to fix inputs so that they can print an error message for when a empty string is inputted

def all_books():
    books = Book.get_all()
    space()
    for i,book in enumerate(books,start=1):
        print(f"{i}) {book.title}" )
    space()
    return books

def book_by_num(genre_choice=None,choice=None):
    all_genres = Bookshelf.get_all()
    genre_num = int(genre_choice)
    num = int(choice)
    genres =  all_genres[genre_num -1].books()
    if num <= len(genres):
        try:
            book = genres[num -1]
            genre = all_genres[genre_num -1].id
            if book.genre_id == genre:
                space()
                print(f"{book.title} by {book.author}")
                space()
                return True
            else:
                return False
        except Exception as exc:
            space()
            print("An Error has occured: ", exc)
            space()
            

def create_book():
    genres = all_genres()
    title = input("Enter Title of book: ")
    if isinstance(title,str) and title != "" and title.isalpha():
        author = input("Enter Author of book: ")
        if isinstance(author,str) and author != "" and author.isalpha():
            genre = input("Enter a number associated with a Genre from the list above: ")
            if genre.isnumeric(): 
                converted = int(genre)   
                try:
                    num_in_list = genres[converted - 1]
                    book = Book.create(title,author,num_in_list.id)
                    space()
                    print(f"{book.title} has been added to the bookshelf")
                    space()
                except Exception as exc:
                    space()
                    print("Error creating book: ", exc)
                    space()
            else:
                space()
                print("Error input must be a integer")
                space()
        else:
            space()
            print("Error input must be valid string input")
            space()
    else:
        space()
        print("Error input must be a valid string input")
        space()

def delete_book():
    books = all_books()
    inp_num = input("Enter a number associated to a Book from the list above: ")
    if inp_num.isnumeric():
        num = int(inp_num)
        if num <= len(books):
            book = books[num - 1]
            book.delete()
            space()
            print(f"Book associated with number {num} has been removed")
            space()
        else:
            space()
            print(f"no such book found with associated to the number {num}")
            space()
    else:
        space()
        print("Error input must be a integer")
        space()
    
def update_book_info(g_choice,b_choice):
    all_genres()
    all_genre = Bookshelf.get_all()
    genre_num = int(g_choice)
    num = int(b_choice)
    genres =  all_genre[genre_num -1]
    book = genres.books()[num -1]
    space()
    try:
        title = input("Enter Title of book: ")
        if title.isalpha():
            book.title = title
        elif title.isnumeric():
            book.title = title
            space()
            print("Error input must be valid string input")
            space()
        else:
            book.title = book.title
        author = input("Enter Author of book: ")
        if author.isalpha():
            book.author = author
        elif author.isnumeric():
            book.author = author
            space()
            print("Error input must be valid string input")
            space()
        else:
            book.author = book.author
        genre = (input("Enter a number associated with a Genre from the list above: "))
        if genre.isnumeric():
            converted_num = int(genre)
            if 0 <= converted_num <= len(Bookshelf.get_all()):
                book.genre_id = all_genre[converted_num -1].id
                book.update()
                space()
                print("Success! ")
                print(
                    f"{book.title} by {book.author} "
                )
                print(f"Genre: {genres.genre}")
                space()
            else:
                space()
                print("Error input must be a value from the list above")
                space()
        elif genre.isalpha():
            space()
            print("Error input must be a value from the list above")
            space()
        else:
            book.genre_id = book.genre_id
            book.update()
            space()
            print("Success! ")
            print(
                f"{book.title} by {book.author} "
            )
            print(f"Genre: {genres.genre}")
            space()
        
    except Exception as exc:
        space()
        print("Error in updating book: ", exc)
        space()




def space():
    print(" ")