import numpy as np


def intitialisation(dimentions):
    parameters={}
    C=len (dimentions)
    for c in range(1,C):
        parameters['W'+str(c)]=np.random.randn(dimentions[c],dimentions[c-1])
        parameters["b"+str(c)]=np.random.randn(dimentions[c],1)

    return parameters

paramaters=intitialisation([2,12,12,1])
for key,val in paramaters.items():
    print(key,val.shape)

