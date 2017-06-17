from flask import flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'hola'
app.ru0n(debug = True, port = 8000)