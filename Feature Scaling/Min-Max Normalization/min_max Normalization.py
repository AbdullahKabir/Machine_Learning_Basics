#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
def calculate_min_max_normalization(data,test):
    minVal = min(data)
    print("Min Value:",minVal)
    maxVal = max(data)
    print("max Value:",maxVal)
    normalizedValues = []
    normalizedValuesTest = []
    for i in data:
        val = (i-minVal)/(maxVal-minVal)
        print("Raw Data:",i,"Normalized Data:",val)
        normalizedValues.append(val)
    for k in test:
        valTest = (k-minVal)/(maxVal-minVal)
        print("Raw Data Test:",k,"Normalized Data:",valTest)
        normalizedValuesTest.append(valTest)
    return normalizedValues,normalizedValuesTest
def main():
    df=pd.read_csv("A:\\Python Files\\Scaling\\Raw data.csv")
    train = df.values
    df2=pd.read_csv("A:\\Python Files\\Scaling\\testData.csv")
    test = df2.values
    values = calculate_min_max_normalization(train,test)
    #print("Train data -> ",values[0],"\nTest data -> ",values[1])
main()


# In[ ]:





# In[ ]:




