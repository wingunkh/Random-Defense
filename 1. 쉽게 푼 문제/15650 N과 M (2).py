def backtracking(x, depth):
    if depth == m:
        print(*stack, sep = ' ')

        return

    for i in range(x, n + 1):
        stack.append(i)
        backtracking(i + 1, depth + 1)
        stack.pop()

n, m = map(int, input().split())
a = [i for i in range(1, n + 1)]
stack = []

backtracking(1, 0)

