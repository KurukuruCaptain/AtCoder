n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
"""
n = 12
m = 3
a = [4, 56, 78, 901, 2, 345, 67, 890, 123, 45, 6, 789]
"""
for i in range(m):
    if sorted(a)[(i+1)*-1] * 4 * m < sum(a):
        print('No')
        exit()

print('Yes')
