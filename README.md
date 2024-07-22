# Phase 3 CLI+ORM Project

## Introduction

The database has two models a bookshelfs and the books, it is a one to many relationship as there is only one bookshelf and many books associated to the bookshelf.

The base options are E and A, A to see all the genres in the bookshelf and E to exit the program. 
Option A will display all the genres in the database and then:
    - Enter the number associated with the genre to see books in that section
    - A to see all books
    - B to go back to previous menu
    - C to add a new genre to the shelf
    - D to delete a genre, enter number associated with the genre
    - E to exit program

The first two options: entering a number and the choice A both call upon the books loop in which you will be presented with these options to pick from
    - Enter a number associated with book to see the details of that book
    - B to go back to previous menu
    - C to create a new book
    - D to delete a book
    - M to go back main menu
    - E to exit program

The first option of picking anumber will show the details of the book and the give you the newer option of updating the book
    - U to update book
    - B to go back to previous menu
    - E to exit program

and its pretty self explanitory, to run the program you will need to fork and clone this repository.


To have the data to retrieve and manipulate you will have to fist call python lib/seed.py in the console
Then to run the program to see the data and manipulate the database you will need to run python lib/cli.py
