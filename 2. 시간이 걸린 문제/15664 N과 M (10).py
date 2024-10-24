def backtracking(x, depth):
    prev = 0
    
    if depth == m:
        print(*stack, sep = ' ')

        return

    for i in range(x, n):
        if a[i] != prev:
            prev = a[i]
            stack.append(a[i])
            backtracking(i + 1, depth + 1)
            stack.pop()

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
stack = []

backtracking(0, 0)
