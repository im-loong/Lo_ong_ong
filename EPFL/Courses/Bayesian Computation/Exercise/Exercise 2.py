# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:36:30 2020

@author: Loong
"""
#%%

import numpy as np

#%%

X= 10*np.random.rand(3,3)
theta = 5*np.random.rand(3,1)
sigma = float(input('sigma'))
Y = np.matmul(X,theta) + np.random.uniform(0,1)*sigma



