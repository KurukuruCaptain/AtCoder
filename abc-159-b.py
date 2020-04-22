s = str(input())

kai1 = ''
kai2 = ''

print("len->", len(s))

for i in range(len(s)-1, (len(s)+1)/2, -1):
    kai1 = kai1+s[i]

print(kai1)
