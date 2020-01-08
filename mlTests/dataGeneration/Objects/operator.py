import numpy as np
import random
x_operators = np.load('./../../../mlTestData/symbols/x_operators.npy')
y_operators= np.load('./../../../mlTestData/symbols/y_operators.npy')

class Operator:
    def __init__(self):
        imageIndex = random.randint(0, len(x_operators)-1)
        self.array = x_operators[imageIndex]
        self.label = y_operators[imageIndex]
        self.length = x_operators[0].shape[1]
        self.height = x_operators[0].shape[0]

    def createYoloLabel(self, startingLocationX, startingLocationY, canvasXSize, canvasYSize):      
        annotation = []
        annotation.append(int(self.label))
        annotation.append((startingLocationX+(self.length/2))/canvasXSize)
        annotation.append((startingLocationY+(self.height/2))/canvasYSize)
        annotation.append(self.length/canvasXSize)
        annotation.append(self.height/canvasYSize)
        return annotation