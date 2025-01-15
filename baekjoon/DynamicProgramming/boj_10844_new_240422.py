# n 자리 수 
n = int(input())

# dp의 차원: (n+1)*10 


# [[0] * 10]이라는 리스트가 n+1번 반복되는 것이 아니라, 
# 동일한 리스트 객체에 대한 참조가 n+1개 생성됩니다. 
# 즉, dp의 각 행은 동일한 리스트 객체를 참조하고 있기 때문에 한 행의 값을 변경하면 다른 행들도 같이 변경됩니다.
# dp = [[0] * 10] * (n+1)

dp = [[0] * 10 for _ in range(n+1)]


# dp table 초기 설정
for c in range(1,10):
    dp[1][c] = 1


for r in range(2,n+1):
    for c in range(10):
        if c == 0:
            dp[r][c] = dp[r-1][c+1]
        elif c == 9:
            dp[r][c] = dp[r-1][c-1]
        else:
            dp[r][c] = dp[r-1][c-1] + dp[r-1][c+1]


print(sum(dp[n]) % 1000000000)