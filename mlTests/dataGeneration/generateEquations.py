"""Generate training data for equations"""
import numpy as np
import random 
import os
from PIL import Image
from Objects.equation import Equation

canvasXSize = 416
canvasYSize = 416
dataSetSize = 1

for pictureNum in range(dataSetSize):
    canvas = np.zeros([canvasXSize,canvasYSize,3],dtype=np.uint8)
    canvas.fill(255) 

    equation = Equation()
    x = random.randint(0, canvasXSize-equation.length)
    y = random.randint(0, canvasYSize-equation.height)
    
    for i in range(equation.height):
        for j in range(equation.length):
            canvas[y+i][x+j] = equation.array[i][j]

    annotations = equation.createYoloLabel(x, y, canvasXSize, canvasYSize)
    annotations = np.array(annotations)
    canvas = Image.fromarray(canvas)
    fileNamePNG = 'objDetect' + str(pictureNum) + '.png'
    fileNameTXT = 'objDetect' + str(pictureNum) + '.txt'
    pathPNG = './../../../mlTestData/equationData/' + fileNamePNG
    pathTXT = './../../../mlTestData/equationData/' + fileNameTXT
    print("saving " + pathPNG)
    canvas.save(pathPNG)
    np.savetxt(pathTXT, annotations, fmt='%u %f %f %f %f')
    