import sys
input = sys.stdin.readline

def backtracking(x, depth):
    global result
    
    if depth == m:
        result = min(result, calculate())

        return

    for i in range(x, len(chicken)):
        if not visited[i]:
            visited[i] = True
            backtracking(i + 1, depth + 1)
            visited[i] = False

def calculate():
    total = 0

    for r1, c1 in house:
        distance = sys.maxsize
            
        for i in range(len(chicken)):
            if visited[i]:
                r2, c2 = chicken[i]
                distance = min(distance, abs(r2 - r1) + abs(c2 - c1))

        total += distance

    return total

n, m ,= map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
result = sys.maxsize

for r in range(n):
    for c in range(n):
        if a[r][c] == 1:
            house.append((r, c))
        elif a[r][c] == 2:
            chicken.append((r, c))

visited = [False for _ in range(len(chicken))]

backtracking(0, 0)

print(result)
