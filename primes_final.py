import numpy as np
import pandas as pd 

def primes_calc(limit):

    if limit==0:
        matrix=[0]
    if limit==1:
        matrix=[0,1]
    if limit==2:
        matrix=[0,1,1]
    if limit==3:
        matrix=[0,1,1,1]
    if limit==4:
        matrix=[0,1,1,1,0]
    if limit >=5:

        matrix=[0]*(limit+1)

        matrix[0]=0
        matrix[1]=1
        matrix[2]=1
        matrix[3]=1
        matrix[4]=0
        x=1
        while x * x <= limit:
            y = 1
            while y * y <= limit:

                n = (4 * x * x) + (y * y)
                if (n <= limit and (n % 12 == 1 or n % 12 == 5)):
                    matrix[n] ^= 1

                n = (3 * x * x) + (y * y)
                if n <= limit and n % 12 == 7:
                    matrix[n] ^= 1

                n = (3 * x * x) - (y * y)
                if (x > y and n <= limit and n % 12 == 11):
                    matrix[n] ^= 1
                y += 1
            x += 1

        r = 5
        while r * r <= limit:
            if matrix[r]:
                for i in range(r * r, limit+1, r * r):
                    matrix[i] = 0
            r += 1
            
    return matrix

limit=100000
A=primes_calc(limit)*np.arange(limit+1,dtype=int)

for i in A:
    if A[i]:
        print(i,end=" ")