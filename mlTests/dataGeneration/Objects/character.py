import numpy as np
import random
x_train = np.load('./../../../mlTestData/numbers/xData.npy')
y_train = np.load('./../../../mlTestData/numbers/yData.npy')

class Character:
    def __init__(self):
        imageIndex = random.randint(0, len(x_train)-1)
        self.array = x_train[imageIndex]
        self.label = y_train[imageIndex]
        self.length = x_train[0].shape[1]
        self.height = x_train[0].shape[0]

    def createYoloLabel(self, startingLocationX, startingLocationY, canvasXSize, canvasYSize):
        asciiLabel = ord(str(self.label))
        if asciiLabel > 57:
            self.label = asciiLabel - 55
            
        annotation = []
        annotation.append(int(self.label))
        annotation.append((startingLocationX+(self.length/2))/canvasXSize)
        annotation.append((startingLocationY+(self.height/2))/canvasYSize)
        annotation.append(self.length/canvasXSize)
        annotation.append(self.height/canvasYSize)
        return annotation



