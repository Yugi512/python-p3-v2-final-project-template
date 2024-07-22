#!/usr/bin/env python3
# lib/debug.py

from models.bookshelf import Bookshelf
from models.book import Book
from models.__init__ import CONN, CURSOR
import ipdb

def reset_database():
    Book.drop_table()
    Bookshelf.drop_table()
    Bookshelf.create_table()
    Book.create_table()

    non_fiction = Bookshelf.create("non-fiction")
    fiction = Bookshelf.create("fiction")

    Book.create("Breakfast of champions","Kurt Vonnegut", fiction.id)
    Book.create("Harrison Bergeron","Kurt Vonnegut", fiction.id)
    Book.create("Fahrenheit 451","Ray Bradburry", fiction.id)
    Book.create("Into the wild", "Jon Krakauer", non_fiction.id)
    Book.create("Down and out in Paris and London","GEorge Orwell", non_fiction.id)

reset_database()
ipdb.set_trace()
