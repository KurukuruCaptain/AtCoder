s = str(input())
t = str(input())

if t.startswith(s) and len(s)+1 == len(t):
    print('Yes')
else:
    print('No')
    