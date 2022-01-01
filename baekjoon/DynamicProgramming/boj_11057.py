n = int(input())

dp = [[0 for _ in range(10)] for _ in range(n+1)]

for c in range(10):
    dp[1][c] = 1

for r in range(2,n+1):
    for c in range(10):
        if c == 0:
            dp[r][c] = dp[r-1][c]
        else:
            for j in range(c+1):
                dp[r][c] += dp[r-1][j]
            # dp[r][c] = dp[r][c-1] + dp[r-1][c]

print(sum(dp[n]) % 10007)