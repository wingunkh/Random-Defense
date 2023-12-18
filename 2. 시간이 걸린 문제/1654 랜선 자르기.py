def binary_search(start, end):
    while start <= end:
        center = (start + end) // 2
        count = 0
        
        for i in a:
            count += i // center

        if count >= k:
            start = center+1
        else:
            end = center-1

    print(end)

n, k = map(int, input().split())
a = [int(input()) for  _ in range(n)]

binary_search(1, max(a))
