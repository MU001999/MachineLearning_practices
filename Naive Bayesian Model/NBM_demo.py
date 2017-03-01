'''
Naive Bayesian Model
easy model
just have 2 classes and cannot extend
'''
import argparse
import os
import numpy


def loadData(url='\\trainDemo'):
    # demo
    res = []
    for filename in os.listdir(os.getcwd()+url):
        with open(filename,'r') as aTxt:
            oneTxt = {list[aTxt.read().split(' ')]:filename[-1]}
        res.append(oneTxt)
    return res


def loadSingleData(url):
    with open(url,'r') as aTxt:
        oneTxt = list[aTxt.read().split(' ')]
    return oneTxt


def trainNBM():
    data = loadData()
    numAll = len(data)
    simpleNBM = {}
    for i in range(0,numAll):
        for item in data[numAll]:
            for word in item:
                if word not in simpleNBM:
                    simpleNBM[word] = [0.0,0.0]
    # the process
    return simpleNBM


def predictData(url):
    simple = trainNBM()
    singleData = loadSingleData(url)
    res =  calculate(simple, singleData)
    print res


def calculate(simple, singleData):
    res = {'T':0.0,'F':0.0}
    for word in singleData:
        if word in simple:
            res['T']+=simple[word][0]
            res['F']+=simple[word][1]
    if res['T']>res['F']:
        return 'T'
    else:
        return 'F'


def parseGet():
    parser = argparse.ArgumentParser()
    parser.add_argument('--singleDataUrl',help='the url of the data that needs to be predicted',type=str)
    args = parser.parse_args()
    return args


def main():
    args = parseGet()
    predict(args.singleDataUrl)


if __name__ == '__main__':
    main()
