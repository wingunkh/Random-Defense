min, max = map(int, input().split())
a = [i for i in range(min, max + 1)]
result = 0

for i in range(2, int(max ** 0.5) + 1):
    square = i * i
    start_index = min if min % square == 0 else (min // square + 1) * square

    for j in range(start_index, max + 1, square):
        if a[j - min]:
            a[j - min] = 0

for i in a:
    if i:
        result += 1

print(result)
