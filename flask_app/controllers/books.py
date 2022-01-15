from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/books')
def dojos():
    return render_template("show_book.html", books=Book.getAll())

@app.route('/create/book',methods=['POST'])
def create_book():
    data = {
        "title" : request.form["title"],
        "num_of_pages" : request.form["num_of_pages"]
    }
    print(data)
    Book.save(data)
    return redirect('/books')

@app.route('/books/<int:id>')
def show_books(id):
    print(id)
    data ={ 
        "id":id
    }
    return render_template("b_fave.html",book=Book.fave_by_author(data), authors=Author.getAll())

@app.route('/add/author', methods=['POST'])
def add_author():
    book_id=request.form["book_id"]
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect (f"/books/{book_id}")

