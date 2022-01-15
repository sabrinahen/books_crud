from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template("show_author.html", authors=Author.getAll())

@app.route('/create/author',methods=['POST'])
def create_author():
    data = {
        "name" : request.form["name"]
    }
    print(data)
    # author_id = Author.save(data)
    Author.save(data)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def show_authors(id):
    print(id)
    data ={ 
        "id":id
    }
    return render_template("a_fave.html",author=Author.authors_fave(data), books=Book.getAll())

@app.route('/add/book', methods=['POST'])
def add_book():
    author_id=request.form["author_id"]
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    print(data)
    Author.add_favorite(data)
    return redirect (f"/authors/{author_id}")
