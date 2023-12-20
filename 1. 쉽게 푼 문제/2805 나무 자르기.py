def binary_search(start, end):
    while start <= end:
        center = (start + end) // 2
        trees = 0
        
        for tree in a:
            if tree > center:
                trees += tree - center

        if trees >= m:
            start = center+1
        else:
            end = center-1

    print(end)
            
n, m = map(int, input().split())
a = list(map(int, input().split()))

binary_search(0, max(a))
