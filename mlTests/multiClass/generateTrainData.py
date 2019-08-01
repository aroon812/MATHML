"""Generate training data from smaller 
   images for object detection.
"""
import numpy as np
import random 
import os
import multiprocessing 
from PIL import Image

numThreads = 12
dataSetSize = 30000
numberXSize = 28
numberYSize = 28
canvasXSize = 416
canvasYSize = 416
coordinates = []

x_train = np.load('/home/aroon/Desktop/NumpyArrays/xTrain.npy')
y_train = np.load('/home/aroon/Desktop/NumpyArrays/yTrain.npy')

def generateRandomCoordinate():
    x = random.randint(0, canvasXSize-numberXSize)
    y = random.randint(0, canvasYSize-numberYSize)
    while (x, y) in coordinates:
        x = random.randint(0, canvasXSize-numberXSize)
        y = random.randint(0, canvasYSize-numberYSize)
    coordinates.append((x,y))
    return (x, y)

def generateData(startPoint, endPoint):
    for pictureNum in range(startPoint, endPoint):
        annotations = []
        canvas = np.zeros([canvasXSize,canvasYSize,3],dtype=np.uint8)
        canvas.fill(255) 

        for k in range(5):
            x, y = generateRandomCoordinate()
            imageIndex = random.randint(0, len(x_train)-1)
            addition = x_train[imageIndex]

            annotation = []
            annotation.append(y_train[imageIndex].astype(int))
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
        pathPNG = '/home/aroon/Desktop/YOLOTrainingData/' + fileNamePNG
        pathJPG = '/home/aroon/Desktop/YOLOTrainingData/' + fileNameJPG
        pathTXT = '/home/aroon/Desktop/YOLOTrainingData/' + fileNameTXT
        print(pathJPG)
        canvas.save(pathPNG)
        image = Image.open(pathPNG)
        rgbImage = image.convert('RGB')
        rgbImage.save(pathJPG)
        os.remove(pathPNG)
        np.savetxt(pathTXT, annotations, fmt='%u %f %f %f %f')

processes = []
interval = dataSetSize/numThreads
for i in range(0,numThreads):
    print(i*interval)
    print(i*interval+interval)
    process = multiprocessing.Process(target=generateData, args=(int(i*interval), int((i*interval)+interval)))
    processes.append(process)
    process.start()

for process in processes:
    process.join()


