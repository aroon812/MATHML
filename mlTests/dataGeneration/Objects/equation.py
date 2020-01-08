import numpy as np
import random
from Objects.character import Character
from Objects.operator import Operator

class Equation:
    EQUATION_ID = 41

    def __init__(self):
        self.length = 0
        self.maxCharNum = 5
        self.equationLength = random.randint(1, int(self.maxCharNum+1))
        self.objects = []
        self.objectsStart = []
        self.generateStructure()
        self.height = self.getHeight()
        self.createArray()

    def generateStructure(self):
        currObjectStart = 0
        lastWasNumber = False

        for k in range(self.equationLength):
            if lastWasNumber is False:
                newCharacter = Character()
                lastWasNumber = True
                self.length += newCharacter.length
                self.objects.append(newCharacter)
                self.objectsStart.append(currObjectStart)
                currObjectStart += newCharacter.length
            else:
                lastWasNumber = random.choice([True, False])
                if lastWasNumber is True:
                    newCharacter = Character()
                    self.length += newCharacter.length
                    self.objects.append(newCharacter)
                    self.objectsStart.append(currObjectStart)
                    currObjectStart += newCharacter.length
                else:
                    newOperator = Operator()
                    self.length += newOperator.length
                    self.objects.append(newOperator)
                    self.objectsStart.append(currObjectStart)
                    currObjectStart += newOperator.length
        
    def createArray(self):
        self.array = np.zeros([self.height,self.length,3],dtype=np.uint8)
        self.array.fill(255)

        for i in range(len(self.objects)):
            for j in range(self.objects[i].length):
                for k in range(self.objects[i].height-1):
                    #print(self.array.shape)
                    #print(self.objects[i].array.shape)
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
            annotations.append(self.objects[i].createYoloLabel(topLeftX+self.objectsStart[i], topLeftY, canvasXSize, canvasYSize))

        return annotations

    def getHeight(self):
        height = 0 
        for obj in self.objects:
            if obj.height > height:
                height = obj.height
        return height
