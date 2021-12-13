n,k = map(int,input().split())
cnt = 0

# 1이 될 때까지 진행
while n > 1:
    if n % k != 0:  # 본인과 가장 근접한 k의 배수를 구할 때까지 반복
        n -= 1
        cnt += 1
    else:  # 본인과 가장 근접한 k의 배수를 찾은 순간
        n //= k
        cnt += 1

print(cnt)
