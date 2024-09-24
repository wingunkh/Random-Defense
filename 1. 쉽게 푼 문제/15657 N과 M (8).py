def backtracking(x, depth):
    if depth == m:
        print(*stack)

        return

    for i in range(x, n):
        stack.append(a[i])
        backtracking(i, depth + 1)
        stack.pop()

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
stack = []

backtracking(0, 0)
