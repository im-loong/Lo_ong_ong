# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 13:53:37 2020

@author: Loong
"""

#%%
import numpy as 


#%%
def delta_Q (Q,r,eta):
    deta_q = eta*(r-Q)
    return deta_q

#%%
Q=[[1.8,1.68]]

for i in range(0,2000):
    Q_new1 = Q[i][0] + delta_Q(Q[i][0],0.25,0.001)
    Q_new2 = Q[i][1] + delta_Q(Q[i][1],0.3,0.001)
    Q.append([Q_new1,Q_new2])
    if Q_new1<=Q_new2:
        print(i)
        break
print([Q_new1,Q_new2])


#%%





















