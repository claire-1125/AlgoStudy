d = [0] * int(input())
numList = list(map(int,input().split()))

for i in range(len(d)):
    for j in range(i):
        if numList[i] < numList[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1

print(max(d))