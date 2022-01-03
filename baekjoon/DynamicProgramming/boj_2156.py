n = int(input())
wines = []
d = [0]*n  # 마신 누계 포도주 량

for _ in range(n):
    wines.append(int(input()))

"""
앞으로 마시게 될 것들이 아니라 거꾸로 이전 포도주들을 기준으로 경우를 나누자!
[세 가지 경우]
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