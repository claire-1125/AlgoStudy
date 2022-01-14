"""
0 0이 나오기 전까지 계속 진행 → while로 돌리기
상하좌우 + 대각선(8가지)이 갈 수 있는 곳
1 : 땅
각 그래프(땅)에 대해 BFS 실행하고 끝나는 순간 count + 1
지도 그 자체를 visited 배열로도 사용하자
"""

from collections import deque

def bfs(r,c):
    # 초기 설정
    queue = deque([(r,c)])
    pos[r][c] = 0

    """
    * 큐의 역할 : 방문 후보군을 넣어놓는 임시저장소
    
    큐가 빌 때까지 
        1. 현재 노드 방문 (pop)
        2. 1에서 꺼낸 애의 '인접한 얘들'에 대해
            2-1. 아직 방문하지 않았다면 큐에 삽입 
            
    * 문제마다 '인접한 얘들'의 정의가 달라진다!
    """

    # 상,하,좌,우,북동,북서,남동,남서
    adjacent_r = [-1,+1,0,0,-1,-1,+1,+1]
    adjacent_c = [0,0,-1,+1,+1,-1,+1,-1]

    while queue:  # queue에 뭐라도 들어가 있으면 True
        now = queue.popleft()

        for a in range(8):
            r, c = now[0]+adjacent_r[a], now[1]+adjacent_c[a]

            # 인접한 얘가 범위 내에 존재하는지 확인
            if not ((r in range(h)) and (c in range(w))):
                continue

            # 인접한 얘가 이미 방문 혹은 벽인지 확인
            if pos[r][c] == 0:
                continue
            else:  # 인접한 얘가 '1) 범위 안 2) 아직 방문 안 함' 이므로
                pos[r][c] = 0
                queue.append((r,c))

    return True


while True:
    w,h = map(int,input().split())
    
    # 테스트케이스 입력 끝인지 확인
    if (w,h) == (0,0):
        break

    # 각 테스트케이스의 지도
    pos = [[elem for elem in map(int,input().split())] for _ in range(h)]

    # 섬의 개수를 counting
    island = 0

    for i in range(h):
        for j in range(w):
            if pos[i][j] == 1:
                bfs(i,j)
                island += 1
            # if bfs(i,j):
            #     island += 1

    print(island)












