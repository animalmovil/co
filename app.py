
from flask import Flask, render_template
import requests

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():

    return render_template('inicio.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 