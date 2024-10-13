n, m, k = map(int, input().split())
a = [[[] for _ in range(n)] for _ in range(n)]
direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
result = 0

def move():
    new_a = [[[] for _ in range(n)] for _ in range(n)]
    
    for r in range(n):
        for c in range(n):
            if a[r][c]:
                for w, s, d in a[r][c]:
                    next_r = (r + direction[d][0] * s) % n
                    next_c = (c + direction[d][1] * s) % n
                    new_a[next_r][next_c].append((w, s, d))

    return new_a

def spread():
    for r in range(n):
        for c in range(n):
            if len(a[r][c]) > 1: # 같은 칸에 파이어볼이 2개 이상 있을 경우
                nw, ns, nd, count = 0, 0, [], len(a[r][c])

                for w, s, d in a[r][c]:
                    nw += w
                    ns += s
                    nd.append(d % 2)

                nw = nw // 5
                ns = ns // count

                if len(set(nd)) == 1: # 합쳐지는 파이어볼의 방향이 모두 홀수이거나 짝수일 경우
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]

                if nw > 0:
                    a[r][c] = [(nw, ns, d) for d in nd]
                else: # 질량이 0인 파이어볼은 소멸
                    a[r][c] = []

for _ in range(m):
    r, c, w, s, d = map(int, input().split())
    a[r - 1][c - 1].append((w, s, d))

for _ in range(k):
    a = move()
    spread()

for r in range(n):
    for c in range(n):
        if a[r][c]:
            for w, _, _ in a[r][c]:
                result += w

print(result)
