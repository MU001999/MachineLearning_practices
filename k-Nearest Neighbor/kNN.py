"""
    k-Nearest Neighbor ( kNN
    k <= 20 ( k is 7 in this demo
    the kNN demo for the classification handwritten numbers
"""

import argparse
import numpy as np
import panda as pd
import math
import os


def train(args):
    pass


def predic(args):
    pass


def parse_args():
    parser = argparse.ArgumentParser(description="the kNN demo")

    parser.add_argument("--train", help="choose training and input the path of the dataset", type=str, default=None)
    parser.add_argument("--dim", help="the num of the dim", type=int, default=2)

    parser.add_argument("--predict", help="choose predicting", action="store_true")
    parser.add_argument("--proposed", help="the path of the proposed model", type=str, default=None)
    parser.add_argument("--data", help="the path of the data that be predicting", type=str, default=None)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    if args.predict:
        predict(args)
    else:
        train(args)