# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:49:41 2020

@author: Loong
"""
#%%
import math
import numpy as np
import matplotlib.pyplot as plt

#%%
#defining exponential draw function
def draw_exp(l, shape=(1,)):
    """
        Draws from a distribution with pdf l*e^(-l*x).
    """
    return -np.log(np.random.rand(*shape)) / l
    
#%%
#plotting the draw
lam=2
D=300
exp_draw = expo_rand_gen(lam,D)
plt.hist(exp_draw,bins=30,density=True)
#plotting the theratical distribution
x=np.arange(0,4,0.001)
y=lam*np.e**(-lam*np.arange(0,4,0.001))
plt.plot(x,y)
plt.show()

#%%
#Homogeneous Poisson Process

def homo_poisson_process (T,lam,D):
    t=0
    X=[]
    while True:
        t = t + float(expo_rand_gen(lam)[1,])
        if t>T:
            break
        X.append(t)
        print(X)

    return X
#%%
T=4
lam=2
D=100

homo_process = homo_poisson_process(T,lam,D)
plt.hist(homo_poisson_process)
plt.show()

#%%
homo_poisson_process(T,lam,D)
