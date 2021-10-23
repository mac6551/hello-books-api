from flask import Blueprint, jsonify, make_response, request
from app import db
from app.models.book import Book

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST", "GET"])
def handle_books(): 
    if request.method == "POST":
        request_body = request.get_json()
        new_book = Book(title=request_body["title"],
                        description=request_body["description"])

        db.session.add(new_book)
        db.session.commit()

        return make_response(f"Book {new_book.title} successfully created", 201)
    
    elif request.method == "GET":
        books = Book.query.all()
        books_response = [vars(book) for book in books]
        return jsonify(books_response)

# @books_bp.route("", methods=["GET"])
# def get_books(): 
#     

# @books_bp.route("/<book_id>", methods=["GET"])
# def get_book(book_id): 
#     book_id = int(book_id)
#     return vars(next(b for b in books if b.id == book_id))



