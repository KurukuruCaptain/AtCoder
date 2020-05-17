n = str(input())

last = n[len(n)-1]

if last == '2' or last == '4' or last == '5' or last == '7' or last == '9':
    print('hon')
elif last == '0' or last == '1' or last == '6' or last == '8':
    print('pon')
else:
    print('bon')