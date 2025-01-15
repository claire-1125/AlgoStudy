n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!
cnt = 0  # 각 숫자 그룹당 숫자 개수 카운팅

group_cnt = []  # 각 숫자 그룹의 개수 카운팅 리스트

for i in range(n):
    if i==0:
        cnt += 1
    elif arr[i] != arr[i-1]:
        group_cnt.append(cnt)
        cnt = 1
    else:
        cnt += 1

group_cnt.append(cnt)  # 맨 마지막 숫자 그룹의 개수 카운팅 추가

print(max(group_cnt))