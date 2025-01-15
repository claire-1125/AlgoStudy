N = int(input())
arr = [int(input()) for _ in range(N)]

# Write your code here!
# 부호가 동일해야 함.
# 연속 부분 수열: 특정 구간에 속하는 숫자 전체
# list = [3,7,8,2,5,9]이고 list[2:5]에 대한 연속 부분 수열은 [8,2,5]를 의미함.

# 이 문제에서는 '부호 동일'이라는 규칙을 준수해야 하므로
# 결국 부호가 같은 그룹을 하나의 연속 부분 수열로 볼 수 있다.

cnt = 0
group_cnt = []

for i in range(N):
    if i == 0:
        cnt += 1
    elif  arr[i-1] * arr[i] < 0:  # 부호가 달라지면
        # 부호가 변경 = 한 쪽만 음수 = 둘이 곱하면 음수
        group_cnt.append(cnt)
        cnt = 1
    else:
        cnt += 1
    

group_cnt.append(cnt)

print(max(group_cnt))