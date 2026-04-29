# from unittest.mock import Base

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, desc
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)


# CREATE DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///top-movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.ranking.desc()))
    all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)


@app.route("/update", methods=["GET", "POST"])
def update():
    form = RateMovieForm()
    if form.validate_on_submit():
        movie_id = request.args.get("id")
        movie = db.get_or_404(Movie, movie_id)
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        return redirect(url_for("home"))
    return render_template("add.html", form=form)
    # if request.method == "POST":
    #     movie_title = request.form.get("title")
    #     response = requests.get(
    #         "https://api.themoviedb.org/3/search/movie",
    #         params={"api_key": "a9c1e1c8d0f2b4e7aabf0cfeeea9cde", "query": movie_title},
    #     )
    #     data = response.json()["results"]
    #     return render_template("select.html", options=data)
    # return render_template("add.html", )


if __name__ == "__main__":
    app.run(debug=True)
