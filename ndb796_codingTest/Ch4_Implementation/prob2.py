N = int(input())
cnt = 0

# 시,분,초 list
hour = [elem for elem in range(N+1)]
minute = [elem for elem in range(60)]
second = [elem for elem in range(60)]

for h in hour:
    for m in minute:
        for s in second:
            if '3' in str(h)+str(m)+str(s):
                cnt += 1

print(cnt)