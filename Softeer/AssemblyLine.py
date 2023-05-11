workingTimeA, workingTimeB = [], []
movingAtoB, movingBtoA = [], []

# 입력 받기
NumPlaces = int(input())
for i in range(NumPlaces):
    if i < (NumPlaces-1):
        a,b,c,d = map(int,input().split())
        workingTimeA.append(a)
        workingTimeB.append(b)
        movingAtoB.append(c)
        movingBtoA.append(d)
    else:
        a,b = map(int,input().split())
        workingTimeA.append(a)
        workingTimeB.append(b)




# 앞에서부터 순회하며 매번 최선 선택
for j in range(NumPlaces):
    # [(1, 3), (10, 2)]
    workingTimes = list(zip(workingTimeA,workingTimeB))
    # workingTimes[j]


"""
1   3
(1) (2)
10  2

매 순간마다 최선을 선택하자: 그리디?
a라인인지 b라인인지 구분필요
"""