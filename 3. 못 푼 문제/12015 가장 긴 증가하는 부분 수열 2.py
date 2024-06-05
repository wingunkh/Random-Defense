def binary_search(target):
    left = 0
    right = len(result) - 1

    while left <= right:
        center = (left + right) // 2

        if result[center] >= target:
            right = center - 1
        else:
            left = center + 1

    return left

n = int(input())
a = list(map(int, input().split()))
result = []

for i in a:
    location = binary_search(i)

    if location ==  len(result):
        result.append(i)
    else:
        result[location] = i
        
print(len(result))

# ex) 10 20 1 21 22
# 10 -> [10]
# 20 -> [10, 20]
# 1 -> [1, 20]
# 1이 커버할 수 있는 뒤의 숫자 : >= 2
# 10이 커버할 수 있는 뒤의 숫자 : >= 10
# 즉, 1이 10의 상위 호환 격
# 21 -> [1, 20, 21]
# 22 -> [1, 20, 21, 22] (실제 LIS는 [10, 20, 21, 22])
