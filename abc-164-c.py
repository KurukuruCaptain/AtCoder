#ABC 164C

n = int(input())

mylist = [input() for i in range(n)]
output = list(set(mylist))

print(len(output))