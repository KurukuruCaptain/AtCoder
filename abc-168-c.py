import math

a, b, h, m = list(map(int, input().split()))

a1 = math.pi*(60*h+m)/360
b1 = math.pi*m/30

print(math.sqrt( (a*math.cos(a1) - b*math.cos(b1))**2 + \
    (a*math.sin(a1) - b*math.sin(b1))**2))

