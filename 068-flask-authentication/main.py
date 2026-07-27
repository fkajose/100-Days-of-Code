from flask import (
    Flask,
    render_template,
    request,
    url_for,
    redirect,
    flash,
    send_from_directory,
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    login_required,
    current_user,
    logout_user,
)

app = Flask(__name__)
app.config["SECRET_KEY"] = "dhf5gw622q"

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# CREATE TABLE IN DB


class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
    # is_authenticated: Mapped[bool] = mapped_column(default=False)
    # is_active: Mapped[bool] = mapped_column(default=True)
    # is_anonymous: Mapped[bool] = mapped_column(default=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered. Please log in.", "error")
            return redirect(url_for("login"))

        # # Hash the password
        hashed_password = generate_password_hash(
            password, method="pbkdf2:sha256", salt_length=8
        )

        # Create new user
        new_user = User(email=email, password=hashed_password, name=name)
        db.session.add(new_user)
        db.session.commit()

        # flash("Registration successful! Please log in.", "success")
        return render_template("secrets.html", name=name)
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Find user by email
        user = User.query.filter_by(email=email).first()

        if not user:
            flash("Email does not exist. Please register first.", "error")
            return redirect(url_for("register"))

        # Check password
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("secrets"))
        else:
            flash("Incorrect password. Please try again.", "error")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/secrets", methods=["GET", "POST"])
@login_required
def secrets():
    return render_template("secrets.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route("/download")
@login_required
def download():
    return send_from_directory("static", path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
