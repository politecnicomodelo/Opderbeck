from flask import flask
app = Flask(__name__)
@app.route('/')
def index():
    return
app.ru0n(debug = True, port = 5000)