"""Uses Numpy to serialize HASYv2 data for 
   faster loading
"""
import os
import pandas
import numpy as np
import random 
from PIL import Image

numClasses = 10
numberXSize = 32
numberYSize = 32
dataDir = 'hasyDataPath'
hasyData = []
hasyLabels = []
labels = pandas.read_csv('csvPath')

for filename in os.listdir(dataDir):
    if filename.endswith(".png"):
        newPath = os.path.join(dataDir, filename)
        labelIndex = newPath.replace('pathForEachFileExceptNumber', "")
        labelIndex = labelIndex.replace('.png', "")
        index = int(labelIndex)
        
        img = Image.open(newPath).convert('L')
        img = np.array(img)
        img = img.reshape(numberXSize, numberYSize, 1)
        hasyData.append(img)
        
        label = labels.iloc[index]['latex']
        label = label.replace('\\', "")
        hasyLabels.append(label)

        print('Path: ' + newPath)
        print('label: ' + label)

hasyData = np.array(hasyData)
hasyLabels = np.array(hasyLabels)

np.save('hasyData.npy', hasyData)
np.save('hasyLabels.npy', hasyLabels)
