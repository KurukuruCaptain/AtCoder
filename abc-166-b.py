n, k = list(map(int, input().split()))

sunuke = [0]*(n+1)

for j in range(k):
    d = int(input())
    a = list(map(int, input().split()))
    for i in range(d):
        sunuke[a[i]] += 1

cnt = 0

for k in range(1, n+1):
    if sunuke[k] == 0:
        cnt += 1

print(cnt)