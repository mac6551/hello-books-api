from flask import Blueprint, jsonify

class Book:
    def __init__(self, id, title, description): 
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Interview with a Vampire", "The first book in Anne Rice's Vampire Chronicles."),
    Book(2, "The Vampire Lestat", "The second book in Anne Rice's Vampire Chronicles."), 
    Book(3, "Queen of the Damned", "The third book in Anne Rice's Vampire Chronicles")
]

books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["GET"])
def get_books(): 
    books_response = []
    for book in books: 
        books_response.append({
            "id": book.id,
            "title": book.title, 
            "description": book.description
        })
    return jsonify(books_response)

@books_bp.route("/<book_id>", methods=["GET"])
def get_book(book_id): 
    book_id = int(book_id)
    for book in books: 
        if book.id == book_id: 
            return{
                "id": book.id,
                "title": book.title, 
                "description": book.description
            }

