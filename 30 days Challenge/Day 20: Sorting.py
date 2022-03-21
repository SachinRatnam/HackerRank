#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    no_of_swap = 0
    for i in range(n):
        for j in range(0,n-1):    
            if a[j] > a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j]
                    no_of_swap += 1
        if (no_of_swap == 0):
            break
    print(f"Array is sorted in {no_of_swap} swaps.")
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')
    
            
        
            
        
