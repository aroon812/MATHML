"""Simple utility script for flipping
   the colors of images
"""
import os
from PIL import Image
import PIL.ImageOps

#hardcoded directories for changing the color. It's a simple utility file you don't need to be that abstract.
directories = ['/home/aroon/Desktop/EMNIST/digits/training', '/home/aroon/Desktop/EMNIST/digits/testing', '/home/aroon/Desktop/EMNIST/MNIST/training', '/home/aroon/Desktop/EMNIST/MNIST/testing']

for directory in directories:
    for i in range(10):
        newDirectory = os.path.join(directory, str(i))
        newDirectoryTemp = newDirectory
        for filename in os.listdir(newDirectory):
            if filename.endswith(".png"):
                newDirectory = os.path.join(newDirectoryTemp, filename)
                print(newDirectory)
                image = Image.open(newDirectory)
                PIL.ImageOps.invert(image).convert('RGB').save(newDirectory, "PNG", optimize=True)