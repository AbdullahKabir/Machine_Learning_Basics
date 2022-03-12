#!/usr/bin/env python
# coding: utf-8

# In[40]:


from cmath import sqrt
import pandas as pd
def calculate_SD(data):
    sumArr = []
    N=len(data)
    mean = sum(data)/N
    for i in data:
        temp = (i - mean)
        tempSq = temp*temp
        sumArr.append(tempSq)
        tempsum = sum(sumArr)
    sd = sqrt(tempsum/N)
    return sd,mean,N

def calculate_Z_Score(data,test):
    sd,mean,N = calculate_SD(data)
    print ("Standard Daviasion:",sd,"\n Mean: ",mean)
    standardizedValues = []
    standardizedValuesOnTest = []
    for i in data:
        z = (i - mean) / sd
        print(i,z)
        standardizedValues.append(z)
    for k in test:
        z = (k - mean) / sd
        print(k,z)
        standardizedValuesOnTest.append(z)
    return standardizedValues,standardizedValuesOnTest
def main():
    train= []
    test = []
    t = pd.read_csv("A:\\Python Files\\Scaling\\Raw data.csv")
    train= t.values
    t2 = pd.read_csv("A:\\Python Files\\Scaling\\testData.csv")
    test = t2.values
    calculate_Z_Score(train,test)
main()


# In[ ]:





# In[ ]:




