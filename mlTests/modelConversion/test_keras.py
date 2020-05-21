# load and evaluate a saved model
from numpy import loadtxt
from keras.models import load_model
from PIL import Image
import numpy as np
 
# load model
model = load_model('./../../../backupWeights/math_weights.h5')
# summarize model.
model.summary()
# load dataset
#dataset = loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split into input (X) and output (Y) variables
#X = dataset[:,0:8]
#Y = dataset[:,8]

image = Image.open('/home/aroon/CS/MA+H/mlTestData/multiClassData/objDetect66859.png')
img = np.array(image)
print(img.shape)
model.evaluate(img)

#score = model.evaluate(X, Y, verbose=0)
#print("%s: %.2f%%" % (model.metrics_names[1], score[1]*100))