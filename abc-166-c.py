n, m = list(map(int, input().split()))

h = list(map(int, input().split()))

yoi_warui = [0]*n
dokuritsu = [0]*n

for i in range(m):
    a, b = list(map(int, input().split()))
    dokuritsu[a-1] = 1
    dokuritsu[b-1] = 1
    if h[a-1] == h[b-1]:
        yoi_warui[a-1] = 1
        yoi_warui[b-1] = 1
    elif h[a-1] < h[b-1]:
        yoi_warui[a-1] = 1
    elif h[b-1] < h[a-1]:
        yoi_warui[b-1] = 1

print(yoi_warui.count(0))

