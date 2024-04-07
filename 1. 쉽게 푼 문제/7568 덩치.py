n = int(input())
a = []
result = []

for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

for i in range(len(a)):
    target = a[i]
    rank = 1

    for j in range(len(a)):
        if i == j:
            continue

        if a[i][0] < a[j][0] and a[i][1] < a[j][1]:
            rank += 1

    result.append(rank)

print(*result)
