"""Uses Numpy to serialize datasets for 
   faster loading
"""
import numpy as np
import random 
from PIL import Image
import os

#change these directories for different data sets
trainDirectories = ['C:/Users/steal/Desktop/poloProjectData/EMNISTdata/digits/training', 'C:/Users/steal/Desktop/poloProjectData/EMNISTdata/MNIST/training']
testDirectories = ['C:/Users/steal/Desktop/poloProjectData/EMNISTdata/digits/testing', 'C:/Users/steal/Desktop/poloProjectData/EMNISTdata/MNIST/testing']
numClasses = 10
numberXSize = 28
numberYSize = 28
x_train = []
y_train = []
x_test = []
y_test = []

for directory in trainDirectories:
    for i in range(numClasses):
        newDirectory = os.path.join(directory, str(i))
        print(newDirectory)
        for filename in os.listdir(newDirectory):
            if filename.endswith(".png"):
                newPath = os.path.join(newDirectory, filename)
                print(newPath)
                img = Image.open(newPath).convert('L')
                img = np.array(img)
                img = img.reshape(numberXSize, numberYSize, 1)
                x_train.append(img)
                y_train.append(i)

for directory in testDirectories:
    for i in range(numClasses):
        newDirectory = os.path.join(directory, str(i))
        print(newDirectory)
        for filename in os.listdir(newDirectory):
            if filename.endswith(".png"):
                newPath = os.path.join(newDirectory, filename)
                print(newPath)
                img = Image.open(newPath).convert('L')
                img = np.array(img)
                img = img.reshape(numberXSize, numberYSize, 1)
                x_test.append(img)
                y_test.append(i)

x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

np.save('serializedDataSets/xTrain.npy', x_train)
np.save('serializedDataSets/xTest.npy', x_test)
np.save('serializedDataSets/yTrain.npy', y_train)
np.save('serializedDataSets/yTest.npy', y_test)


