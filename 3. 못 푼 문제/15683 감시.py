import sys, copy

def dfs(copied, depth):
    global result

    if depth == len(cctv):
        count = 0
        
        for r in range(n):
            for c in range(m):
                if copied[r][c] == 0:
                    count += 1

        result = min(result, count)

        return

    tmp = copy.deepcopy(copied)

    for direction in level[cctv[depth][0]]:
        monitoring(tmp, direction, depth)
        dfs(tmp, depth + 1)
        tmp = copy.deepcopy(copied) 

def monitoring(copied, direction, depth):
    _, r, c = cctv[depth]
    
    for d in direction:
        next_r, next_c = r, c

        while True:
            next_r += dr[d]
            next_c += dc[d]

            if not (0 <= next_r < n and 0 <= next_c < m):
                break

            if copied[next_r][next_c] == 6:
                break

            if copied[next_r][next_c] == 0:
                copied[next_r][next_c] = '#'
                
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cctv = []
level = [[],
         [[0], [1], [2], [3]],
         [[0, 2], [1, 3]],
         [[0, 1], [1, 2], [2, 3], [0, 3]],
         [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
         [[0, 1, 2, 3]]]
result = sys.maxsize

for r in range(n):
    for c in range(m):
        if a[r][c] == 1:
            cctv.append((1, r, c))
        elif a[r][c] == 2:
            cctv.append((2, r, c))
        elif a[r][c] == 3:
            cctv.append((3, r, c))
        elif a[r][c] == 4:
            cctv.append((4, r, c))
        elif a[r][c] == 5:
            cctv.append((5, r, c))
        
dfs(a, 0)

print(result)
