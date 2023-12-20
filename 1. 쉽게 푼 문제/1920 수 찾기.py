def binary_search(n):
    start, end = 0, len(a)-1

    while start <= end:
        center = (start + end) // 2

        if a[center] == n:
            return 1
        elif a[center] < n:
            start = center+1
        else:
            end = center-1

    return 0

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))

for i in b:
    print(binary_search(i))
