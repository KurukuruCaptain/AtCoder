from collections import deque

S = str(input())
Q = int(input())

tmp = deque(S)
houkou = 1 #1:foward 2:reverse

for i in range(Q):
    inp = input().split()
    if inp[0] == '1':
        if houkou == 1:
            houkou = 2
        else:
            houkou = 1
    else:
        if houkou == 1 and inp[1] == '1':
            tmp.appendleft(inp[2])
        elif houkou == 1 and inp[1] == '2':
            tmp.append(inp[2])
        elif houkou == 2 and inp[1] == '1':
            tmp.append(inp[2])
        else:
            tmp.appendleft(inp[2])
    
#    print(houkou, tmp)

output = ''.join(list(tmp))
if houkou == 2:
    output = output[::-1]

print(output)
