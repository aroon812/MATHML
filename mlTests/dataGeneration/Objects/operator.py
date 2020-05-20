import numpy as np
import random
x_operators = np.load('./../../../mlTestData/symbols/hasyData.npy')
y_operators= np.load('./../../../mlTestData/symbols/hasyLabels.npy')

x_standard_operators = []
y_standard_operators = []

for i in range(0,len(x_operators)):
    label = str(y_operators[i])
    if label is "+":
        x_standard_operators.append(x_operators[i])
        y_standard_operators.append(36)
    elif label is "-":
        x_standard_operators.append(x_operators[i])
        y_standard_operators.append(37)
    elif label is "times":
        x_standard_operators.append(x_operators[i])
        y_standard_operators.append(38)
    elif label is "cdot":
        x_standard_operators.append(x_operators[i])
        y_standard_operators.append(38)
    elif label is "/":
        x_standard_operators.append(x_operators[i])
        y_standard_operators.append(39)


class Operator:
    def __init__(self):
        imageIndex = random.randint(0, len(x_standard_operators)-1)
        self.array = x_standard_operators[imageIndex]
        self.label = y_standard_operators[imageIndex]
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