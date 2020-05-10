from tqdm import tqdm
import matplotlib.pyplot as plt
import os
import timeit
import time
#import sys
#import threading
import multiprocessing
from copy import deepcopy
import pandas as pd
from glob import glob
import gc

def get_data():
    data = []
    with open('../../../Data_small.txt','r') as f:
        for line in f:
            point=[]
            unit=''
            for i in line:
                if i != ' ' and i != '\n':
                    unit=unit+i
                else:
                    point.append(int(unit))
                    unit=''                    
            data.append(point)
            if len(data)>=10**7: 
                break
    '''
    data = [[1,234],[124,135],[236,2345]]
    '''
    #print(data)
    return data



def horizontal_allgined(plane):
    line={}
    while len(plane)>0:
         pointA=plane.pop()
         if pointA[1] in line.keys():
             line[pointA[1]].append(pointA[0])
         else:
             line[pointA[1]]=[pointA[0]]


def vertical_allgined(plane):
    line={}
    while len(plane)>0:
         pointA=plane.pop()
         if pointA[0] in line.keys():
             line[pointA[0]].append(pointA[1])
         else:
             line[pointA[0]]=[pointA[1]]
    
def conver2CSV(x,y,name):
    x=pd.DataFrame(x)
    y=pd.DataFrame(y)
    x.to_csv(name+".csv")
    y.to_csv(name+".csv")
     
def get_Time():
    x=pd.read_csv("x.csv")
    y=pd.read_csv("y.csv")
    tab=[]
    k=[i for i in x.keys()]
    time=[]
    n=[]
    for i in range(len(x[k[1]])):
        n.append(x[k[0]][i])
        time.append(max(x[k[1]][i],y[k[1]][i]))
    conver2CSV(n,time,"Parallel")
    os.remove('x.csv')
    os.remove('y.csv')
    get_TimeF()
    
def get_TimeF():
    for fileName in glob("*.csv"):
        data=pd.read_csv(fileName)
        tab=[]
        for i in data:
            v=[]
            for j in data[i]:
                v.append(j)
            tab.append(v)
        plt.plot(tab[0],tab[1],label=fileName[:-4])


def core(data,label):
    timePara = []
    xPara = []
    totalT=timeit.default_timer()
    for j in tqdm(range(10,len(data),len(data)//200)):
        #time.sleep(0.5)
        xD=deepcopy(data[:j])
        start = timeit.default_timer()
        if label=='x':
            horizontal_allgined(xD)
        else:
            vertical_allgined(xD)
        #function
        end = timeit.default_timer()
        xPara.append(j)
        timePara.append(end-start)
    totalT=timeit.default_timer() - totalT
    #print(totalT,label)
    conver2CSV(xPara,timePara,label)

    return

if __name__ == '__main__':
    data = get_data()
    
    totalT2 = timeit.default_timer()

    #function
    y = multiprocessing.Process(target=core, args=(deepcopy(data),'x',))
    x = multiprocessing.Process(target=core, args=(deepcopy(data),'y',))
    x.start()
    y.start()
    x.join()
    y.join()
    totalT2 = timeit.default_timer() - totalT2
    
    get_Time()
    plt.xlabel("Numbers of Points in the plane")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig(str(len(data))+"_ParalleProcess_VS_Sequential.jpeg")
    plt.close()

    timePara = []
    xPara = []
    totalT=timeit.default_timer()
    
    for j in tqdm(range(10,len(data),len(data)//200)):
        gc.collect()
        #time.sleep(0.5)
        xD=deepcopy(data[:j])
        yD=deepcopy(data[:j])
        start = timeit.default_timer()

        #function
        y = multiprocessing.Process(target=horizontal_allgined, args=(yD,))
        x = multiprocessing.Process(target=vertical_allgined, args=(xD,))
        x.start()
        y.start()
        x.join()
        y.join()
        end = timeit.default_timer()
        xPara.append(j)
        timePara.append(end-start)
    totalT=timeit.default_timer() - totalT
    #print(totalT,totalT2)
    conver2CSV(xPara,timePara,"ParallelCS")
    get_TimeF()
    plt.xlabel("Numbers of Points in the plane")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig(str(len(data))+"_ParalleProcessCS.jpeg")
    
    print("Context Switch based parallel algo :",totalT)
    print("Optimized Parallel algo            :",totalT2)
    #DONE
