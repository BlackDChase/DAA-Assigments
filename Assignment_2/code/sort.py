from tqdm import tqdm
import matplotlib.pyplot as plt
import os
import timeit

def plotit(data):
    plt.plot(data)
    plt.ylabel("Time")
    plt.show()

def arrange(data):
    n=len(data)
    arranged=[]
    for i in range(0,n,3):
        arranged.append(data[i])
    for i in range(n-(n+1)%3 -1,0,-3):
        arranged.append(data[i])
    for i in range(2,n,3):
        arranged.append(data[i])
    print(arranged)
    return arranged
'''
#old arrange
def arrange(data):
    n=len(data)
    exede=0
    it=0
    arranged1=[]
    arranged2=[]
    arranged3=[]
    for i in range(0,n,3):
        arranged1.append(data[i])
    for i in range(1,n,3):
        arranged2.append(data[i])
    for i in range(2,n,3):
        arranged3.append(data[i])
    arranged = arranged1 + arranged2[::-1] + arranged3
    return arranged
'''
def insertionSort(arr, left, right):  
   
    for i in range(left + 1, right+1):  
       
        temp = arr[i]  
        j = i - 1 
        while arr[j] > temp and j >= left:  
           
            arr[j+1] = arr[j]  
            j -= 1
           
        arr[j+1] = temp  
    
def merge(arr, l, m, r): 
   
    len1, len2 =  m - l + 1, r - m  
    left, right = [], []  
    for i in range(0, len1):  
        left.append(arr[l + i])  
    for i in range(0, len2):  
        right.append(arr[m + 1 + i])  
   
    i, j, k = 0, 0, l 
    while i < len1 and j < len2:  
        if left[i] <= right[j]:  
            arr[k] = left[i]  
            i += 1 
          
        else: 
            arr[k] = right[j]  
            j += 1 
          
        k += 1
       
    while i < len1:     
        arr[k] = left[i]  
        k += 1 
        i += 1
    
    while j < len2:  
        arr[k] = right[j]  
        k += 1
        j += 1
      
def timSort(arr, n):  
    RUN=32
    for i in range(0, n, RUN):  
        insertionSort(arr, i, min((i+31), (n-1)))  
    
    size = RUN 
    while size < n:  
        for left in range(0, n, 2*size):  
            mid = left + size - 1 
            right = min((left + 2*size - 1), (n-1))  
            merge(arr, left, mid, right)  
          
        size = 2*size 

def getDATA(n):
    data=[]
    '''
    with open('Data.txt','r') as f:
        for line in f:
            for i in line:
                if i != '\n':
                    data.append(i)
            if len(data)>=n:
                break
    '''
    data=[6,2,1,3,7,4,9,10,8,5]
    return data            


#main
#n = int(input("Order to sort (less than equal to 8): "))
time=[]
'''
for j in tqdm(range(10,10**n,100)):
    data = getDATA(j)
    #start_time = timeit.default_timer()
    timSort(data,len(data))
    data = arrange(data)
    #end_time = timeit.default_timer()
    #total_time = end_time - start_time 
    #time.append(total_time)
    
    print(data)
'''
data=getDATA(1)
timSort(data,len(data))
arrange(data)
print(data)
#plotit(time)
