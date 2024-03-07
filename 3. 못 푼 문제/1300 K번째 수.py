n = int(input())
k = int(input())
# k번째 수 == 작거나 같은 값이 k개 있는 수 
left, right = 1, k

while left <= right:
    center = (left + right) // 2
    count = 0

    for i in range(1, n + 1):
        count += min(center // i, n)

    if count >= k: # 중앙값보다 작거나 같은 수의 개수가 k보다 크거나 같을 때
        right = center - 1
    else: # 중앙값보다 작거나 같은 수의 개수가 k보다 작을 때
        left = center + 1

print(left)
