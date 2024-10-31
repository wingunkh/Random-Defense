def backtracking(x, depth):
    if depth == m:
        print(*stack, sep = ' ')

        return

    prev = 0

    for i in range(0, n):
        if a[i] != prev:
            prev = a[i]
            stack.append(a[i])
            backtracking(i, depth + 1)
            stack.pop()

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
stack = []

backtracking(0, 0)
