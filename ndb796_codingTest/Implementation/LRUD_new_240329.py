n = int(input())
path = [elem.upper() for elem in input().split()]

# 현재 있는 좌표
x,y = 1,1

# 동서남북 좌표 (LRUD)
dx, dy = [-1,+1,0,0], [0,0,-1,+1]

dir = ['L','R','U','D']

for elem in path:
    idx = dir.index(elem)
    x_temp, y_temp = x + dx[idx], y + dy[idx]

    # 범위 내 존재하면 이동
    if not (x_temp <= n and y_temp <= n):
        continue
    else:
        x, y = x_temp, y_temp
        # print(f"이동 후: ({x}, {y})")/

    
print(x, y)


