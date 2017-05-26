import os
import cv2
import json
import numpy as np
import mxnet as mx
import pickle
from collections import namedtuple
from werkzeug import secure_filename
from flask import Flask, jsonify, make_response, request

import c10p

ALLOWED_EXTENSIONS = set(['jpg', 'png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploadImgs'


def allowed_file(filename):
    return '.' in filename and filename.split('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        res = c10p.predict(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return json.dumps(res)
    return jsonify({'error': "Not success"})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
