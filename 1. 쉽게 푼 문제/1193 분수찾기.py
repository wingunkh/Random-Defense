n = int(input())
count = 0
tmp = 2

for i in range(1, 10000001):
    count += 1
    
    if i == n:
        if tmp % 2 != 0:
            print(count, end = '')
            print('/', end = '')
            print(tmp - count)
        else:
            print(tmp - count, end = '')
            print('/', end = '')
            print(count)

        break

    if count == tmp - 1:
        tmp += 1
        count = 0
