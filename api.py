import flask
from flask import (
    request,
    jsonify
)
import sqlite3


app = flask.Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for index, col in enumerate(cursor.description):
        d[col[0]] = row[index]
    return d

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    all_books = cur.execute('SELECT * FROM books;').fetchall()
    return jsonify(all_books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL
    # If ID is provided, assign it to a var
    # If no ID is provided, display an error in the browser
    query_params = request.args

    id = query_params.get('id')
    published = query_params.get('published')
    author = query_params.get('author')
    
    query = "SELECT * FROM books WHERE"
    print("query: {}".format(query))
    to_filter = list()

    if id:
        query += " id=? AND"        
        to_filter.append(id)

    if published:
        query += " published=? AND"
        to_filter.append(published)

    if author:
        query += " author=? AND"
        to_filter.append(author)

    if not (id or published or author):
        return page_not_found(404)

    query = query[:-1] + ';'
    print(query)

    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)

    for book in books:
        if book['id'] == id:
            results.append(book)
    
    return jsonify(results)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

app.run()
