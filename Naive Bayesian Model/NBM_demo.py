'''
Naive Bayesian Model
'''
import argparse
import os
import numpy


def loadData(url):
    pass


def loadSingleData(url):
    pass


def trainNBM():
    pass


def predictData(url):
    simple = trainNBM()
    singleData = loadSingleData(url)
    res =  calculate(simple, singleData)


def calculate(simple, singleData):
    pass


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
