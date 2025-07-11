from flask import Flask, render_template
from tkinter import *
import json

import requests

app = Flask(__name__,template_folder='templates')

@app.route('/')
def index():
    datosObtenidos = requests.get('https://www.google.com/maps/embed?pb=!1m24!1m8!1m3!1d1423760.7200647807!2d-71.76897957663357!3d-34.02009703119218!3m2!1i1024!2i768!4f13.1!4m13!3e2!4m5!1s0x9662c5410425af2f%3A0x505e1131102b91d!2sChile!3m2!1d-35.675146999999996!2d-71.542969!4m5!1s0x9662c5410425af2f%3A0x505e1131102b91d!2sChile!3m2!1d-35.675146999999996!2d-71.542969!5e0!3m2!1ses!2sve!4v1751929782839!5m2!1ses!2sve" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade')
    datosFormatoJSON = datosObtenidos.json()
    print(datosFormatoJSON)

    return render_template('pruebazona.html')
    #return render_template('myapp.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
