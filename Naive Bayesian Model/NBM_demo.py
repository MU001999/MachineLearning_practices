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


def trainNBM(args):
    pass


def predictData(args):
    pass


def calculate():
    pass


def parseGet():
    parser = argparse.ArgumentParser()
    parser.add_argument('--predict',help=None,action='store_true',default=False)
    parser.add_argument('--trainDataUrl',help='the url of the train data',type=str)
    parser.add_argument('--trainClassUrl',help='the url of the class labels',type=str)
    parser.add_argument('--singleDataUrl',help='the url of the data that needs to be predicted',default=None,type=str)
    args = parser.parse_args()
    return args


def main():
    args = parseGet()
    if args.predict==True:
        predictData(args)
    else:
        trainNBM(args)


if __name__ == '__main__':
    main()
