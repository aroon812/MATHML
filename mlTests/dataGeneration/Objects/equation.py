import numpy as np
import random
from functools import reduce
from Objects.character import Character
from Objects.operator import Operator
from Objects.fraction import Fraction

class Equation:
    EQUATION_ID = 41

    def __init__(self):
        self.length = 0
        self.maxCharNum = 5
        self.equationLength = random.randint(1, int(self.maxCharNum+1))
        self.objects = []
        self.objectsStart = []
        self.label = self.EQUATION_ID
        self.generateStructure()
        self.height = self.getHeight()
        self.createArray()

    def generateStructure(self):
        currObjectStart = 0
        lastWasNumber = False
        lastWasFraction = False
        lastWasOperator = False

        lastValue = random.choice([Character(), Fraction()])
        for k in range(self.equationLength):
            self.length += lastValue.length
            self.objects.append(lastValue)
            self.objectsStart.append(currObjectStart)
            currObjectStart += lastValue.length

            if isinstance(lastValue, Character):
                lastValue = random.choice([Character(), Operator()])
            elif isinstance(lastValue, Fraction):
                lastValue = Operator()
            elif isinstance(lastValue, Operator):
                lastValue = random.choice([Character(), Fraction()])         

    def createArray(self):
        self.array = np.zeros([self.height,self.length,3],dtype=np.uint8)
        self.array.fill(255)

        for i in range(len(self.objects)):
            for j in range(self.objects[i].length):
                for k in range(self.objects[i].height):
                    self.array[k][self.objectsStart[i]+j] = self.objects[i].array[k][j]

    def createYoloLabel(self, topLeftX, topLeftY, canvasXSize, canvasYSize):
        annotations = []
        
        annotation = []
        annotation.append(self.EQUATION_ID)
        annotation.append((topLeftX+(self.length/2))/canvasXSize)
        annotation.append((topLeftY+(self.height/2))/canvasYSize)
        annotation.append(self.length/canvasXSize)
        annotation.append(self.height/canvasYSize)
        annotations.append(annotation)

        for i in range(len(self.objects)):
            label = self.objects[i].createYoloLabel(topLeftX+self.objectsStart[i], topLeftY, canvasXSize, canvasYSize)
            if type(label[0]) is type([]):
                for annotation in label:
                    annotations.append(annotation)
            else:
                annotations.append(label)
       
        return annotations

    def getHeight(self):
        height = 0 
        for obj in self.objects:
            if obj.height > height:
                height = obj.height
        return height
