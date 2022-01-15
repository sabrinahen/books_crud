from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    db = "book_schema"
    def  __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.favorite_books = []
    
    
    @classmethod
    def getAll(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.db).query_db(query)
        authors = []
        for author in results:
            authors.append( cls(author) )
        return authors

    @classmethod
    def getOne(cls, data):
        query  = "SELECT * FROM authors WHERE id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query,data)
        return cls(result[0])

    @classmethod
    def save(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)


    @classmethod
    def authors_fave(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        author = cls(results[0])
        for row in results:
            book_data = {
                "id": row["books.id"],
                "title": row["title"],
                "num_of_pages": row["num_of_pages"],
                "created_at": row["books.created_at"],
                "updated_at": row["books.updated_at"]
            }
# not sure about this part
            author.favorite_books.append(book.Book(book_data))
        return author

    @classmethod
    def update(cls, data):
        pass

    @classmethod
    def delete(cls, data):
        pass