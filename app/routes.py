from flask import Flask, jsonify



books_bp = Blueprint("books", __name__, url_prefix="/books")

# @books_bp.route("", methods=["GET"])
# def get_books(): 
#     books_response = [vars(book) for book in books]
#     return jsonify(books_response)

# @books_bp.route("/<book_id>", methods=["GET"])
# def get_book(book_id): 
#     book_id = int(book_id)
#     return vars(next(b for b in books if b.id == book_id))



