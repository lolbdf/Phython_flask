from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to title page!"


@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(port=1337, debug=True)