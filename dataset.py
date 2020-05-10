from tqdm import tqdm
from random import randint
n=int(input("Dataset order\t:\t"))
r=int(input("Data range order\t:\t"))
with open('Data.txt','w') as f:
    for i in tqdm(range(10**(n-1))):
        for j in range(10):
            f.write(str(randint(1,10**r))+" ")
        f.write("\n")
          
print("Dataset of order",n,"with a range in order",r,"is created")
