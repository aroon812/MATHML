import glob, os
data_dir = './../../../mlTestData/fractionData/'

# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open('./../../../mlTestData/dataSplit/train.txt', 'w')  
file_test = open('./../../../mlTestData/dataSplit/test.txt', 'w')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test) 
for filename in os.listdir(data_dir):
    if not filename.endswith(".txt"):
        absPath = os.path.abspath(data_dir + filename)
        if counter == index_test:
            counter = 1
            file_test.write(absPath + "\n")
        else:
            file_train.write(absPath + "\n")
            counter = counter + 1
