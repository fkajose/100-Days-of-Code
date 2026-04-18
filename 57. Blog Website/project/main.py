from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)


@app.route('/')
def home():
    blog_url = "https://api.npoint.io/1ad80cb61d6c22baaaaf"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", all_posts=all_posts)


@app.route('/post/<int:id>')
def get_post(id):
    post = Post(id)
    return render_template("post.html", blog_post=post)


if __name__ == "__main__":
    app.run(debug=True)
