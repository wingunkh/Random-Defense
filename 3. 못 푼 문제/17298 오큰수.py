n = int(input())
a = list(map(int, input().split()))
stack = []
result = [-1 for _ in range(n)]

stack.append(0)

for i in range(1, n): # 시간 복잡도 : O(2N)
    while (stack and a[i] > a[stack[-1]]):
        result[stack.pop()] = a[i]

    stack.append(i)

print(*result)
