# https://velog.io/@happyyeon/%EC%86%8C%ED%94%84%ED%8B%B0%EC%96%B4-%EC%A1%B0%EB%A6%BD%EB%9D%BC%EC%9D%B8
# https://fre2-dom.tistory.com/37


workingTimeA, workingTimeB = [], []
movingAtoB, movingBtoA = [], []

# 입력 받기
NumPlaces = int(input())
for i in range(NumPlaces):
    if i < (NumPlaces-1):
        a,b,c,d = map(int,input().split())
        # 각 작업장당 작업시간 저장
        workingTimeA.append(a)
        workingTimeB.append(b)
        # 작업장 간 이동시간 저장
        movingAtoB.append(c)
        movingBtoA.append(d)
    else:
        a,b = map(int,input().split())
        workingTimeA.append(a)
        workingTimeB.append(b)


# [(1, 3), (10, 2)]
workingTimes = list(zip(workingTimeA,workingTimeB))

minResult = 0
minResult_ = 0

# 앞에서부터 순회하며 매번 최선 선택
for j in range(NumPlaces):

    a = workingTimes[j][0]
    b = workingTimes[j][1]

    minResult += min(a, b)
    here = (a,b).index(min(a,b))

    # a < b인 경우
    if here == 0:
        minResult_ = minResult + movingAtoB[here]

    # a > b인 경우
    elif here == 1:
        minResult_ = minResult + movingBtoA[here]




    # tempMin = 0
    #
    # for a,b in zip(workingTimeA, workingTimeB):
    #     if a > b:
    #         tempMin = b
    #         # 다음 것에 대해 a vs. b 따진다.
    #         tempMin + next(b)
    #         tempMin + iter(a)
    #     else:
    #         tempMin = a






"""

workingTimeA = [1,10]
workingTimeB = [3,2]
movingAtoB = [1]
movingBtoA = [2]

1   3
(1) (2)
10  2

매 순간마다 최선을 선택하자: 그리디?
a라인인지 b라인인지 구분필요

zip() 이용해 더 작은 값 선택
다른 리스트로 이동할 경우에 한해 이동시간 추가

아니면 프로그래머스의 입국심사와 유사: 이분탐색?

동적계획법?
"""