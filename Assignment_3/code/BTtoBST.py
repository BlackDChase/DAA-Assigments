from tqdm import tqdm
import matplotlib.pyplot as plt
import os
import timeit
import sys

def plotit(x,data):
    plt.plot(x,data)
    plt.ylabel("Time")
    plt.show()

class NodeBST:
    
    def __init__(self,val):
        self.v = val
        self.l = None
        self.r = None
    
    def Aleft(self,Node):
        self.l = Node
    
    def Aright(self,Node):
        self.r = Node
    
    def left(self):
        return self.l
    
    def right(self):
        return self.r
    
    def val(self):
        return self.v
    
    def addBST(self,Node):
        if self.v==Node.v:
            return
        elif self.v>Node.v:
            if self.l == None:
                self.l = Node
                return
            else:
                self.l.addBST(Node)
                return
        else:
            if self.r == None:
                self.r = Node
                return
            else:
                self.r.addBST(Node)
                return

class NodeBT:
    def __init__(self,val):
        self.v = val
        self.l = None
        self.r = None

def insertBT(arr, root, i):
    
    if i<len(arr):
        temp = NodeBT(arr[i])
        root = temp
        root.l = insertBT(arr,root.l,2*i+1)
        root.r = insertBT(arr,root.r,2*i+2)
    return root

def getDATA():
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
            if len(data)>=10**3:
                break
    '''
    data = [1,234,124,135,236,2345]
    '''
    return data

def printInOrder(root):
    if root == None:
        return
    printInOrder(root.l)
    print(root.v,end=' ')
    printInOrder(root.r)
    
if __name__ == '__main__':
    
    #sys.setrecursionlimit(1500)
    #time_make_BT = []
    time_convert_to_BST = []
    x=[]
    data = getDATA() 
    for j in tqdm(range(100,len(data),100)): 
        start = timeit.default_timer()
        #rootBT = None
        #rootBT = insertBT(data,rootBT,0)
        #end = timeit.default_timer()
        #time_make_BT.append(end-start)
        rootBST = NodeBST(data[0])
        for i in range(1,j):
            rootBST.addBST(NodeBST(data[i]))
        
        end = timeit.default_timer()

        time_convert_to_BST.append(end-start)
        x.append(j)
    plotit(x,time_convert_to_BST)
    #plotit(x,time_make_BT)
'''
        print("BT: ")
        printInOrder(rootBT)
        print("\nBST: ")
        printInOrder(rootBST)
        print("")
        print(data)
'''
