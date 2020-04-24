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
