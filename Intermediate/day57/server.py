import random
import requests
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    current_year = datetime.now().year
    random_number = random.randint(1, 10)
    return render_template('index.html', num=random_number, year=current_year)


@app.route("/guess/<name>")
def guess(name):
    person_name = name.title()
    gender_url = "https://api.genderize.io?name=" + person_name
    response = requests.get(gender_url)
    gender = response.json().get("gender")

    age_url = "https://api.agify.io/?name=" + person_name
    response = requests.get(age_url)
    age = response.json().get("age")

    return render_template('guess.html', name=person_name, gender=gender, age=age)


@app.route("/blog")
def get_blog():
    api_url = "https://api.npoint.io/454b0b4a8cdca3afaee7"
    response = requests.get(api_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(port=80, debug=True)
