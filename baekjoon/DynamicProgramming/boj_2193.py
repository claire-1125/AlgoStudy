n = int(input())

d = [[0 for _ in range(2)] for _ in range(n+1)]

for r in range(1,n+1):
    if r == 1:
        d[r][0],d[r][1] = 0,1
    else:
        d[r][0] = sum(d[r-1])
        d[r][1] = d[r-1][0]

print(sum(d[n]))
