# app.py
from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models import db
from flask_migrate import Migrate
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import Book,Review
import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return "Book Review API is running!"

# GET all books
@app.route('/books', methods=['GET'])
def get_books():
    try:
        books = Book.query.all()
        data = []
        for x in books:
            data.append({
                "book_id": x.id,
                "book_title": x.title,
                "book_author": x.author
            })

        return jsonify({
            "status": "success",
            "status_code": 200,
            "data": data
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "status_code": 500,
            "message": "Failed to fetch books",
            "details": str(e)
        })


@app.route('/books', methods=['POST'])
def add_book():
    try:
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')

        if not title or not author:
            return jsonify({
                "status": "error",
                "status_code": 400,
                "message": "Title and Author are required"
            }), 400

        book = Book(title=title, author=author)
        db.session.add(book)
        db.session.commit()

        return jsonify({
            "status": "success",
            "status_code": 201,
            "message": "Book added successfully",
            "data": {
                "book_id": book.id,
                "book_title": book.title,
                "book_author": book.author
            }
        }), 201

    except Exception as e:
        return jsonify({
            "status": "error",
            "status_code": 500,
            "message": "Failed to add book",
            "details": str(e)
        }), 500



@app.route('/books/<int:book_id>/reviews', methods=['GET'])
def get_reviews(book_id):
    try:
        reviews = Review.query.filter_by(book_id=book_id).all()

        data = []
        average_rating=0
        
        for r in reviews:
            data.append({
                "review_id": r.id,
                "content": r.content,
                "rating": r.rating
            })
            average_rating=average_rating+r.rating
            
        

        return jsonify({
            "status": "success",
            "status_code": 200,
            "message": f"Found {len(data)} review(s) for book_id {book_id}",
            "data": data,
            "average_rating":average_rating/len(data)
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "status_code": 500,
            "message": "Failed to fetch reviews",
            "details": str(e)
        })


@app.route('/books/<int:book_id>/reviews', methods=['POST'])
def add_review(book_id):
    try:
        data = request.get_json()
        content = data.get('content')
        rating = data.get('rating')

        if not content or rating is None:
            return jsonify({
                "status": "error",
                "status_code": 400,
                "message": "Content and Rating are required"
            })

        review = Review(content=content, rating=rating, book_id=book_id)
        db.session.add(review)
        db.session.commit()

        return jsonify({
            "status": "success",
            "status_code": 201,
            "message": "Review added successfully",
            "data": {
                "review_id": review.id,
                "book_id": review.book_id,
                "content": review.content,
                "rating": review.rating
            }
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "status_code": 500,
            "message": "Failed to add review",
            "details": str(e)
        })


# Run
if __name__ == '__main__':
    app.run(debug=True)



