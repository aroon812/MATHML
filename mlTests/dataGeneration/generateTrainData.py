"""Generate training data from smaller 
   images for object detection.
   (currently working on multi class detection for fractions)
"""
import numpy as np
import random 
import os
import multiprocessing 
from Objects.equation import Equation
from PIL import Image

numThreads = 12
dataSetSize = 90000
canvasXSize = 416
canvasYSize = 416

def generateRandomCoordinate(objectLength, objectHeight):
    """Generate a random starting coordinate"""
    x = random.randint(0, canvasXSize-objectLength)
    y = random.randint(0, canvasYSize-objectHeight)
    return (x, y)

def generateData(startPoint, endPoint, procNum):
    """Generate pictures of random equations (currently fractions).
    startpoint and endpoint should be dependent on which thread
    is running the function.
    """
    counter = np.zeros(42)
    for pictureNum in range(startPoint, endPoint):
        canvas = np.zeros([canvasXSize,canvasYSize,3],dtype=np.uint8)
        canvas.fill(255) 

        equation = Equation()
        x, y = generateRandomCoordinate(equation.length, equation.height)
        for i in range(equation.height):
            for j in range(equation.length):
                canvas[y+i][x+j] = equation.array[i][j]
        
        """
        finish
        """
        for item in equation.objects:
            counter[item.label] += 1 
        counter[equation.label] += 1 
           

        annotation = equation.createYoloLabel(x, y, canvasXSize, canvasYSize)
        annotation = np.array(annotation)
        canvas = Image.fromarray(canvas)
        fileNamePNG = 'objDetect' + str(pictureNum) + '.png'
        fileNameTXT = 'objDetect' + str(pictureNum) + '.txt'
        pathPNG = './../../../mlTestData/multiClassData/' + fileNamePNG
        pathTXT = './../../../mlTestData/multiClassData/' + fileNameTXT
        print("process " + str(procNum) + " saving " + pathPNG)
        canvas.save(pathPNG)
        np.savetxt(pathTXT, annotation, fmt='%u %f %f %f %f')

    print(counter)

processes = []
interval = dataSetSize/numThreads
for i in range(0,numThreads):
    process = multiprocessing.Process(target=generateData, args=(int(i*interval), int((i*interval)+interval), i))
    processes.append(process)
    process.start()

for process in processes:
    process.join()




