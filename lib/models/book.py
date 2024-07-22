#indvidual books each book has a title author and genre_id for the genre 
from models.__init__ import CURSOR, CONN
from models.bookshelf import Bookshelf

class Book:
    
    all = {}

    def __init__(self,title,author, genre_id, id = None):
        self.id = id
        self.title = title
        self.author = author
        self.genre_id = genre_id
    
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        if isinstance(title, str):
            self._title = title
        else:
            raise ValueError(
                "title must be an string"
            )

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, str):
            self._author = author
        else:
            raise ValueError(
                "Author must be an string"
            )
        
    @property
    def genre_id(self):
        return self._genre_id
    
    @genre_id.setter
    def genre_id(self, genre_id):
        if type(genre_id) is int and Bookshelf.find_by_id(genre_id):
            self._genre_id = genre_id
        else:
            raise ValueError(
                "genre_id must be an integer"
            )
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books(
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES bookshelf(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """ 
            DROP TABLE IF EXISTS books;
        """
        CURSOR.execute(sql)
        CONN.commit()

    
    def save(self):
        sql = """
            INSERT INTO books (title,author,genre_id)
            VALUES (?,?,?)
        """

        CURSOR.execute(sql, (self.title , self.author, self.genre_id))
        CONN.commit()
    
        self.id  = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        sql = """
            UPDATE books
            SET title = ?, author = ?, genre_id = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.title, self.author, self.genre_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM books
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None
    
    @classmethod
    def create(cls,title,author,genre_id):
        book = cls(title,author,genre_id)
        book.save()
        return book
    
    @classmethod
    def instance_from_db(cls, row):
        book = cls.all.get(row[0])  
        if book:
            book.title = row[1]
            book.author = row[2]
            book.genre_id = row[3]
        else:
            book = cls(row[1],row[2],row[3])
            book.id = row[0]
            cls.all[book.id] = book 
        return book
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM books
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):

        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        
        sql = """
            SELECT *
            FROM books
            WHERE author is ?
        """

        row = CURSOR.execute(sql, (author,)).fetchone()
        return cls.instance_from_db(row) if row else None

























