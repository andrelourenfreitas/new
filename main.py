from flask import flask
app = Flask(_name_)

@app.route("/")
def hello_word():
    return "<p>Heloo, World</p>"
