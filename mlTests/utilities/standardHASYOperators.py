"""Puts basic algebraic operators from HASY into their own numpy array"""
import numpy as np
x_hasy = np.load('./../../../mlTestData/symbols/hasyData.npy')
y_hasy = np.load('./../../../mlTestData/symbols/hasyLabels.npy')

x_standard_operators = []
y_standard_operators = []

for i in range(0,len(x_hasy)):
    label = str(y_hasy[i])
    if label is "+":
        x_standard_operators.append(x_hasy[i])
        y_standard_operators.append(36)
    elif label is "-":
        x_standard_operators.append(x_hasy[i])
        y_standard_operators.append(37)
    elif label is "times":
        x_standard_operators.append(x_hasy[i])
        y_standard_operators.append(38)
    elif label is "cdot":
        x_standard_operators.append(x_hasy[i])
        y_standard_operators.append(38)
    elif label is "/":
        x_standard_operators.append(x_hasy[i])
        y_standard_operators.append(39)

x_standard_operators = np.array(x_standard_operators)
y_standard_operators = np.array(y_standard_operators)

np.save('./../../../mlTestData/symbols/x_operators.npy', x_standard_operators)
np.save('./../../../mlTestData/symbols/y_operators.npy', y_standard_operators)