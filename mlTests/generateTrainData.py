"""Generate training data from smaller 
   images for object detection.
"""
import numpy as np
import random 
from PIL import Image

numberXSize = 28
numberYSize = 28
canvasXSize = 300
canvasYSize = 300
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

for pictureNum in range(1000):
    annotations = []
    canvas = np.zeros([canvasXSize,canvasYSize,3],dtype=np.uint8)
    canvas.fill(255) 

    for k in range(5):
        x, y = generateRandomCoordinate()
        imageIndex = random.randint(0, len(x_train))
        addition = x_train[imageIndex]

        annotation = []
        annotation.append(y_train[imageIndex])
        annotation.append((x+14)/canvasXSize)
        annotation.append((y+14)/canvasYSize)
        annotation.append(numberXSize/canvasXSize)
        annotation.append(numberYSize/canvasYSize)

        for i in range(numberXSize):
            for j in range(numberYSize):
                canvas[x+i][y+j] = addition[i][j]

        annotations.append(annotation)


    annotations = np.array(annotations)
    canvas = Image.fromarray(canvas)
    fileNamePNG = 'objDetect' + str(pictureNum) + '.png'
    fileNameTXT = 'objDetect' + str(pictureNum) + '.txt'
    pathPNG = '/home/aroon/Desktop/YOLOTrainingData/' + fileNamePNG
    pathTXT = '/home/aroon/Desktop/YOLOTrainingData/' + fileNameTXT
    print(pathPNG)
    canvas.save(pathPNG)
    np.savetxt(pathTXT, annotations, fmt='%f')
    

