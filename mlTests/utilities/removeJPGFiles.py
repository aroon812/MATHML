import os
data_dir = '/home/aroon/Desktop/YOLOTrainingData'

for filename in os.listdir(data_dir):
    if filename.endswith(".jpg"):
        path = os.path.join(data_dir, filename)
        print("removing " + path)
        os.remove(path)
       