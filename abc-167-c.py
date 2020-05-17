import itertools

n, m, x = list(map(int, input().split()))

a = [[0] * (m) for i in range(n)]

for k in range(n):
    a[k] = list(map(int, input().split()))

min_score = 100000
ok_flag = 1

for d in range(0, m+1):
    for v in itertools.permutations(a, d):
        ok_flag = 1
        cost = 0
        for m1 in range(1, d):
            score = 0
            for m2 in range(0, d):
                score += v[m2][m1]

            if score < x:
                ok_flag = 0
            
            if ok_flag == 1:
                for m3 in range(d):
                    cost += v[m3][0]
                if cost < min_score:
                    min_score = cost

if min_score == 100000000:
    print(-1)
else:
    print(min_score)