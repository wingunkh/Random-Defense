def backtracking(x, depth):
    if depth == n:
        print(*stack)
        
        return

    for i in range(1, n + 1):
        if not visited[i]:
            stack.append(i)
            visited[i] = True
            backtracking(i + 1, depth + 1)
            stack.pop()
            visited[i] = False
    
n = int(input())
a = [i for i in range(n + 1)]
visited = [False for _ in range(n + 1)]
stack = []

backtracking(1, 0)
