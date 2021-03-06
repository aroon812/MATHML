"""Uses Numpy to serialize datasets for 
   faster loading
"""
import numpy as np
import random 
from PIL import Image
import os

#change these directories for different data sets
trainDirectories = ['EMNIST/digits/training', 'EMNIST/MNIST/training']
testDirectories = ['EMNIST/digits/testing', 'EMNIST/MNIST/testing']
letterDirectories = ['EMNIST/letters/training', 'EMNIST/letters/testing']
numNumbers = 10
numLetters = 26
numberXSize = 28
numberYSize = 28
x_data = []
y_data = []

for directory in trainDirectories:
    for i in range(numNumbers):
        newDirectory = os.path.join(directory, str(i))
        print(newDirectory)
        for filename in os.listdir(newDirectory):
            if filename.endswith(".png"):
                newPath = os.path.join(newDirectory, filename)
                print(newPath)
                img = Image.open(newPath).convert('L')
                img = np.array(img)
                img = img.reshape(numberXSize, numberYSize, 1)
                x_data.append(img)
                y_data.append(i)

for directory in testDirectories:
    for i in range(numNumbers):
        newDirectory = os.path.join(directory, str(i))
        print(newDirectory)
        for filename in os.listdir(newDirectory):
            if filename.endswith(".png"):
                newPath = os.path.join(newDirectory, filename)
                print(newPath)
                img = Image.open(newPath).convert('L')
                img = np.array(img)
                img = img.reshape(numberXSize, numberYSize, 1)
                x_data.append(img)
                y_data.append(i)

for directory in letterDirectories:
    for i in range(numLetters):
        newDirectory = os.path.join(directory, str(chr(i+65)))
        print(newDirectory)
        for filename in os.listdir(newDirectory):
            if filename.endswith(".png"):
                newPath = os.path.join(newDirectory, filename)
                print(newPath)
                img = Image.open(newPath).convert('L')
                img = np.array(img)
                img = img.reshape(numberXSize, numberYSize, 1)
                x_data.append(img)
                y_data.append(i+10)
                print(i+10)

x_data = np.array(x_data)
y_data = np.array(y_data)

np.save('NumpyArrays/xData.npy', x_data)
np.save('NumpyArrays/yData.npy', y_data)


