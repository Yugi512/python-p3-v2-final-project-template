# will have genres amd id
from models.__init__ import CURSOR, CONN

class Bookshelf:
    all = {}

    def __init__(self, genre , id = None):
        self.genre = genre
        self.id = id


    @property
    def genre(self):
        return self._genre
    
    @genre.setter
    def genre(self,genre):
        if isinstance(genre, str):
            self._genre = genre
        else:
            raise ValueError(
                "Value needs to be a string"
                )
    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Bookshelf instances """
        sql = """
            CREATE TABLE IF NOT EXISTS bookshelfs (
            id INTEGER PRIMARY KEY,
            genre TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists the bookshelf instances """
        sql = """
            DROP TABLE IF EXISTS bookshelfs;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        """ insert a new tow with the genre of the current bookshelf instance
        Updates the object id attribute using thr primary key value of the new row
        Saves rhe object into the local dictionary using the table's rows PK as dictionary key """
        sql = """
            INSERT INTO bookshelfs (genre)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.genre,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
    
    def update(self):
        sql ="""
            UPDATE bookshelfs
            SET genre = ?,
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.genre,self.id))
        CONN.commit()


    @classmethod
    def create(cls,genre):
       """inititalize a new bookshelf instance and save the object to the database"""
       bookshelf = cls(genre)
       bookshelf.save()
       return bookshelf

    def delete(self):
        """delete the table row that corresponds to the current instance"""
        sql = """
            DELETE FROM bookshelfs
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None
    
    @classmethod
    def instance_from_db(cls,row):

        bookshelf = cls.all.get(row[0])
        if bookshelf:
            bookshelf.genre = row[1]
        else:
            bookshelf = cls(row[1])
            bookshelf.id = row[0]
            cls.all[bookshelf.id] = bookshelf
        return bookshelf

    @classmethod
    def get_all(cls):
        """ return a loist containing a bookshelf object by row """
        sql = """
            SELECT * 
            FROM bookshelfs
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """ find the bookshelf objecty that corresponds to the row with the matching primary key"""
        sql = """
            SELECT *
            FROM bookshelfs
            WHERE id =?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def books(self):
        """ Return a list of the books that are of the genre"""
        from models.book import Book
        sql = """
            SELECT * FROM books
            WHERE genre_id = ?
        """
        CURSOR.execute(sql,(self.id,),)

        rows = CURSOR.fetchall()
        return [
            Book.instance_from_db(row) for row in rows
        ]