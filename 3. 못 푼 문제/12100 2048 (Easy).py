from copy import deepcopy

def up(a):
    for c in range(n):
        target = 0
        for r in range(1, n):
            if a[r][c]:
                tmp = a[r][c]
                a[r][c] = 0
                
                if a[target][c] == 0:
                    a[target][c] = tmp
                elif a[target][c] == tmp:
                    a[target][c] *= 2
                    target += 1
                else:
                    target += 1
                    a[target][c] = tmp

    return a

def down(a):
    for c in range(n):
        target = n - 1
        for r in range(n - 2, -1, -1):
            if a[r][c]:
                tmp = a[r][c]
                a[r][c] = 0
                
                if a[target][c] == 0:
                    a[target][c] = tmp
                    a[r][c] = 0
                elif a[target][c] == tmp:
                    a[target][c] *= 2
                    target -= 1
                else:
                    target -= 1
                    a[target][c] = tmp
                    
    return a

def left(a):
    for r in range(n):
        target = 0
        for c in range(1, n):
            if a[r][c]:
                tmp = a[r][c]
                a[r][c] = 0
                
                if a[r][target] == 0:
                    a[r][target] = tmp
                    a[r][c] = 0
                elif a[r][target] == tmp:
                    a[r][target] *= 2
                    target += 1
                else:
                    target += 1
                    a[r][target] = tmp

    return a

def right(a):
    for r in range(n):
        target = n - 1
        for c in range(n - 2, -1, -1):
            if a[r][c]:
                tmp = a[r][c]
                a[r][c] = 0
                
                if a[r][target] == 0:
                    a[r][target] = tmp
                    a[r][c] = 0
                elif a[r][target] == tmp:
                    a[r][target] *= 2
                    target -= 1
                else:
                    target -= 1
                    a[r][target] = tmp
                    
    return a


def dfs(a, depth):
    global result
    
    if depth == 5:
        for r in range(n):
            for c in range(n):
                result = max(result, a[r][c])

        return

    dfs(up(deepcopy(a)), depth + 1)
    dfs(down(deepcopy(a)), depth + 1)
    dfs(left(deepcopy(a)), depth + 1)
    dfs(right(deepcopy(a)), depth + 1)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
result = 0

dfs(a, 0)

print(result)
