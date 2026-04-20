from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/7ffde18fb59256cc0932"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
