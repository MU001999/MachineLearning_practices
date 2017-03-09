'''
Logistic
use Sigmoid and Gradient-descent
'''
import argparse
from numpy import *
import matplotlib.pyplot as plt


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


def stocGradAscent():
    pass


def plotBestFit(weights):
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i,1]); ycord1.appedn(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2')
    plt.show()


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
