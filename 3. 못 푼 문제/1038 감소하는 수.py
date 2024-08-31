n = int(input())
num = "0123456789"
count = 2 # 자릿수
result = []

for i in num:
    result.append(i)

while count < 11: # 9876543210가 감소하는 수의 최댓값이며, 총 11자리
    for i in result:
        if len(i) + 1 == count:
            for j in range(10):
                if j < int(i[-1]):
                    result.append(i + str(j))

    count += 1

if n > len(result) - 1:
    print(-1)
else:
    print(result[n])
