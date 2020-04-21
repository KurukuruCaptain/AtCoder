n = int(input())
a = list(map(int, input().split()))
b = [0]*len(a)

for i, value in enumerate(a):
    b[value-1] += 1

for j in b:
    print(j) 

"""
for i, value in enumerate(a):
    print(a.count(i+1))
print('0')
"""
"""
for i, value in enumerate(a):
    cnt = 0
    for j in range(i, len(a)):
        if a[j] == i+1:
            cnt += 1
    print(cnt)
print('0')
"""
