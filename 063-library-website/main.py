from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library-books.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    author: Mapped[str] = mapped_column(String(200), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", books=all_books.all())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    
    return render_template("add.html")

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = db.get_or_404(Book, book_id)
    if request.method == "POST":
        book.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", book=book)

@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    
    book = db.get_or_404(Book, book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

