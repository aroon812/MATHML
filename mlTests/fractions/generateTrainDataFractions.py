"""Generate training data for fractions"""
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
middleZone = 10

x_train = np.load('./../../../mlTestData/numbers/xData.npy')
y_train = np.load('./../../../mlTestData/numbers/yData.npy')

for pictureNum in range(3000):
    canvas = np.zeros([canvasXSize,canvasYSize,3],dtype=np.uint8)
    canvas.fill(255) 
    annotations = []

    x1 = random.randint(0, canvasXSize-numberXSize)
    y1 = random.randint(0, canvasYSize-(2*numberYSize)-middleZone)
    x2 = x1
    y2 = y1 + middleZone + numberYSize
    middleZoneY = y1 + numberYSize

    coord1 = (x1, y1)
    coordMid = (x1, middleZoneY)
    coord2 = (x2, y2)

    """
    print(coord1)
    print(coordMid)
    print(coord2)
    """

    imageIndex1 = random.randint(0, len(x_train)-1)
    imageIndex2 = random.randint(0, len(x_train)-1)

    addition1 = x_train[imageIndex1]
    addition2 = x_train[imageIndex2]
    """
    annotation = []
    annotation.append(0)
    annotation.append((x1+14)/canvasXSize)
    annotation.append((y1+14)/canvasYSize)
    annotation.append(numberXSize/canvasXSize)
    annotation.append(numberYSize/canvasYSize)
    """

    for i in range(numberXSize):
        for j in range(numberYSize):
            canvas[y1+j][x1+i] = addition1[j][i]
            canvas[y2+j][x2+i] = addition2[j][i]

    thickness = random.randint(1, 3)
    direction = random.randint(-1, 1)
    for i in range(numberXSize):
        direction += random.randint(-1, 1)
        yLoc = int(middleZoneY + (middleZone/2) + direction)
        for j in range(thickness):
            canvas[yLoc-j][x1+i] = [0,0,0]
            canvas[yLoc+j][x1+i] = [0,0,0]

    annotation = []
    annotation.append(0)
    annotation.append((x1+(numberXSize/2))/canvasXSize)
    annotation.append((y1 + numberYSize + (middleZone/2))/canvasYSize)
    annotation.append(numberXSize/canvasXSize)
    annotation.append(((2*(numberYSize))+middleZone)/canvasYSize)
    annotations.append(annotation)

    annotations = np.array(annotations)
    
    canvas = Image.fromarray(canvas)
    fileNamePNG = 'objDetect' + str(pictureNum) + '.png'
    fileNameTXT = 'objDetect' + str(pictureNum) + '.txt'
    pathPNG = './../../../mlTestData/fractionData/' + fileNamePNG
    pathTXT = './../../../mlTestData/fractionData/' + fileNameTXT
    print("saving " + pathPNG)
    canvas.save(pathPNG)
    np.savetxt(pathTXT, annotations, fmt='%u %f %f %f %f')
    

