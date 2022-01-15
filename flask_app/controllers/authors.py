from flask import render_template, request, redirect

from flask_app import app
from flask_app.models.author import Author
from flask_app.models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def dojos():
    return render_template("show_author.html", authors=Author.get_all())

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
def show(id):
    print(id)
    data ={ 
        "id":id
    }
    return render_template("a_fave.html",author=Author.authors_fave(data))

@app.route('/add/book', methods=['POST'])
def add_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    print(data)
    Author.save(data)
    return redirect ("/authors/<int:id>/")
