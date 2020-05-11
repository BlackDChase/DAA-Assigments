import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import timeit

def N2T(n,t,itter,observ):
    a=1123
    for i in range(n):
        for j in range(t):
            for k in range(n):
                for l in range(itter):
                    for m in range(observ):
                        a=a*i*j*k*l*m+1


