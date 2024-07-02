n = int(input())
a = list(map(int, input().split()))
dic = dict()
left, right = 0, 0
count = 0
result = 0

while right < n:
    # 현재 right가 가리키는 숫자를 dic에 추가
    if a[right] in dic:
        dic[a[right]] += 1
    else:
        dic[a[right]] = 1
        count += 1

    # 범위 내 서로 다른 숫자의 개수가 2를 초과하면 left를 오른쪽으로 이동
    while count > 2:
        dic[a[left]] -= 1
        
        if dic[a[left]] == 0:
            del dic[a[left]]
            count -= 1
            
        left += 1

    # 현재 범위의 길이를 결과값과 비교하여 최대값 갱신
    result = max(result, right - left + 1)
    right += 1

print(result)
