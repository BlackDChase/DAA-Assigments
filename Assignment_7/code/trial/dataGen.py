import random as rd
def transmissionMat(nHS):
    transM=[]
    transM.append([0 for i in range(nHS+2)])
    for i in range(nHS):
        weather=[]
        c=1
        for j in range (nHS):
            b=rd.randint(1,100)
            weather.append(b)
            c+=b
        for j in range(nHS):
            weather[j]/=c
        weather.append(1/c)
        weather.append(0)
        transM.append(weather)
    transM.append([1/(nHS) for i in range(nHS)]+[0,0])
    return transM

def emisionMat(nHS,nO):
    emisM=[]
    for i in range(nHS):
        temp=[]
        a=0
        for j in range(nO):
            b=rd.randint(1,100)
            temp.append(b)
            a+=b
        for j in range(nO):
            temp[j]/=a
        emisM.append(temp)
    return emisM #We need its transpose


def observationMat(nO,n):
    a=[str(i) for i in range(nO)]
    o=[a[rd.randint(0,nO-1)] for j in range(n)]
    return o
