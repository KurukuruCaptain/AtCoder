a = [0] *9

a[0], a[1], a[2] = list(map(int, input().split()))
a[3], a[4], a[5] = list(map(int, input().split()))
a[6], a[7], a[8] = list(map(int, input().split()))

n = int(input())

b = [0]*9

for i in range(n):
    c = int(input())
    for j in range(9):
        if a[j] == c:
            b[j] = 1

if (b[0] == 1 and b[1] == 1 and b[2] == 1) or \
    (b[3] == 1 and b[4] == 1 and b[5] == 1) or \
    (b[6] == 1 and b[7] == 1 and b[8] == 1) or \
    (b[0] == 1 and b[3] == 1 and b[6] == 1) or \
    (b[1] == 1 and b[4] == 1 and b[7] == 1) or \
    (b[2] == 1 and b[5] == 1 and b[8] == 1) or \
    (b[0] == 1 and b[4] == 1 and b[8] == 1) or \
    (b[2] == 1 and b[4] == 1 and b[6] == 1):
    print('Yes')
else:
    print('No')