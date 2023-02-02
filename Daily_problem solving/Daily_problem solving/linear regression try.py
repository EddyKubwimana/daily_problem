# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 20:23:52 2021

@author: Kubwi
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
x=[1,2,3,4,5,6,7,8,9,10]
y=[2,3,4,5,6,7,8,9,10,11]
df=pd.DataFrame({'x':np.array(x),
                 'y':np.array(y),
                 'x^2':np.array(x)**2,
                 'y^2':np.array(y)**2,
                 'xy':np.array(x)*np.array(y)})
sumx=df.sum(axis=0)[0]
sumy=df.sum(axis=0)[1]
sumx2=df.sum(axis=0)[2]
sumy2=df.sum(axis=0)[3]
sumxy=df.sum(axis=0)[4]
#slope
m=(len(x)*sumxy-(sumx*sumy))/(len(x)*sumx2-sumx**2)
print(m)

