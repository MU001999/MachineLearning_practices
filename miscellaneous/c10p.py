import os
import cv2
import json
import numpy as np
import mxnet as mx
import pickle
from collections import namedtuple


def load_batches_meta():
    file = open('batches.meta', 'rb')
    datadict = pickle.load(file)
    file.close()
    return datadict['label_names']


labels = load_batches_meta()

Batch = namedtuple('Batch', ['data'])

mod = mx.model.FeedForward.load('CIFAR_MXNet', 100)

def predict(img):
    img = cv2.imread(img)
    img = cv2.resize(img, (32, 32))
    img = np.asarray(img, dtype=np.uint8)
    img = img.reshape(1, 3, 32, 32).astype(np.float32) / 255
    val = mx.io.NDArrayIter(data=img)
    prob = mod.predict(X=val)
    prob = np.squeeze(prob)
    a = np.argsort(prob)[::-1]
    return [{'class': labels[i], 'probability': '{%.2f}'%(prob[i])} for i in a[0:5]]


if __name__ == "__main__":
    while (1):
        img_url = raw_input("Enter the img_url: ")
        for item in predict(img_url):
            print item
