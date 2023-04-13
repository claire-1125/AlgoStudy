def solution(need, lans):
    # 초기 scan range 설정
    left, right = 1, max(lans)
    mid = 0

    while left <= right:
        mid = (left+right)//2
        
        # mid값과 searchNum을 비교
        # 그런데 현재는 그 searchNum을 찾아야 하는 상황

        # 각 랜선마다 mid값 단위로 몇 개를 자를 수 있는가?
        cnt = 0
        for elem in lans:
            cnt += (elem // mid)

        # 이제 cnt와 need 비교
        if cnt < need:  # 개수가 모자른 경우
            right = mid - 1
        elif cnt >= need:  # 개수가 너무 많은 경우 ('최대' 단위길이를 구하고 싶다!)
            left = mid + 1


    return right

# 가진 랜선의 개수, 필요한 랜선의 개수
Given, Need = map(int, input().split())

# 가진 랜선의 길이
Lans = [int(input()) for _ in range(Given)]

print(solution(Need, Lans))

