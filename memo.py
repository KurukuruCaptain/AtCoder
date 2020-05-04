#####入力
a = str(input())
a, b, c = inp.split()
a, b, c = list(map(int, input().split()))

#####リスト
#初期化
mylist = [0]*10
#リストの先頭に追加したい時などはdequeを使う

#count回避
num_list = [0]* (len(a)+1)
for i in range(len(a)):
#    num_list[i] = a.count(i)
    num_list[a[i]] += 1

#####MATH
#べき乗
math.pow(l/3, 3)

