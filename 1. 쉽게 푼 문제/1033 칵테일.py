def dfs(A):
    visited[A] = True

    for B, P, Q in a[A]:
        if not visited[B]:
            result[B] *= result[A] * Q // P                               
            dfs(B)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
a = [[] for _ in range(n)]
visited = [False for _ in range(n)]
lcm = 1
result = [1 for _ in range(n)]

for _ in range(n - 1):
    A, B, P, Q = map(int, input().split())
    a[A].append((B, P, Q))
    a[B].append((A, Q, P))
    lcm *= P * Q //gcd(P, Q)

result[0] = lcm
dfs(0)
result_gcd = result[0]

for i in range(1, n):
    result_gcd = gcd(result_gcd, result[i])
    
for i in result:
    print(i // result_gcd, end = ' ')
