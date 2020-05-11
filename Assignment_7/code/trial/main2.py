from math import sqrt
import dataGen
from hmm import HMM
import numpy as np
import matplotlib.pyplot as plt
import timeit
from tqdm import tqdm 
from mpl_toolkits.mplot3d import Axes3D

def run(nO,nHS):
    n=20
    #itteration=10
    emission=np.array(np.transpose(dataGen.emisionMat(nHS,nO))) 
    transmission=np.array(dataGen.transmissionMat(nHS)) 
    observation=dataGen.observationMat(nO,n)
    start=timeit.default_timer()
    model = HMM(transmission,emission)
    model.train(observation)
    end=timeit.default_timer()
    return end-start

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
a=[]
b=[]
c=[]
for nO in range(5,10):
    for nHS in range(5,10):
        
        a.append(nO)
        b.append(nHS)
        c.append(end-start)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(a,b,c)
ax.set_xlabel('number of Observable states')
ax.set_ylabel('number of Hidden States')
ax.set_zlabel('time')
plt.show()
#################################################################################

