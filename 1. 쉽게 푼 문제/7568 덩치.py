n = int(input())
a = []

for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

for i in range(len(a)):
    target = a[i]
    count = 1
    for j in range(len(a)):
        if i == j:
            continue
        
        if a[j][0] > target[0] and a[j][1] > target[1]:
            count += 1

    print(count, end = ' ')
