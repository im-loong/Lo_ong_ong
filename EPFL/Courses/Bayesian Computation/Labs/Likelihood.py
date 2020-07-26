# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 11:25:09 2020

@author: Loong
"""

#%%
import numpy as np
import matplotlib.pyplot as plt

#%%

def likelihood_function (x):
    '''Compute the likelihood function for tossing coins
    '''
    lld=[]
    p = np.linspace(0,1,100)
    for i in p:
        y = [(1-i)+(2*i-1)*e for e in x]
        lld.append(np.prod(y))
    N=np.sum(lld*p)
    plt.plot(p,np.log(lld))
#%%
def sample_gen(n):
    '''Generate a senario of tossing n coins
    '''
    x=np.random.rand(n)
    sample=[(e<0.5)*1 for e in x]
    return sample
    
#%%
x=sample_gen(100)
likelihood_function(x)

#%%
sample_gen(10)