from collections import deque

def bfs(r,c):
    # 초기 설정
    if pos[r][c] == 1:
        pos[r][c] = 0
    queue = deque([(r,c)])

    # 상,하,좌,우,북동,북서,남동,남서
    adjacent_r = [-1,+1,0,0,-1,-1,+1,+1]
    adjacent_c = [0,0,-1,+1,+1,-1,+1,-1]
    
    while queue:
        v = queue.popleft()
        for i in range(8):
            r, c = v[0] + adjacent_r[i], v[1] + adjacent_c[i]
            # 범위 내에 존재하는지 확인
            if not ((r in range(w)) and (c in range(h))):
                return False
            # 주위에 대해 체크
            if pos[r][c] == 1:
                queue.append((r,c))
                pos[r][c] = 0

    return True


while True:
    w,h = map(int,input().split())
    if (w,h) == (0,0):
        break

    pos = [[elem for elem in map(int,input().split())] for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if bfs(i,j):
                cnt += 1

    print(cnt)
