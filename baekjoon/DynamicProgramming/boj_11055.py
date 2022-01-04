d = [1] * int(input())  # 증가 부분 수열의 누적합
numList = list(map(int,input().split()))

d[0] = numList[0]  # 첫번째 원소

for i in range(len(d)):
    for j in range(i):
        if numList[j] < numList[i]:  # 증가 부분 수열이 된다면
            d[i] = max(d[i],d[j]+numList[i])
        else:
            d[i] = max(d[i],numList[i])

print(max(d))