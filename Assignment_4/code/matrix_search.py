from tqdm import tqdm
import matplotlib.pyplot as plt
import os
import timeit
import sys
from random import randint

def plotit(scale,data):
    new = []
    for val in range(len(scale)):
        new.append([scale[val],data[val]])
    new.sort()
    scale=[]
    data=[]
    for val in new:
        scale.append(val[0])
        data.append(val[1])
        
    plt.plot(scale,data)
    plt.xlabel("m*n")
    plt.ylabel("Time")
    plt.show()

def get_data():
    data = []
    with open('../../../Data.txt','r') as f:
        for line in f:
            unit=''
            for i in line:
                if i != ' ' or i != '\n':
                    unit=unit+i
                if i==' ':
                    data.append(unit)
                    unit=''
            if len(data)>=10**6: #n_sq
                break
    '''
    data = [1,234,124,135,236,2345]
    '''
    return data

def scale_data(raw,m,n):
    data = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(raw[i*m+j]))
        data.append(row)
    return data

'''
def mat_merge(mat,mid):
    i1,j1,i2,j2 = 0,0,mid,0
    while i1<mid,i2<len(mat):
        new[]
        if mat[i1][j1]>mat[i2][j2]:
            new.append(mat[i2][j2])
            i2=i2+1
        else:
            new.app
        if j1==len(mat[0]):
            j1=0
            i1=i1+1
        if j2==len(mat[0]):
            j2=0
            i1=i1+1
'''
def mat_sort(mat):
    full=[]
    for rows in mat:
        full=full+rows
    full.sort()
    k=0
    for rows in mat:
        for cols in rows:
            cols = full[k]
            k=k+1
    #print(type(mat),type(mat[0]))
    return mat

def mat_search(mat,x):
    j=len(mat[0])-1
    i=0
    while 0<=j<len(mat[0]) and 0<=i<len(mat):
        if mat[i][j]==x:
            return
        elif x<mat[i][j]:
            j=j-1
        else:
            i=i+1
        if i==len(mat):
            i=i-1
            j=j+1
        if j==-1:
            j=len(mat[0])-1
            i=i-1
    return

if __name__ == '__main__':
    
    time = []
    x=[]
    data = get_data()
    for j in tqdm(range(1,1000,10)):
        for k in range(1,1000,10):
            matrix = scale_data(data,j,k)
            
            start = timeit.default_timer()
            matrix = mat_sort(matrix)
            f = randint(1,10**5)
            mat_search(matrix,f)
            end = timeit.default_timer()
            x.append(j*k)
            time.append(end-start)
    plotit(x,time)

