#ABC 164A

s, w = list(map(int, input().split()))

if s <= w:
    print('unsafe')
else:
    print('safe')