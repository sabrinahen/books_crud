from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    db = "book_schema"
    def  __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.authors_favorited = []

    @classmethod
    def getAll(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.db).query_db(query)
        books = []
        for book in results:
            books.append( cls(book) )
        return books

    @classmethod
    def getOne(cls, data):
        query  = "SELECT * FROM books WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s, %(num_of_pages)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def fave_by_author (cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        book = cls(results[0])
        for row in results:
            author_data = {
                "id": row["authors.id"],
                "name": row["name"],
                "created_at": row["authors.created_at"],
                "updated_at": row["authors.updated_at"]
            }
# not sure about this part
            book.authors_favorited.append(author.Author(author_data))
        return book

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass