import matplotlib.pyplot as plt
import os
import timeit
import tqdm
import threading

class Prime:
    
    def __init__(self,n):
        self.n = n
        self.sieve = []

    def make_Sieve_Eratosthenes(self):
        for i in range(0,(int((self.n)**(1/2))+1)**2+2):
            self.sieve.append(True)  
        self.sieve[0]=False
        self.sieve[1]=False
        for i in range(2,int(self.n**(1/2))+2):
            if(self.sieve[i]):
                for j in range(i*i,(int(self.n**(1/2))+1)**2,i):
                    self.sieve[j]=False
        return len(self.sieve)

    def find_nearest_Prime(self):
        less = self.n
        more = self.n
        while less>=0:
            try:
                if self.sieve[less] or self.sieve[more]:
                    return [True,less,more]
            except:
                return [False,less,more,i]
            less = less - 1
            more = more + 1
        return [False,less,more,i]
'''
def plotit(data):
    print(data)
    plt.plot(data)
    plt.ylabel("Time")
    plt.show()
'''
 
def plotit(datay,datax):
    plt.plot(datax,datay)
    plt.ylabel("Time")
    plt.show()

def getTime(i):
    start_time = timeit.default_timer()
    s_obj = Prime(i)
    s_obj.make_Sieve_Eratosthenes()
    fact = s_obj.find_nearest_Prime()
    if(fact[0]):
        end_time = timeit.default_timer()
        total_time = end_time - start_time
    else:
        print(fact)
    del s_obj
    return total_time


time = []
number = []
for i in tqdm.tqdm(range(2,10**6)):
    total_time = getTime(i)
    time.append(total_time)
    number.append(i)

for i in range(len(time)):
    if time[i]==100:
        print(i)

plotit(time.reverse(),number.reverse())
