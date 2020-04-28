n = int(input())
a = list(map(int, input().split()))

num_list = [0]* (len(a)+1)

for i in range(len(a)):
#    num_list[i] = a.count(i)
    num_list[a[i]] += 1

total = 0

for j in range(len(num_list)):
    total += (num_list[j]* (num_list[j]-1))/2

#print(total)

for k in range(len(a)):
#    print(num_list[a[k]]) 
    print(int(total-(num_list[a[k]])+1))
"""
import math

n = int(input())
a = list(map(int, input().split()))

cnt = flaot(0.0)

for i in range(1, len(a)+1):
    b = a[0:i-1]+a[i:len(a)]
    
    cnt = 0.0
    for j in range (1, len(a)):
        cnt += b.count(j)*(b.count(j)-1)/2
    print(int(cnt))
"""