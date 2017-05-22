import os
import cv2
import json
import numpy as np
import mxnet as mx
from collections import namedtuple
from werkzeug import secure_filename
from flask import Flask, jsonify, make_response, request

ALLOWED_EXTENSIONS = set(['jpg', 'png'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploadImgs'


path = 'http://data.mxnet.io/models/imagenet-11k/'
mx.test_utils.download(path+'resnet-152/resnet-152-symbol.json')
mx.test_utils.download(path+'resnet-152/resnet-152-0000.params')
mx.test_utils.download(path+'synset.txt')

sym, arg_params, aux_params = mx.model.load_checkpoint('resnet-152', 0)
mod = mx.mod.Module(symbol=sym, context=mx.gpu())
mod.bind(for_training=False, data_shapes=['data', (1,3,224,224)])
mod.set_params(arg_params, aux_params)
with open('synset.txt', 'r') as f:
    labels = [l.strip() for l in f]

Batch = namedtuple('Batch', ['data'])


def predict(img):
    img = cv2.cvtColor(cv2.imread(img), cv2.COLOR_RGB2RGB)
    img = cv2.resize(img, (224, 224))
    img = np.swapaxes(img, 0, 2)
    img = np.swapaxes(img, 1, 2)
    img = img[np.newaxis, :]
    mod.forward(Batch([mx.nd.array(img)]))
    prob = mod.get_outputs()[0].asnumpy()
    prob = np.squeeze(prob)
    return [{'class': labels[i], 'probability': prob[i]} for i in prob[0:5]]


def allowed_file(filename):
    return '.' in filename and filename.split('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        res = predict(file)
        return json.dumps(res)
    return jsonify({'error': "Not success"})


if __name__ == "__main__":
    app.run(debug=True)
