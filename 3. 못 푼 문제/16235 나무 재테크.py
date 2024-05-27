from collections import deque

n, m, k = map(int, input().split())
a = [[5 for _ in range(n)] for _ in range(n)] # 양분
b = [list(map(int, input().split())) for _ in range(n)] # 매년 추가되는 양분
tree = [[deque() for _ in range(n)] for _ in range(n)] # 나무
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
result = 0

for _ in range(m):
    x, y, age = map(int, input().split())
    tree[x - 1][y - 1].append(age)

for _ in range(k):
    for r in range(n):
        for c in range(n):
            alive_tree = deque()
            tmp = 0
            
            while tree[r][c]:
                age = tree[r][c].popleft()
                
                if a[r][c] >= age: # 봄
                    a[r][c] -= age
                    alive_tree.append(age + 1)
                else: # 여름
                    tmp += age // 2

            tree[r][c] = alive_tree
            a[r][c] += tmp

    for r in range(n):
        for c in range(n):
            for age in tree[r][c]:
                if age % 5 == 0: # 가을
                    for i in range(8):
                        next_r, next_c = r + dr[i], c + dc[i]

                        if not (0 <= next_r < n and 0 <= next_c < n):
                            continue

                        tree[next_r][next_c].appendleft(1)

            a[r][c] += b[r][c] # 겨울

for r in range(n):
    for c in range(n):
        result += len(tree[r][c])

print(result)
