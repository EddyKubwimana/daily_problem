#Build prediction model using sklearn module
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:38:40 2021

@author: Kubwi
"""
import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import scipy.stats as st
x=[1,2,3,4,5,6,7,8,9,10,11]
y=[0.018,0.035,0.053,0.070,0.087,0.104,0.121,0.121,0.138,0.155,0.171]
data=pd.DataFrame({'x':x,
                   'y':y})
model=linear_model.LinearRegression()
model.fit(data[['x']],data['y'])

#print(model.coef_, model.intercept_)
x=True
while x is True:
     print('the number of hours some spent drinking')
     UserInput=int(input())
     a= model.predict([[UserInput]])
     print('the concentration of alchool in the blood is', a)
     
     print('do you want to continue predicting the alchool concentration in the driver blood')
     print('if yes tape y if no tape n')
     User=input()
     if User=='no'or  User=='N' or User=='No' or User=='nO':
         x=False
         
    
#slope,intercept,r,p,std_err=st.linregress(x,y)
#print(slope, intercept, r, std_err,p)
#def myfun(a):
   # return slope*a+intercept
#print('enter the number of our spent drinking, and check the alchool concentration in the blood')
#UserInput=int(input())
#print('the alchool concentration for{UserInput} is,', myfun(UserInput))
