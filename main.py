from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return f"<h1>elcome To The END!.<h1>"


@app.route("/info")
def info():
    return f"<h1>The One And Only!.<h1>"


@app.route("/me")
def me():
    return f"<h1>@********tools.<h1>"


if __name__ == "__main__":
    app.run()
