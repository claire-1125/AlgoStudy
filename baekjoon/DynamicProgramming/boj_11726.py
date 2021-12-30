n = int(input())

d = [0] * (n+1)

for i in range(1,n+1):
    if i == 1:
        d[i] = 1
        continue
    elif i == 2:
        d[i] = 2
        continue
    else:
        d[i] = d[i - 1] + d[i - 2]

print(d[n] % 10007)

