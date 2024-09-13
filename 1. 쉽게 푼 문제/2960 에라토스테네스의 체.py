n, m = map(int, input().split())
a = [i for i in range(n + 1)]
a[1] = 0
count = 0

for i in range(2, len(a)):
    if a[i] == 0:
        continue

    for j in range(i, len(a), i):
        if a[j] != 0:
            a[j] = 0
            count += 1

        if count == m:
            print(j)
            exit()
