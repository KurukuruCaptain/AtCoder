import math

x = int(input())

tmp = 100
year = 1

while True:
    if tmp*1.01 >= x:
        print(year)
        exit()
    tmp = int(1.01*tmp)
    year += 1


#print(math.log(x/100, 1.01))
