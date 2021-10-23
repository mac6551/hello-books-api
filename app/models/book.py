from app import db

class Book(db.Model): 
    id = db.Column(db.Interger, primary_key = True, autoincrement = True)
    title = db.Column(db.String)
    description = db.Column(db.String)

