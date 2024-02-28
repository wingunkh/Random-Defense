n = int(input())
a = list(map(int, input().split()))
stack = []
result = [-1 for _ in range(n)]

stack.append(0)

for i in range(1, n): # 내부 루프의 총 반복 횟수가 N회이므로 이 코드의 시간복잡도는 O(N)이다.
    while (stack and a[i] > a[stack[-1]]):
        result[stack.pop()] = a[i]

    stack.append(i)

print(*result)
