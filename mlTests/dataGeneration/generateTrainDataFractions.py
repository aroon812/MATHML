"""Generate training data for fractions"""
import numpy as np
import random 
import os
from PIL import Image
from Objects.fraction import Fraction

canvasXSize = 416
canvasYSize = 416
dataSetSize = 1

for pictureNum in range(dataSetSize):
    canvas = np.zeros([canvasXSize,canvasYSize,3],dtype=np.uint8)
    canvas.fill(255) 

    fraction = Fraction()
    x = random.randint(0, canvasXSize-fraction.length)
    y = random.randint(0, canvasYSize-fraction.height)
    
    for i in range(fraction.height):
        for j in range(fraction.length):
            canvas[y+i][x+j] = fraction.array[i][j]

    annotations = fraction.createYoloLabel(x, y, canvasXSize, canvasYSize)
    annotations = np.array(annotations)
    canvas = Image.fromarray(canvas)
    fileNamePNG = 'objDetect' + str(pictureNum) + '.png'
    fileNameTXT = 'objDetect' + str(pictureNum) + '.txt'
    pathPNG = './../../../mlTestData/fractionData/' + fileNamePNG
    pathTXT = './../../../mlTestData/fractionData/' + fileNameTXT
    print("saving " + pathPNG)
    canvas.save(pathPNG)
    np.savetxt(pathTXT, annotations, fmt='%u %f %f %f %f')
    
