from tqdm import tqdm
import matplotlib.pyplot as plt
import os
import timeit
import sys

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
    plt.xlabel("Array size [m*n]")
    plt.ylabel("Time")
    plt.show()

def kadane(arr, start, finish, n): 
    Sum = 0
    maxSum = -999999999999
    i = None
    finish[0] = -1
    local_start = 0
    for i in range(n): 
        Sum += arr[i]  
        if Sum < 0: 
            Sum = 0
            local_start = i + 1
        elif Sum > maxSum: 
            maxSum = Sum
            start[0] = local_start  
            finish[0] = i 

    if finish[0] != -1:  
        return maxSum  

    maxSum = arr[0]  
    start[0] = finish[0] = 0
    for i in range(1, n): 
        if arr[i] > maxSum: 
            maxSum = arr[i]  
            start[0] = finish[0] = i 
    return maxSum 
  
  
def findMaxSum(M): 
    ROW=len(M)
    COL=len(M[0])
    maxSum, finalLeft = -999999999999, None
    finalRight, finalTop, finalBottom = None, None, None
    left, right, i = None, None, None
    temp = [None] * ROW 
    Sum = 0
    start = [0] 
    finish = [0]  
    for left in range(COL): 
        temp = [0] * ROW  
        for right in range(left, COL):           
            for i in range(ROW): 
                temp[i] += M[i][right]  
  
            Sum = kadane(temp, start, finish, ROW)                
            if Sum > maxSum: 
                maxSum = Sum
                finalLeft = left  
                finalRight = right  
                finalTop = start[0]  
                finalBottom = finish[0] 
    #print("(Top, Left)", "(", finalTop,finalLeft, ")")  
    #print("(Bottom, Right)", "(", finalBottom,finalRight, ")")  
    #print("Max sum is:", maxSum) 

if __name__ == '__main__':
    time = []
    x=[]
    data = get_data()
    for j in tqdm(range(1,901,10)):
        for k in range(1,901,10):
            matrix = scale_data(data,j,k)
            
            start = timeit.default_timer()
            
            #function
            findMaxSum(matrix)

            end = timeit.default_timer()
            x.append(j*k)
            time.append(end-start)
    plotit(x,time)
