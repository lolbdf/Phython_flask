from flask import Flask, url_for

app = Flask(__name__)


@app.route("/<string:name>")
def index(name):
    return '<a href=' + url_for("hello", name="world") + '>lass dich grüßen ' + name + '</a>'


@app.route("/hello/<string:name>")
def hello(name):
    return "Hello " + name + "!"


if __name__ == "__main__":
    app.run(port=1337, debug=True)
