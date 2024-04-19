def solution(n, times):
    answer = 0

    # scan range 초기세팅
    left, right = 1, n*max(times)

    while left <= right:
        middle = (left+right)//2

        # [left,middle] 범위 내에 7&10의 배수가 몇 개나 있는가?
        HowManyPeople = 0

        for time in times:
            # 해당 범위 내 7 혹은 10의 배수 개수
            HowManyPeople += middle // time

        # if HowManyPeople == n:
        #     answer = middle
        #     break
        # elif HowManyPeople < n:
        #     left = middle + 1
        # else:
        #     right = middle - 1

        # 의문점: 왜 HowManyPeople == n인 경우에도 answer = middle이 아니라 right = middle -1를 해줘야 하는가?
        if HowManyPeople < n:
            left = middle + 1
            answer = left
        else:
            right = middle - 1

    return answer


# 예상 출력: 28
N = 6
Times = [7,10]

print(solution(N,Times))