def backtracking(x, depth):
    if depth == m:
        print(*stack, sep = ' ')

        return

    for i in range(n):
        stack.append(a[i])
        backtracking(i, depth + 1)
        stack.pop()

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
stack = []

backtracking(0, 0)
