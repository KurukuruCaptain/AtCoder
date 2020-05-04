x = int(input())

for i in range(-1000,1000):
    for j in range(-1000,1000):
        if i ** 5 - j ** 5 == x:
            print(i,j)
            quit()
            
"""
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors
    
x = int(input())

div = make_divisors(x)

for i in range(len(div)):
    if math.pow((x+b**5), 0.2).is_integer():
        print(int(math.pow((x+b**5), 0.2)), b)
            exit()
"""


"""
b = -100

while True:
    if x+b**5 > 0:
        if math.pow((x+b**5), 0.2).is_integer():
            print(int(math.pow((x+b**5), 0.2)), b)
            exit()
        
    b += 1
"""