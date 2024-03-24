a = [i for i in range(10001)]

for i in range(1, 10000):
    target = i

    for j in str(i):
        target += int(j)
    
    if target <= 10000:
        a[target] = 0

for i in a:
    if i:
        print(i)
