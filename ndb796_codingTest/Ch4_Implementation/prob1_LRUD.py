size = int(input())  # 공간의 크기
path = [elem for elem in input().split()]  # 이동경로계획

# 현재 좌표를 표시하는 변수
r, c = 1, 1  # row, column

# L,R,U,D를 좌표형태로 표현해준 list
dr = [0, 0, -1, 1]  # row 변화량
dc = [-1, 1, 0, 0]  # column 변화량

# 각 위치의 좌표를 나타내는 2차원 list
# pos = [[1,1],[1,2],[1,3],...,[5,4],[5,5]]
pos = [[row, column] for row in range(1, 6) for column in range(1, 6)]

for elem in path:
    if elem == 'L':
        i = 0
    elif elem == 'R':
        i = 1
    elif elem == 'U':
        i = 2
    else:
        i = 3

    # 바로 r,c에 대입하면 공간범위 밖으로 나가는 상황을 filtering할 수 없다.
    nr, nc = r + dr[i], c + dc[i]

    if [nr, nc] in pos:
        r, c = nr, nc

print(r, c)