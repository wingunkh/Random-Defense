import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
height = [0 for _ in range(257)]
result_time = sys.maxsize
result_height = 0

for r in range(n):
    for c in range(m):
        height[a[r][c]] += 1

for i in range(257):
    create_count = 0
    delete_count = 0

    for j in range(257):
        if j < i:
            create_count += (i - j) * height[j]
        elif j > i:
            delete_count += (j - i) * height[j]

    if create_count - delete_count <= b:
        if create_count + delete_count * 2 <= result_time:
            result_time = create_count + delete_count * 2
            result_height = i

print(result_time, result_height)
