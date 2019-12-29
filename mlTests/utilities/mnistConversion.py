#!/usr/bin/env python

import os
import struct
import sys
import png
import numpy as np
from PIL import Image
import scipy.misc

from array import array
from os import path
# source: http://abel.ee.ucla.edu/cvxopt/_downloads/mnist.py

def read(dataset="training", path="."):
    if dataset is "training":
        fname_img = os.path.join(path, 'emnist-mnist-train-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'emnist-mnist-train-labels-idx1-ubyte')
    elif dataset is "testing":
        fname_img = os.path.join(path, 'emnist-mnist-test-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'emnist-mnist-test-labels-idx1-ubyte')
    else:
        raise ValueError("dataset must be 'testing' or 'training'")

    flbl = open(fname_lbl, 'rb')
    magic_nr, size = struct.unpack(">II", flbl.read(8))
    lbl = array("b", flbl.read())
    flbl.close()

    fimg = open(fname_img, 'rb')
    magic_nr, size, rows, cols = struct.unpack(">IIII", fimg.read(16))
    img = array("B", fimg.read())
    fimg.close()

    return lbl, img, size, rows, cols


def write_dataset(labels, data, size, rows, cols, output_dir):
    # create output directories
    output_dirs = [
        path.join(output_dir, str(i))
        for i in range(10)
    ]
    for dir in output_dirs:
        if not path.exists(dir):
            os.makedirs(dir)

    # - output_filename -> C:/Users/steal/Desktop/newData/training/2/0.png

    # write data
    for (i, label) in enumerate(labels):
        output_filename = path.join(output_dirs[label], str(i) + ".png")
        print("writing " + output_filename)
        with open(output_filename, "wb") as h:
            #w = png.Writer(cols, rows, greyscale=True)
            data_i = [
                data[(i*rows*cols + j*cols): (i*rows*cols + (j+1)*cols)]
                for j in range(rows)
            ]
            image = np.rot90(np.fliplr(data_i))
            scipy.misc.imsave(output_filename, image)

if __name__ == "__main__":

    input_path = '/home/aroon/Desktop/AroonDataConversionToolsAndResourcesWhichMightBeUseful/gzip/extracted'
    output_path = '/home/aroon/Desktop/EMNISTLetters/MNIST'

    for dataset in ["training", "testing"]:
        labels, data, size, rows, cols = read(dataset, input_path)
        write_dataset(labels, data, size, rows, cols,
                      path.join(output_path, dataset))
