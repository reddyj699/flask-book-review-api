
📘 
Flask Book Review API

📝 Description

A lightweight, RESTful API built using Flask, SQLAlchemy, and MySQL for managing books and their reviews.
This project is ideal for developers learning backend development, database integration, or REST API design using Python.








Acknowledgements

This project was made possible thanks to the following tools, libraries, and resources:

Flask – Lightweight Python web framework used to build the RESTful API

SQLAlchemy – ORM used to define and manage the relational database models

Flask-Migrate – Database migration tool powered by Alembic

PyMySQL – MySQL client for Python used to connect the Flask app to MySQL

Postman – Used for testing API endpoints during development

GitHub Docs – For repository management and Git best practices


## API Reference

#### Get all books

```http
  GET /books
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-` | `-` | 	Returns a list of all books |

#### Get all reviews for a book

```http
  GET /books/${book_id}/reviews
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `book_id`      | `int` | **Required**. Id of Book to fetch the reviews |

#### Add a new book

```http
  Post /books
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `title`      | `string` | **Required**. Title of the book |
| `author`      | `string` | **Required**. Author of the book |


#### Add a review to a book

```http
  Post /books/${book_id}/reviews
```
| Url_Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `book_id`      | `int` | **Required**. ID of the book to add the review to |



| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `content`      | `string` | **Required**. Text content of the review|
| `rating`      | `int` | **Required**.Rating value (e.g., 1–5) |


## Appendix

This API was developed as a learning project to demonstrate integration of Flask, SQLAlchemy, and MySQL with RESTful design principles.

The project uses Flask-Migrate for version-controlled schema migrations.

All endpoints return structured JSON responses with consistent keys: status, status_code, message, and data.

Postman or cURL can be used to test the API endpoints during development.

Ensure MySQL is installed and running locally, and that the database credentials are correctly set in config.py.

For production, environment variables should be used to manage sensitive configurations (e.g., DB passwords).

This API can be extended to include user authentication, pagination, review timestamps, and search/filter features.
# Deployment

## 1. Clone the repository
git clone https://github.com/reddyj699@gmail.com/flask-book-review-api.git
cd flask-book-review-api

## 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

## 3. Install dependencies
pip install -r requirements.txt

## 4. Configure your database in config.py
Example: 'mysql+pymysql://root:1234@localhost/book_review_db'

## 5. Initialize the database (run migrations)
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

## 6. Start the Flask development server
flask run


## Installation

✅ requirements.txt


```bash
Flask==2.3.2
Flask-SQLAlchemy==3.1.1
Flask-Migrate==4.0.5
PyMySQL==1.1.0

```
pip install -r requirements.txt

    
