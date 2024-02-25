n = int(input())
a = list(map(int, input().split()))
stack = []
result = [0 for _ in range(n)]

for i in range(n):
    target = (a[i], i) # 다음 탑의 크기와 인덱스
    
    while stack: # 내부 루프의 총 반복 횟수가 N회이므로 이 코드의 시간복잡도는 O(N)이다.
        if stack[-1][0] > target[0]: # 다음 탑이 스택 top의 탑보다 작을 경우 
            result[target[1]] = stack[-1][1] + 1
            break
        else: # 다음 탑이 스택 top의 탑보다 클 경우
            stack.pop()

    if not stack:
        result[target[1]] = 0

    stack.append(target)

print(*result, sep = ' ')
