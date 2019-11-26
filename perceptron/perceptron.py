# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np 

np.random.seed(50)

def stepFunction(t):
    if t>=0:
       return 1
    return 0

def prediction(X,W,b):
  return stepFunction((np.mathmul(X,W) +b)[0]) 
  
def preceptronStep(X, Y, W, b, learn_rate=0.01):
    
    return W,b

def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.array(np.random.rand(1)[0]) + x_max
    
    boundry_lines = []
    for i in range(num_epochs):
        
        W,b =perceptronStep(X, y, W, b, learn_rate)
        boundry_lines.append((-W[0]/W[1], -b/W[1]))
        return boundry_lines
        