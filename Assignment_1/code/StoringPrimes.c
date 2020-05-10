#include<stdio.h>
#include<math.h>
#include<limits.h>
#include <time.h>
long long power10(int a)
{
    long long n = 1;
    while(a--)  n=n*10;
    return n;
}

bool make(long long n)
{
    bool Prime[n+1];
    memset(Prime+2,true,(n+1)*sizeof(true))
    Prime[0]=false;Prime[1]=false;
    return Prime;
}


void sieveOfEratosthenes(bool Prime[],long long n)
{
    for(long long i=2; i*i<=n; i++)
    {
        if(Prime[i])
        {
            for(long long j=i*i;j*j<=n;j++)
            {
                Prime[j] = false;
            }
        }
    }
}

void writeToFile(bool Prime[],int a)
{
    char name[] = "Prime_list_ .txt"
    for(int i=1;i<n;i++)
    {
        char name[11] = n+48;
        FILE *filePointer;
        filePointer = fopen(name, "w");
        for(long long j=power(i); j<power(j+1); j++)
        {
            if(Prime[j]) fprintf("%lld\n",j);
        }
    }
}

void printPrimes(bool Prime[],long long n)
{
    for(long long i=0;i<=n;i++)
    {
        if(Prime[i]) printf("%lld\n",i);
    }
}

int main(int a)
{
    clock_t start, end;
    long long int n = power(a);

    double initializingTime,sieveingTime;
    start = clock();
    bool *Prime=make(n);
    end = clock();
    initializingTime = ((double) (end - start)) / CLOCKS_PER_SEC;
    
    start = clock();
    sieveOfEratosthenes(Prime,n);
    end = clock();
    sieveingTime = ((double) (end - start)) / CLOCKS_PER_SEC;
    
    start = clock();
    writeToFile(Prime,a);
    end = clock();
    writingTime = ((double) (end - start)) / CLOCKS_PER_SEC;

    start = clock();
    printPrimes(Prime,n);
    end = clock();
    printingTime = ((double) (end - start)) / CLOCKS_PER_SEC;
    return 0;
}