import itertools

n, m, q = list(map(int, input().split()))

i_list = list(range(m))

num_list = list(itertools.combinations(i_list, n))

max_num = 0

for j in range(len(num_list)):   
    
    a, b, c, d = list(map(int, input().split()))
    tmp = 0

    for i in range(q):
        a, b, c, d = list(map(int, input().split()))     
        if (num_list[j][b-1] - num_list[j][a-1]) == c:
            tmp = tmp+ d
    
    if tmp > max_num:
        max_num = tmp

print (max_num)

"""


for i in range(q):
    a, b, c, d = list(map(int, input().split()))

    for j in range(n):
#        print(num_list[0][b-1], num_list[0][a-1], c)
        if (num_list[j][b-1] - num_list[j][a-1]) == c:
            print('Yes') 

"""
#print(len(num_list))