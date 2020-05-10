from tqdm import tqdm
import matplotlib.pyplot as plt
#import os
import timeit
#import sys
#import threading
import multiprocessing
from copy import deepcopy
import pandas as pd
from glob import glob
#import gc

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

def para(data):
    timePara = []
    xPara = []
    for j in tqdm(range(10,len(data),len(data)//200)):
        xD=deepcopy(data[:j])
        yD=deepcopy(data[:j])
        #gc.collect()
                
        #function
        start = timeit.default_timer()
        y = multiprocessing.Process(target=horizontal_allgined, args=(yD,))
        x = multiprocessing.Process(target=vertical_allgined, args=(xD,))
        x.start()
        y.start()
        x.join()
        y.join()
        end = timeit.default_timer()
        xPara.append(j)
        timePara.append(end-start)
    
    conver2CSV(xPara,timePara,"Parallel")
    timePara = []
    xPara = []
    xD=[]
    yD=[]
    #gc.collect()
    return 

def seq(data):
    timeSeq = []
    xSeq = []
    for j in tqdm(range(10,len(data),len(data)//200)):
        xD=deepcopy(data[:j])
        yD=deepcopy(data[:j])
        #gc.collect()

        start = timeit.default_timer()
        
        #function
        horizontal_allgined(yD)
        vertical_allgined(xD)
        end = timeit.default_timer()
        
        xSeq.append(j)
        timeSeq.append(end-start)
    conver2CSV(xSeq,timeSeq,"Sequential")
    timeSeq = []
    xSeq = []
    xD={}
    yD={}
    #gc.collect()
    return 

def horizontal(data):
    timeHorizontal = []
    xHorizontal = []
    for j in tqdm(range(10,len(data),len(data)//200)):
        yD=deepcopy(data[:j])
        yDict={}
        #gc.collect()      
                
        #function
        start = timeit.default_timer()
        horizontal_allgined(yD)
        end = timeit.default_timer()

        xHorizontal.append(j)
        timeHorizontal.append(end-start)
    conver2CSV(xHorizontal,timeHorizontal,"Horizontal")
    timeHorizontal = []
    xHorizontal = []
    yD={}
    yDict={}
    #gc.collect()        
    return

def vertical(data):
    timeHorizontal = []
    xHorizontal = []
    for j in tqdm(range(10,len(data),len(data)//200)):
        yD=deepcopy(data[:j])
        yDict={}
        #gc.collect()      
                
        #function
        start = timeit.default_timer()
        vertical_allgined(yD)
        end = timeit.default_timer()

        xHorizontal.append(j)
        timeHorizontal.append(end-start)
    conver2CSV(xHorizontal,timeHorizontal,"Vertical")
    timeHorizontal = []
    xHorizontal = []
    yD={}
    yDict={}
    #gc.collect()        
    return 

def get_Time():
    for fileName in glob("*.csv"):
        data=pd.read_csv(fileName)
        tab=[]
        for i in data:
            v=[]
            for j in data[i]:
                v.append(j)
            tab.append(v)
        plt.plot(tab[0],tab[1],label=fileName[:-4])

if __name__ == '__main__':
    #gc.collect()
    data = get_data()
    
    s=multiprocessing.Process(target=seq, args=(data,))
    p=multiprocessing.Process(target=para, args=(data,)) 
    h=multiprocessing.Process(target=horizontal, args=(data,)) 
    v=multiprocessing.Process(target=vertical, args=(data,)) 
    
    s.start()
    h.start()
    v.start()
    h.join()
    v.join()
    s.join()
    '''
    tab=[]
    for fileName in glob("H*.csv"):
        data=pd.read_csv(fileName)
        for i in data:
            v=[]
            for j in data[i]:
                v.append(j)
            tab.append(v)
    k=0
    
    for fileName in glob("V*.csv"):
        data=pd.read_csv(fileName)
        for j in data[data.keys()[1]]:
            try:
                tab[1][k]+=j
                k+=1
            except:
                break
            
    plt.plot(tab[0],tab[1],label="Parallel")
    
    para(data)
    seq(data)
    horizontal(data)
    vertical(data)
    '''
    get_Time()
    plt.xlabel("Numbers of Points in the plane")
    plt.ylabel("Time")
    plt.legend()
    plt.savefig(str(len(data))+"_Sequential.jpeg")
