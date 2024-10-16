def search(like):
    tmp = []
    
    for r in range(n):
        for c in range(n):
            if a[r][c] != 0:
                continue
            
            like_point, empty_point = 0, 0
            
            for i in range(4):
                next_r, next_c = r + dr[i], c + dc[i]

                if not (0 <= next_r < n and 0 <= next_c < n):
                    continue

                if a[next_r][next_c] in like:
                    like_point += 1
                elif a[next_r][next_c] == 0:
                    empty_point += 1

            tmp.append([r, c, like_point, empty_point])

    tmp.sort(key = lambda x: (-x[2], -x[3]))
    
    return (tmp[0][0], tmp[0][1])

n = int(input())
a = [[0 for _ in range(n)] for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n * n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

for target, one, two, three, four in b:
    r, c = search([one, two, three, four])
    a[r][c] = target

b.sort(key = lambda x: x[0])

for r in range(n):
    for c in range(n):
        target = a[r][c]
        like = b[target - 1][1:]
        score = 0

        for i in range(4):
            next_r, next_c = r + dr[i], c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < n):
                continue

            if a[next_r][next_c] in like:
                score += 1

        if score != 0:
            result += 10 ** (score - 1)

print(result)
