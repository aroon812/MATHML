"""Generate training data from smaller 
   images for object detection.
"""
import numpy as np
import random 
import os
import multiprocessing 
from PIL import Image

numThreads = 12
dataSetSize = 90000
numberXSize = 28
numberYSize = 28
operatorXSize = 32
operatorYSize = 32
canvasXSize = 416
canvasYSize = 416
maxCharNum = (canvasXSize/operatorXSize)-1

x_train = np.load('/home/aroon/Desktop/NumpyArrays/xData.npy')
y_train = np.load('/home/aroon/Desktop/NumpyArrays/yData.npy')
x_hasy = np.load('/home/aroon/Desktop/NumpyArrays/hasyData.npy')
y_hasy = np.load('/home/aroon/Desktop/NumpyArrays/hasyLabels.npy')

x_standard_operators = []
y_standard_operators = []

for i in range(0,len(x_hasy)):
    label = str(y_hasy[i])
    if label is "+":
        x_standard_operators.append(x_hasy[i])
        y_standard_operators.append(36)
    elif label is "-":
        x_standard_operators.append(x_hasy[i])
        y_standard_operators.append(37)
    elif label is "times":
        x_standard_operators.append(x_hasy[i])
        y_standard_operators.append(38)
    elif label is "cdot":
        x_standard_operators.append(x_hasy[i])
        y_standard_operators.append(38)
    elif label is "/":
        x_standard_operators.append(x_hasy[i])
        y_standard_operators.append(39)

def generateRandomCoordinate(equationLength):
    """Generate a random starting coordinate 
    based on the length of the equation.
    """
    x = random.randint(0, canvasXSize-(operatorXSize*equationLength))
    y = random.randint(0, canvasYSize-operatorYSize)
    return (x, y)

def generateData(startPoint, endPoint, procNum):
    """Generate pictures of random equations.
    startpoint and endpoint should be dependent on which thread
    is running the function.
    """

    for pictureNum in range(startPoint, endPoint):
        annotations = []
        canvas = np.zeros([canvasXSize,canvasYSize,3],dtype=np.uint8)
        canvas.fill(255) 
        
        equationLength = random.randint(1, int(maxCharNum+1))
        x, y = generateRandomCoordinate(equationLength)
        lastWasNumber = False

        for k in range(equationLength):
            if lastWasNumber is False:
                imageIndex = random.randint(0, len(x_train)-1)
                addition = x_train[imageIndex]
                lastWasNumber = True
            else:
                lastWasNumber = random.choice([True, False])
                if lastWasNumber is True:
                    imageIndex = random.randint(0, len(x_train)-1)
                    addition = x_train[imageIndex]
                else:
                    imageIndex = random.randint(0, len(x_standard_operators)-1)
                    addition = x_standard_operators[imageIndex]
            

            annotation = []

            if lastWasNumber is True:
                annotation.append(y_train[imageIndex].astype(int))
                annotation.append((x+(numberXSize/2))/canvasXSize)
                annotation.append((y+(numberYSize/2))/canvasYSize)
                annotation.append(numberXSize/canvasXSize)
                annotation.append(numberYSize/canvasYSize)

                for i in range(numberXSize):
                    for j in range(numberYSize):
                        canvas[y+j][x+i] = addition[j][i]

                x += numberXSize

            else:
                annotation.append(int(y_standard_operators[imageIndex]))
                annotation.append((x+(operatorXSize/2))/canvasXSize)
                annotation.append((y+(operatorYSize/2))/canvasYSize)
                annotation.append(operatorXSize/canvasXSize)
                annotation.append(operatorYSize/canvasYSize)

                for i in range(operatorXSize):
                    for j in range(operatorYSize):
                        canvas[y+j][x+i] = addition[j][i]

                x += operatorXSize

            annotations.append(annotation)

        annotations = np.array(annotations)
        canvas = Image.fromarray(canvas)
        fileNamePNG = 'objDetect' + str(pictureNum) + '.png'
        fileNameJPG = 'objDetect' + str(pictureNum) + '.jpg'
        fileNameTXT = 'objDetect' + str(pictureNum) + '.txt'
        pathPNG = '/home/aroon/Desktop/YOLOTrainingData/' + fileNamePNG
        pathJPG = '/home/aroon/Desktop/YOLOTrainingData/' + fileNameJPG
        pathTXT = '/home/aroon/Desktop/YOLOTrainingData/' + fileNameTXT
        print("process " + str(procNum) + " saving " + pathJPG)
        canvas.save(pathPNG)
        image = Image.open(pathPNG)
        rgbImage = image.convert('RGB')
        rgbImage.save(pathJPG)
        os.remove(pathPNG)
        np.savetxt(pathTXT, annotations, fmt='%u %f %f %f %f')

processes = []
interval = dataSetSize/numThreads
for i in range(0,numThreads):
    process = multiprocessing.Process(target=generateData, args=(int(i*interval), int((i*interval)+interval), i))
    processes.append(process)
    process.start()

for process in processes:
    print("joining process " + process)
    process.join()


