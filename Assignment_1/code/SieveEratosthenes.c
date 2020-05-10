#include<stdio.h>
#include<math.h>
#include<limits.h>
#include<string.h>
#include<stdbool.h>
#include<time.h>
#include<stdlib.h>
int power(int a)
{
    a = (int)(sqrt(a)) + 1;
    return a*a;
}

bool* make(int n)
{
    bool *Prime = malloc((n+1)*sizeof(true));
    memset(Prime+2,true,(n+1)*sizeof(true));
    Prime[0]=false;Prime[1]=false;
    return Prime;
}


void sieveOfEratosthenes(bool Prime[],int n)
{
    for(int i=2; i*i<=n; i++)
    {
        if(Prime[i]==true)
        {
            for(int j=i*i;j<=n;j=j+i)
            {
                Prime[j] = false;
            }
        }
    }
}

void findNearestPrime(int k)
{
    int n = power(k);
    bool *Prime=make(n);
    sieveOfEratosthenes(Prime,n);
    int less=k,more=k;
    while(less>=0)
    {
        if(Prime[less]||Prime[more])
        {
            free(Prime);
            printf("%d %d %d\n",less,k,more);
            break;
        }
        less--,more++;
    }
}

int main()
{
    FILE *filePointer;
    filePointer = fopen("Data.txt", "w");
    //findNearestPrime(100000008);

    for(int i=1;i<100000009;i++)
    {
        double time;
        clock_t start,end;
        start = clock();
        findNearestPrime(i);
        end=clock();
        time = (double)((end - start) / CLOCKS_PER_SEC);
        printf("%lf\n",time);
        fprintf(filePointer,"%lf\n",time);
    }
    printf("YO");
    fclose(filePointer);
    return 0;
}