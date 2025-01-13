n, t = map(int, input().split())  # n*n map, t초
r, c, d = input().split()  # 초기 위치 (r,c), 초기 방향 d
r, c = int(r), int(c)

# Write your code here!
dr, dc = [-1, 0, 0, 1], [0, 1, -1, 0]  # U,R,L,D

mapper = {
    'U': 0, 
    'R': 1,
    'L': 2,
    'D': 3
}

mapper_list = list(mapper.items())

for _ in range(t):
    r_, c_ = r + dr[mapper[d]], c + dc[mapper[d]]

    if not ((r_ in range(1,n+1)) and (c_ in range(1,n+1))): # 격자 밖일 경우
        d = mapper_list[3 - mapper[d]][0]  # 방향 전환 (짝궁: U+D, R+L)
        continue  # 이걸 넣어야 방향 전환도 1초 카운팅이 됨.

    r, c = r_, c_


print(r, c)