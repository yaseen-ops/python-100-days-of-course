from flask import Flask, render_template
from post import Post
from datetime import datetime
import requests

CURRENT_YEAR = datetime.now().year
URL = "https://api.npoint.io/454b0b4a8cdca3afaee7"

posts = requests.get(URL).json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["content"])
    post_objects.append(post_obj)

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects, year=CURRENT_YEAR)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(port=80, debug=True)
