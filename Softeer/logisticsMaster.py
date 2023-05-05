# 문제링크: https://softeer.ai/practice/info.do?idx=1&eid=581

from itertools import permutations

numRail, basketMass, timeOfWork = map(int,input().split())
weightPerRail = list(map(int,input().split()))

# 각 레일별 전용 무게 순서 어떻게??
# [(5, 8, 10, 19, 7), (5, 8, 10, 7, 19), (5, 8, 19, 10, 7),...]
permu = list(permutations(weightPerRail,numRail))

candidates = []

for rails in permu:
    tempSum = 0
    totSum = 0
    while timeOfWork > 0:
        # circular iteration 해야 하는 게 문제...
        for i in range(len(rails)):
            if tempSum <= basketMass:
                tempSum = sum(rails[:i+1])
            else:

                # 직전까지를 해야 함....
                # totSum += tempSum
                totSum += sum(rails[:i-1])
                rails = rails[i-1:]
                tempSum = 0
                continue

        timeOfWork -= 1

    # candidates 에 합산 결과 추가
    candidates.append(totSum)




