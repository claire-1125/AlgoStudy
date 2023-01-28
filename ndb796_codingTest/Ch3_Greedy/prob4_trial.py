# 모험가 n명
# 공포도 = 특정 그룹을 이루는 모험가 인원수
# '그룹 수'의 최대값 -> 공포도가 너무 높은 사람은 지양
# 남은 모험가는 존재할 수 있다.

# n=5 data=[2,3,1,2,2] -> 2

# 공포도가 가장 낮은 사람부터 고려해야 할 것 같다.
# data를 오름차순으로 정렬
# 앞사람부터 본인 수값대로 pop 반복 -> 내림차순으로 해서 pop시켜야 하는구나...
# 뽑으려는 수가 내 수보다 크면 종료?
# pop이란 행위를 반복하는 동안에 나보다 더 큰수가 없었다? 그럼 문제 없음.
# 방금 pop해서 만든 그룹 내부 인원 수 검토
# 검토 방식 : 그룹 내 max값 == 그룹 내 인원 수
# 검토에서 통과하면 진정한 그룹으로 인정 (cnt+1)

n = int(input())

# 1차적으로 오름차순 정렬하고 시작
# 작은 값부터 봐야하나 pop()의 내부구현 문제때문에 내림차순 진행
nums = sorted(list(map(int,input().split())),reverse=True)


"""
### 1차 시도
temp_max = 0
cnt = 0

# nums가 빌 때까지 리스트 중 최솟값 뽑아 그 수만큼 모험가 pop → 이를 한 그룹으로 취급
while nums:
    temp_min = min(nums)
    for i in range(1,temp_min+1):
        if nums[-i] <= temp_min:
            nums.pop()
    cnt += 1

print(cnt)
"""

"""
### 오랜만의 시도
# 그룹 수 카운팅
cnt = 0
pioneer = data[-1]  # 가장 작은 공포도를 가진 모험가

# 리스트가 비기 전까지 반복
while len(data):
    print("here")
    # 모험가 수만큼 pop 반복...
    # now : 현재 대상이 되는 모험가
    # pioneer : 특정 그룹의 인원수가 되는 모험가 숫자
    for _ in range(pioneer):
        now = data.pop()
        print(now)
        if now <= pioneer:
            pioneer = data[-1]
        else:
            break
            # pioneer = now

    cnt += 1

print(cnt)
"""