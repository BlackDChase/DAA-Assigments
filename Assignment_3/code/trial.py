from tqdm import tqdm
import matplotlib.pyplot as plt
import os
import timeit
import sys

def plotit(data):
    plt.plot(data)
    plt.ylabel("Time")
    plt.show()

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class BST:
    def __init__(self):
        self.root = None

    def v(self):
        return self.root.v
    def l(self):
        return self.root.l
    def r(self):
        return self.root.r

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val,self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

def insert_in_BT(data,root,i):
    if i< len(data):
        temp = Node(data[i])
        root = temp

        root.l = insert_in_BT(data,root.l,2*i+1)
        root.r = insert_in_BT(data,root.r,2*i+2)
    return root

def inOrder(root):
    if root == None:
        return
    inOrder(root.l)
    print(root.v, end=" ")
    inOrder(root.r)

def getInOrder(root):
    val=None
    if root == None:
        return
    if root.l != None:
        val=getInOrder(root.l)
    if val==None:
        val=root.v
        root=root.r
        if val==None:
            val=getInOrder(root)
    return val

def getDATA():
    '''
    data = []
    with open('../../../Data.txt','r') as f:
        for line in f:
            for i in line:
                if i != '\n':
                    data.append(i)
            if len(data)>=10**8
                break
    '''
    data = [1,234,124,135,236,2345]
    return data

if __name__ == '__main__':
    sys.setrecursionlimit(1500)
    time_make_BT = []
    time_convert_to_BST = []
    data = getDATA()
    '''
    for i in range(0,len(data),100):
        
        start = timeit.default_timer()
        binary_tree_root = None
        binary_tree_root = insert_in_BT(data[:i],binary_tree_root,0)
        end = timeit.default_timer()
        time_make_BT.append(end-start)
        
        tree = BST()
        start = timeit.default_timer()
        while binary_tree_root!=None :
            data = getInOrder(binary_tree_root)
            if data !=None:
                tree.add(data)
        end = timeit.default_timer()
        time_convert_to_BST.append(end-start)
        plotit(time_make_BT)
        plotit(time_convert_to_BST)
    '''
    binary_tree_root = None
    binary_tree_root = insert_in_BT(data,binary_tree_root,0)
    print("Orignal Binary tree")
    inOrder(binary_tree_root)
    print("")
    tree = BST()
    while binary_tree_root!=None :
        data = getInOrder(binary_tree_root)
        if data !=None:
            tree.add(data)
    print("Yay")
    inOrder(tree)
