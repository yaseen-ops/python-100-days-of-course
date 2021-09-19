from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    data = """
    <h2>Hello, World!</h2>
    <p>Hello, World!</p>
    """
    return data


# app.run()
if __name__ == "__main__":
    app.run(port=80)
