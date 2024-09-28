from flask import Flask
from flask import render_template
from flask import request

from tensorflow.keras.models import load_model
from tensorflow.nn import softmax

import numpy as np
from PIL import Image
import io
import base64

model = load_model("assets/model")

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/Centers')
def centers():
    return render_template('Centers.html')
@app.route('/Scan', methods=["GET", "POST"])
def scan():
    return render_template('Scan.html')

      
if __name__ == '__main__':
  app.run()
