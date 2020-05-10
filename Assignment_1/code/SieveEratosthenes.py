import matplotlib.pyplot as plt
import os
import timeit
time = []


def plotit(data):
    plt.plot(data)
    plt.ylabel("Time")
    plt.show()


class Prime:
    
    def __init__(self,n):
        self.n = n
        self.sieve = []

    def make_Sieve_Eratosthenes(self):
        for i in range(0,(int(self.n**(1/2))+1)**2):
            self.sieve.append(True)  
        self.sieve[0]=False
        self.sieve[1]=False
        for i in range(2,int(self.n**(1/2))+1):
            if(self.sieve[i]):
                for j in range(i*i,(int(self.n**(1/2))+1)**2,i):
                    self.sieve[j]=False

    def find_nearest_Prime(self):
        less = self.n
        more = self.n
        while less>=0:
            if self.sieve[less] or self.sieve[more]:
                return True
        return False
            

#10**8
#main
for i in range(2,10):
    start_time = timeit.default_timer()
    total_time = 10
    s_obj = Prime(i)
    s_obj.make_Sieve_Eratosthenes()
    if(s_obj.find_nearest_Prime()):
        end_time = timeit.default_timer()
        total_time = start_time - end_time
    time.append(total_time)

plotit(time)

'''
for n = 9
Initilizing time : 100.28189619999999
Sieveing time : 217.69900619999999
Writing time : 102.50809070000003
Printing time : 7018.977676
Total time :  7439.4718178
'''
'''
Range
1 - 11 : 97
2 - 101 : 997
3 - 1009 : 9973
4 - 10007 : 99991
5 - 100003 : 999983
6 - 1000003 : 9999991
7 - 10000019 : 99999989
8 - 100000007 : 999999937
'''