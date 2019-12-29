"""Simple utility script for flipping
   the colors of images
"""
import os
from PIL import Image
import PIL.ImageOps

#directories for inverting image color
directories = []
classes = 10

for directory in directories:
    for i in range(classes):
        newDirectory = os.path.join(directory, str(i))
        newDirectoryTemp = newDirectory
        for filename in os.listdir(newDirectory):
            if filename.endswith(".png"):
                newDirectory = os.path.join(newDirectoryTemp, filename)
                print(newDirectory)
                image = Image.open(newDirectory)
                PIL.ImageOps.invert(image).convert('RGB').save(newDirectory, "PNG", optimize=True)