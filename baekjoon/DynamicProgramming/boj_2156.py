n = int(input())
wines = []
d = [0]*n  # 마신 누계 포도주 양

for _ in range(n):
    wines.append(int(input()))

"""
앞으로 마시게 될 것들이 아니라 거꾸로 이전 포도주들을 기준으로 경우를 나누자!
[세 가지 경우]
d[i]에 넣어주는 값
- 현재 O, 이전 O, 전전 X (wines[i]+wines[i-1]+d[i-3])
- 현재 O, 이전 X, 전전 O (wines[i]+d[i-2])
- 현재 X, 이전 O, 전전 O (d[i-1])
"""

# 첫번째와 두번째 잔은 무조건 마신다고 가정한다.
d[0] = wines[0]

if n > 1:
    d[1] = wines[0]+wines[1]

if n > 2:
    d[2] = max(wines[2]+wines[1], wines[2]+wines[0], d[1])  # 순서대로 위의 세 가지 경우 중 최대값 선택

for i in range(3, n):
    d[i] = max(wines[i]+wines[i-1]+d[i-3], wines[i]+d[i-2], d[i-1])  # 순서대로 위의 세 가지 경우 중 최대값 선택

print(d[n-1])


"""
<다른 풀이 예시>
for i in range(n):
  array[i] = int(input())
dp = [0]*10000
dp[0] = array[0]
dp[1] = array[0]+array[1]
dp[2] = max(array[2]+array[0], array[2]+array[1], dp[1])
for i in range(3,n):
  dp[i] = max(array[i]+dp[i-2], array[i]+array[i-1]+dp[i-3], dp[i-1])
print(max(dp))
"""
