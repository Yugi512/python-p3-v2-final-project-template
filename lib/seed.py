#!/usr/bin/python3

from models.__init__ import CONN, CURSOR
from models.book import Book
from models.bookshelf import Bookshelf

def seed_database():
    Book.drop_table()
    Bookshelf.drop_table()
    Bookshelf.create_table()
    Book.create_table()

    non_fiction = Bookshelf.create("non-fiction")
    fiction = Bookshelf.create("fiction")
    # sci_fiction = Bookshelf.create("science-fiction")

    Book.create("Breakfast of champions","Kurt Vonnegut", fiction.id)
    Book.create("Harrison Bergeron","Kurt Vonnegut", fiction.id)
    Book.create("Fahrenheit 451","Ray Bradburry", fiction.id)
    Book.create("Into the wild", "Jon Krakauer", non_fiction.id)
    Book.create("Down and out in Paris and London","George Orwell", non_fiction.id)
    # Book.create("book","de", sci_fiction.id)
    # Book.create("book","del", sci_fiction.id)

seed_database()
print("seeded the database")