n = int(input())
crain = sorted(list(map(int, input().split())), reverse = True)
m = int(input())
box = sorted(list(map(int, input().split())), reverse = True)
result = 0

if crain[0] < box[0]:
    result = -1
else:
    while box:
        result += 1
        
        for i in range(n):
            if box and crain[i] < box[-1]:
                continue

            for j in range(len(box)):
                if crain[i] >= box[j]:
                    box.pop(j)
                    break

print(result)
