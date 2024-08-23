def backtracking(x, depth):
    if depth == n:
        calculate()
        
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            stack.append(a[i])
            backtracking(i, depth + 1)
            visited[i] = False
            stack.pop()

def calculate():
    global result
    sum = 0
    
    for i in range(n - 1):
        sum += abs(stack[i] - stack[i + 1])

    result = max(result, sum)

n = int(input())
a = list(map(int, input().split()))
visited = [False for _ in range(n)]
stack = []
result = 0

backtracking(0, 0)

print(result)
