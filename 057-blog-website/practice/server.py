from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)
year = datetime.datetime.now().year
id_num = random.randint(1, 3)


@app.route('/')
def hello():
    num = random.randint(0, year)
    return render_template("index.html", num=num, year=year, id_num=id_num)


@app.route('/guess/<name>')
def guess_age(name):
    name = name.title()
    get_gender = requests.get(f"https://api.genderize.io?name={name}")
    gender = get_gender.json()["gender"]
    get_age = requests.get(f"https://api.agify.io?name={name}")
    age = get_age.json()["age"]
    return render_template("guess.html", name=name, sex=gender, age=age, year=year)


@app.route('/blog/<id_num>')
def get_blog(id_num):
    blog_url = "https://api.npoint.io/1ad80cb61d6c22baaaaf"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", all_posts=all_posts, id_num=int(id_num))


if __name__ == '__main__':
    app.run(debug=True)
