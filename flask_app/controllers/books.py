from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.book import Book
from flask_app.models.author import Author

@app.route('/books')
def dojos():
    return render_template("show_book.html", books=Book.get_all())

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
def show(id):
    print(id)
    data ={ 
        "id":id
    }
    return render_template("b_fave.html",book=Book.fave_by_author(data))

@app.route('/add/author', methods=['POST'])
def add_author():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect ("/books/<int:id>/")

