"""Generate training data from smaller 
   images for object detection on a single class.
"""
import numpy as np
import random 
import os
from PIL import Image

numberXSize = 28
numberYSize = 28
canvasXSize = 416
canvasYSize = 416
numClass = 5
dataSetSize = 3000

x_train = np.load('/home/aroon/Desktop/NumpyArrays/xTrain.npy')
y_train = np.load('/home/aroon/Desktop/NumpyArrays/yTrain.npy')
x_train_single = []

for i in range(0, len(x_train)-1):
    if int(y_train[i]) is numClass:
        x_train_single.append(x_train[i])

for pictureNum in range(3000):
    canvas = np.zeros([canvasXSize,canvasYSize,3],dtype=np.uint8)
    canvas.fill(255) 
    annotations = []

    x = random.randint(0, canvasXSize-numberXSize)
    y = random.randint(0, canvasYSize-numberYSize)
    imageIndex = random.randint(0, len(x_train_single)-1)

    addition = x_train_single[imageIndex]
    annotation = []
    annotation.append(0)
    annotation.append((x+14)/canvasXSize)
    annotation.append((y+14)/canvasYSize)
    annotation.append(numberXSize/canvasXSize)
    annotation.append(numberYSize/canvasYSize)

    for i in range(numberXSize):
        for j in range(numberYSize):
            canvas[y+j][x+i] = addition[j][i]

    annotations.append(annotation)
    annotations = np.array(annotations)
    
    canvas = Image.fromarray(canvas)
    fileNamePNG = 'objDetect' + str(pictureNum) + '.png'
    fileNameJPG = 'objDetect' + str(pictureNum) + '.jpg'
    fileNameTXT = 'objDetect' + str(pictureNum) + '.txt'
    pathPNG = '/home/aroon/Desktop/YOLOTrainingDataSingle/' + fileNamePNG
    pathJPG = '/home/aroon/Desktop/YOLOTrainingDataSingle/' + fileNameJPG
    pathTXT = '/home/aroon/Desktop/YOLOTrainingDataSingle/' + fileNameTXT
    print(pathJPG)
    canvas.save(pathPNG)
    image = Image.open(pathPNG)
    rgbImage = image.convert('RGB')
    rgbImage.save(pathJPG)
    os.remove(pathPNG)
    np.savetxt(pathTXT, annotations, fmt='%u %f %f %f %f')
    

