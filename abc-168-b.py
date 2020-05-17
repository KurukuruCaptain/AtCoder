k = int(input())
s = str(input())

if len(s) > k:
    print(s[:k]+ '...')
else:
    print(s)
