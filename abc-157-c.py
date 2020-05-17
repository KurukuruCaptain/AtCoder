n, m = list(map(int, input().split()))

s = [0]*(m+1)
c = [0]*(m+1)

for k in range(m):
    s[k], c[k] = list(map(int, input().split()))

for l in range(m):
    if n == 1:
        if s[l] != 1:
            print(-1)
            exit()
    elif n == 2:
        if s[l] == 3 or (s[l] == 1 and c[l] == 0):
            print(-1)
            exit()
    elif n == 3:
        if s[l] == 1 and c[l] == 0:
            print(-1)
            exit()

if n == 1:
    for num in range(0, 10):
        seigo = 1
        for i in range(m):
            if num != c[i]:
                seigo = 0
        if seigo == 1:
            print(num)
            exit()
    print(-1)
    exit()
elif n == 2:
    for num in range(10, 100):
        seigo = 1
        for i in range(m):
            if s[i] == 1:
                if num//10 != c[i]:
                    seigo = 0
            if s[i] == 2:
                if num%10 != c[i]:
                    seigo = 0
        if seigo == 1:
            print(num)
            exit()
    print(-1)
    exit()
else:
    for num in range(100, 1000):
        seigo = 1
        for i in range(m):
            if s[i] == 1:
                if num//100 != c[i]:
                    seigo = 0
            elif s[i] == 2:
                if (num-100*(num//100))//10 != c[i]:
                    seigo = 0
            elif s[i] == 3:
                if num%10 != c[i]:
                    seigo = 0
        if seigo == 1:
            print(num)
            exit()
    print(-1)
    exit()

 