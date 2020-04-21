k, n = list(map(int, input().split()))
a = list(map(int, input().split()))

tmp = 0

for i in range(1, len(a)):
    if a[i]-a[i-1] >=tmp:
        tmp = a[i] - a[i-1]

if a[0]+k-a[len(a)-1] > tmp:
    tmp = a[0]+k-a[len(a)-1]

print(k-tmp)