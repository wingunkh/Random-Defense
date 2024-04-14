from collections import deque

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]
red_r, red_c, blue_r, blue_c = 0, 0, 0, 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for r in range(n):
    for c in range(m):
        if a[r][c] == 'R':
            red_r, red_c = r, c
        elif a[r][c] == 'B':
            blue_r, blue_c = r, c
        
def bfs(red_r, red_c, blue_r, blue_c, depth):
    q = deque()
    q.append((red_r, red_c, blue_r, blue_c, depth))
    visited[red_r][red_c][blue_r][blue_c] = True

    while q:
        red_r, red_c, blue_r, blue_c, depth = q.popleft()

        if depth > 10:
            return -1

        if a[red_r][red_c] == 'O':
            return depth

        for i in range(4):
            red_nr, red_nc, blue_nr, blue_nc = red_r, red_c, blue_r, blue_c
            
            while a[red_nr + dr[i]][red_nc + dc[i]] != '#' and a[red_nr][red_nc] != 'O':
                red_nr += dr[i]
                red_nc += dc[i]

            while a[blue_nr + dr[i]][blue_nc + dc[i]] != '#' and a[blue_nr][blue_nc] != 'O':
                blue_nr += dr[i]
                blue_nc += dc[i]
                
            if a[blue_nr][blue_nc] == 'O':
                continue

            if red_nr == blue_nr and red_nc == blue_nc:
                if abs(red_r - red_nr) + abs(red_c - red_nc) > abs(blue_r - blue_nr) + abs(blue_c - blue_nc):
                    red_nr -= dr[i]
                    red_nc -= dc[i]
                else:
                    blue_nr -= dr[i]
                    blue_nc -= dc[i]

            if not visited[red_nr][red_nc][blue_nr][blue_nc]:
                q.append((red_nr, red_nc, blue_nr, blue_nc, depth + 1))
                visited[red_nr][red_nc][blue_nr][blue_nc] = True

    return -1

print(bfs(red_r, red_c, blue_r, blue_c, 0))
