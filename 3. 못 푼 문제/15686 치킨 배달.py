import sys
input = sys.stdin.readline

def dfs(index, depth):
    global result

    if depth == m:
        tmp = 0
        
        for r1, c1 in house:
            distance = sys.maxsize

            for i in range(len(check)):
                if check[i]:
                    r2, c2 = chicken[i]
                    distance = min(distance, abs(r1 - r2) + abs(c1 - c2))

            tmp += distance

        result = min(result, tmp)

        return

    for i in range(index, len(chicken)):
        check[i] = True
        dfs(i+1, depth+1)
        check[i] = False
            
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
house = []
chicken = []
check = []
result = sys.maxsize

for r in range(n):
    for c in range(n):
        if a[r][c] == 1:
            house.append((r, c))
        elif a[r][c] == 2:
            chicken.append((r, c))

check = [False for _ in range(len(chicken))]

dfs(0, 0)

print(result)
