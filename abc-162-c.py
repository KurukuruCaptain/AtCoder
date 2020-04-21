"""
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)
"""
"""
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)
"""
import math

k = int(input())


cnt=0

for a in range(1, k+1):
    for b in range(1, k+1):
        tmp=math.gcd(a,b)       
        for c in range(1, k+1):
            cnt += math.gcd(tmp,c)

print(cnt)
