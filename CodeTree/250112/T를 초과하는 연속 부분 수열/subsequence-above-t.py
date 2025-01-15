n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!
cnt = 0
group_cnt = []

for i in range(n):
    # print(f'arr[{i}]={arr[i]}')

    if arr[i] > t:
        cnt += 1
    else:
        group_cnt.append(cnt)
        cnt = 0

group_cnt.append(cnt)

print(max(group_cnt))