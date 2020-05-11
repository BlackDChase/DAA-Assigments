from math import sqrt
import dataGen
from hmm import HMM
import numpy as np
import matplotlib.pyplot as plt
import timeit
from tqdm import tqdm 
from mpl_toolkits.mplot3d import Axes3D


x=[] 
y=[] 
z=[] 
nO=5 
nHS=5
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for n in tqdm(range(10,100,10)): 
    for itteration in range(int(n/2),2*n): 
        '''
        emission = np.array([[0.1,0.6],[0.4,0.25],[0.5,0.15]]) 
        transmission = np.array([[0,0,0,0],[0.5,0.7,0.1,0],[0.5,0.25,0.85,0],[0,0.05,0.05,0]]) 
        observation = ['2','3','3','2','3','2','3','2','2','3','1','3','3','1','1','1','2','1','1
','1','3','1','2','1','1','1','2','3','3','2','3','2','2'] 
'''
        emission=np.array(np.transpose(dataGen.emisionMat(nHS,nO)))
        transmission=np.array(dataGen.transmissionMat(nHS))
        observation=dataGen.observationMat(nO,n)
        start=timeit.default_timer() 
        model = HMM(transmission,emission) 
        model.train(observation,itteration) 
        end=timeit.default_timer() 
        x.append(n) 
        y.append(itteration) 
        z.append(end-start)
ax.scatter(x,y,z)
ax.set_xlabel('number of observation')
ax.set_ylabel('number of itteration')
ax.set_zlabel('time')

plt.show()
        '''
        x=[]
    ...: y=[]
    ...: z=[]
    ...: nO=100
    ...: nHS=100
    ...: for n in range(nO+nHS,nO*nHS,int(sqrt((nO+nHS)*nO*nHS))):
    ...:     for itteration in range(n/2,2*n):
    ...:         emission=np.array(np.transpose(dataGen.emisionMat(nHS,nO)))
    ...:         transmission=np.array(dataGen.transmissionMat(nHS))
    ...:         observation=dataGen.observationMat(nO,n)
    ...:         t=timeC(emission,transmission,observation,itteration)
    ...:         x.append(n)
    ...:         y.append(itteration)
    ...:         z.append(t)
    '''
