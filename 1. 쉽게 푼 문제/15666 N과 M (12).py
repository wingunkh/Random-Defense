def backtracking(x, depth):
    if depth == m:
        print(*stack, sep = ' ')

        return

    for i in range(x, len(a)):
        stack.append(a[i])
        backtracking(i, depth + 1)
        stack.pop()

n, m = map(int, input().split())
a = sorted(list(set(map(int, input().split()))))
stack = []

backtracking(0, 0)
