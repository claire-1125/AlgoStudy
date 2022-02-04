# 가지고 있는 랜선 수, 만들고 싶은 랜선 수
k,n = map(int, input().split())

# 각 랜선 길이 가지고 있는 리스트
lans = [int(input()) for _ in range(k)]

# 초기 섫정 (index가 아니라 실제 수를 지정한다!)
left, right = 1, max(lans)

### 이진탐색 ###
while left <= right:
    middle = (left + right) // 2  # 역시 index가 아니고 실제 수
    cnt = 0  # 만들 수 있는 랜선 개수

    for lan in lans:
        cnt += lan // middle  # 분할된 랜선 개수

    if cnt < n:  # 랜선을 너무 큼지막하게 자른 경우
        right = middle - 1
    else:  # 랜선을 너무 잘게 자른 경우
        left = middle + 1


print(right)