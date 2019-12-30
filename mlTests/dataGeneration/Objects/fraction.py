import numpy as np
import random
from Objects.character import Character
from PIL import Image 
class Fraction: 
    FRACTION_ID = 40

    def __init__(self):
        self.char1 = Character()
        self.char2 = Character()
        self.middleZone = 10
        self.array = np.zeros([(2*self.char1.height)+self.middleZone,self.char1.length,3],dtype=np.uint8)
        self.array.fill(255)
        print(self.array.shape)
        self.length = self.char1.length
        self.height = self.char1.height + self.middleZone + self.char2.height
        self.addNumeratorAndDenominator()
        self.addMidLine()

    def addNumeratorAndDenominator(self):
        for i in range(self.char1.height):
            for j in range(self.char1.length):
                self.array[j][i] = self.char1.array[j][i]
                self.array[self.char1.height+self.middleZone+j][i] = self.char2.array[j][i]

    def addMidLine(self):
        midZoneBeginY = self.char1.height
        thickness = random.randint(1, 3)
        direction = random.randint(-1, 1)
        for i in range(self.char1.length):
            direction += random.randint(-1, 1)
            yLoc = int(midZoneBeginY + (self.middleZone/2) + direction)
            for j in range(thickness):
                self.array[yLoc-j][i] = [0,0,0]
                self.array[yLoc+j][i] = [0,0,0]
    
    def createYoloLabel(self, topLeftX, topLeftY, canvasXSize, canvasYSize):
        annotations = []
        
        annotation = []
        annotation.append(self.FRACTION_ID)
        annotation.append((topLeftX+(self.length/2))/canvasXSize)
        annotation.append((topLeftY+(self.height/2))/canvasYSize)
        annotation.append(self.length/canvasXSize)
        annotation.append(self.height/canvasYSize)

        annotations.append(annotation)
        annotations.append(self.char1.createYoloLabel(topLeftX, topLeftY, canvasXSize, canvasYSize))

        char2Y = topLeftY + self.char1.height + self.middleZone
        annotations.append(self.char2.createYoloLabel(topLeftX, char2Y, canvasXSize, canvasYSize))

        return annotations


        

