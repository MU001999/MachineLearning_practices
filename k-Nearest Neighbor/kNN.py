"""
    k-Nearest Neighbor ( kNN
    k <= 20 ( k is 7 in this demo
    the kNN demo for the classification handwritten numbers
"""

import argparse
import Image
import numpy as np
import math
import os


def load_sample_data(url):
    labels = []
    data = []
    for num in range(10):
        for file_name in os.listdir(url+'/'+str(num)):
            labels.append(num)
            data.append(load_sample_data(url+'/'+str(num)+'/'+file_name))
    return data, labels


def load_single_image(url):
    img = Image.open(url)
    img = img.convert('L')
    img = img.resize((28,28),Image.ANTIALIAS)
    img = np.asarry(img, dtype=np.uint8)
    return img


def sort_k(results):
    nums = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
    for item in results[0:7]:
        nums[str(item[0])]+=1
    items = nums.items()
    items.sort(reverse=True)
    return [key for key,value in items]


def dis(data_a,data_b):
    sum = 0
    for i in range(28):
        for j in range(28):
            sum += abs(data_a[i][j]-data_b[i][j])
    return sum


def calculate(s_data):
    result_types = []
    sample_data, sample_labels = load_sample_data("sample_data")
    for i in range(len(sample_labels)):
        result_types.append((sample_labels[i,dis(s_data,sample_data[i]))
    result_types.sort(key=lambda x:x[1],reverse=True)
    results = sort_k(results_types)
    return results


def classify(args):
    single_data = load_single_image(args.url)
    results = calculate(single_data)
    if args.vis:
        print "result is may:", results[0]
    else:
        pass


def parse_args():
    parser = argparse.ArgumentParser(description="the kNN demo")
    parser.add_argument("--url",help="the image url",type=str)
    parser.add_argument("--vis",help="display the result and the image",action="store_true")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    classify(args)
