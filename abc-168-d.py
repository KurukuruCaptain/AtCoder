n, m = list(map(int, input().split()))

a = [0]*(n+1)
b = [0]*(n+1)

mark = [0]*(n+1)
mark_base = [0]*(n+1)

for i in range(m):
    a[i+1], b[i+1] = list(map(int, input().split()))

mark[1] = 1

while True:
    
    if mark == mark_base:
        print(mark)

        if 0 in mark:
            print('No')
            exit()
        else:
            print('Yes')
            for m in range(1,n+1):
                print(mark[m])
            exit()
    else:
        mark_base = mark

    print('a', a)
    print('b', b)
    print('mark', mark)

    for j in range(1, n+1):
        print(mark[j])
        if mark[j] != 0:
            for k in range(m):
                if mark[j] == a[k+1]:
                    mark[b[k+1]] = a[k+1]
                    print(mark[b[k]])
    
                    