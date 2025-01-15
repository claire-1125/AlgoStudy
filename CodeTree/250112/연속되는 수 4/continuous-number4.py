n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!
cnt = 0
group_cnt = []

for i in range(n):
    if i == 0:
        cnt += 1
    elif arr[i-1] >= arr[i]:  # 숫자가 증가하지 않으면
        group_cnt.append(cnt)
        cnt = 1
    else:
        cnt += 1

group_cnt.append(cnt)

print(max(group_cnt))