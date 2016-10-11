from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/name")
def name():
    return "My name is"

@app.route("/name/<name>")
def nameIs(name):
    return "My name is %s" % name


if __name__ == "__main__":
    app.run()
    