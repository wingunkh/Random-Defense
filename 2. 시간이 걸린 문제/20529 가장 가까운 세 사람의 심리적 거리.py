import sys
input = sys.stdin.readline

def dfs(x, depth):
    global result
    
    if depth == 3:
        tmp = 0
        
        for i in range(3):
            for j in range(4):
                if stack[i][j] != stack[(i + 1) % 3][j]:
                    tmp += 1

        result = min(result, tmp)
            
        return

    for i in range(x, n):
        stack.append(a[i])
        dfs(i + 1, depth + 1)
        stack.pop()

t = int(input())

for _ in range(t):
    n = int(input())
    a = input().split()
    stack = []
    result = sys.maxsize

    if n > 32:
        print(0)
    else:
        dfs(0, 0)
        print(result)
