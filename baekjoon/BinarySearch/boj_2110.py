# 집의 개수, 공유기의 개수
n, c = map(int,input().split())

# 각 집의 좌표
houses = sorted([int(input()) for _ in range(n)])

# 최소거리, 최대거리
left, right = 1, max(houses)-min(houses)


while left <= right:
    middle = (left + right) // 2  # 우리가 찾게될 최적의 설치 간격

    routers = [min(houses)]  # 설치한 공유기의 각 위치
    # 첫번째 집은 무조건 설치하는 것으로 가정

    for house in houses:
        # 현재 집 위치와 이전에 설치한 공유기 위치 간의 거리가 middle 이상이 되면 설치가능하므로
        if house - routers[-1] >= middle:
            routers.append(house)


    if len(routers) < c:
        right = middle - 1
    else:
        left = middle + 1


print(right)