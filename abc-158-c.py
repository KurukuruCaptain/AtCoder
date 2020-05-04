a, b = map(int, input().split())

for i in range(1, 100000):
    if (i*0.08)//1 == a and (i*0.1)//1 == b:
        print(i)
        exit()

print(-1)



"""
while True:
    if (c*0.080)//1 == a:
        print(int(c))
        exit()
    elif (c*0.080)//1 >= a or (c*0.1)//1 != b:
        print(-1)
        exit()
    else:
        c += 1.0
"""