n = int(input())
result = 0

for number in range(1, n + 1):
    number_list = list(map(int, str(number)))
    
    if number < 100:
        result += 1
        continue
    
    for i in range(2, len(number_list)):
        if number_list[i] - number_list[i - 1] != number_list[i - 1] - number_list[i - 2]:
            break
    else:
        result += 1

print(result)
