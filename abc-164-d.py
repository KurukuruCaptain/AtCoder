#ABC 164D

def count(text, part):
    return sum(text.startswith(part, i) for i in range(len(text)))

#s = str(input())
#s = '1817181712114'
s = '14282668646'

cnt = 0

for i in range(0, 11):
    cnt += count(s, str(2019*i))

print(cnt)

"""
for i in range(0, 11):
    if s.count(str(2019*i)) > 0:
        print(i)
        print(s.count(str(2019*i)))
        cnt += s.count(str(2019*i))

print(cnt)
"""
"""

for i in range(0, len(s)+1):
    for j in range(i+1, len(s)+1):
        if int(s[i:j]) % 2019 == 0:
            cnt += 1
#           print(int(s[i:j]))

print(cnt)

"""