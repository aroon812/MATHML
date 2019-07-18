import glob, os
data_dir = '/home/aroon/Desktop/YOLOTrainingData/'

# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')  
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test) 
for filename in os.listdir(data_dir):
    if not filename.endswith(".txt"):
        if counter == index_test:
            counter = 1
            file_test.write(data_dir + filename + "\n")
        else:
            file_train.write(data_dir + filename + "\n")
            counter = counter + 1