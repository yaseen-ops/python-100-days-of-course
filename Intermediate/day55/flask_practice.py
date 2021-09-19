from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"


@app.route("/<name>")    # Assign as variable and get input while hitting the URL with name or actual value
def my_name(name):
    return f"<h2>Hello {name}!<h2>"


@app.route("/userdata/<name>/<int:age>")   # data types can be converted
def user_data(name, age):
    return f"Hello {name}, your age is {age}"


if __name__ == "__main__":
    app.run(port=80, debug=True)
    # Advantages of enabling debugger
    # If you change in the file no need to stop/start flask, it will reload automatically
    # If for any issue, it will show you the error debug message in the browser itself


