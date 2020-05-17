a, b, c, k= list(map(int, input().split()))

if k < a:
    print(k)
elif a <= k < b:
    print(a)
else:
    print(a-(k-a-b))
