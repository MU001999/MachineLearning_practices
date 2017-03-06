'''
Logistic
use Sigmoid and Gradient-descent
'''
import argparse
from numpy import *


def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
          lineArr = line.strip().split()
          dataMat.append([1.0, float(lineArr[0], float(lineArr[1]))])
          labelMat.append(int(lineArr[2]))
    return dataMat,labelMat


def loadSingleData():
    pass


def Sigmoid(inX):
    return 1.0/(1+exp(-inX))


def gradAscent(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)
    LabelMat = mat(classLabels,).transpose()
    m,n = shape(dataMatrix)
    alpha = 0.001
    maxCycles = 500
    weights = ones((n,1))
    for k in range(maxCycles):
          h = Sigmoid(dataMatrix*weights)
          error = (LabelMat - h)
          weights = weights + alpha * dataMatrix.transpose() * error
    return weights


def train():
    pass


def predict():
    pass


def main(args):
    pass


def parse_get():
    parser = argparse.ArgumentParser('Logistic')
    parser.add_argument('--dataUrl',type=str,help=None)
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_get()
    main(args)
