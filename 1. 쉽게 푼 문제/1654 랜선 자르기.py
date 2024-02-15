def binary_search():
    start = 1
    end = max(a)

    while start <= end:
        center = (start + end) // 2
        tmp = 0

        for i in a:
            tmp += i // center

        if tmp >= m:
            start = center + 1
        else:
            end = center - 1

    return end

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]

print(binary_search())
