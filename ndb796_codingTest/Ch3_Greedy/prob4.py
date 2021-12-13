n = int(input())

# 각 공포도를 원소로 하며 내림차순으로 정렬
nums = sorted(list(map(int,input().split())),reverse=True)
# 3 2 2 2 1

print(nums)

temp_max = 0
cnt = 0

# nums가 빌 때까지 리스트 중 최솟값 뽑아 그 수만큼 모험가 pop → 이를 한 그룹으로 취급
# 탈출 조건??????????????
while nums:
    temp_min = min(nums)
    for i in range(1,temp_min+1):
        if nums[-i] <= temp_min:
            nums.pop()
    cnt += 1

        # if nums[-i] > temp_min:
        #     nums.pop()

print(cnt)