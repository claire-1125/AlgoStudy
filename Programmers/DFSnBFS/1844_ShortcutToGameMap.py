from collections import deque

def solution(maps):
    answer = bfs(maps,0,0)
    return answer

def bfs(maps,r,c):
    R, C = len(maps), len(maps[0])

    # 초기 세팅
    queue = deque([(r,c)])  # queue에 넣기

    # 상하좌우 움직임
    dr = [-1,+1,0,0]
    dc = [0,0,-1,+1]

    # 큐가 비기 전까지 계속 실행
    while queue:
        # 큐에서 꺼낸다.
        row, column = queue.popleft()
        print(f'I just visited ({row},{column}).')

        # 현재 꺼낸 것의 인접한 것에 대해
        for i in range(4):
            # 인접한 것의 좌표
            now_row = row + dr[i]
            now_column = column + dc[i]

            # 예외처리: 지도 범위 내인가?
            if not ((now_row in range(R)) and (now_column in range(C))):
                continue

            # 예외처리: 벽인가?
            if not maps[row][column]:
                continue

            # 인접한 노드가 아직 방문한 게 아니라면
            if maps[now_row][now_column]:
                # 방문했다고 처리
                maps[now_row][now_column] = maps[row][column] + 1

                # queue에 추가
                queue.append((now_row, now_column))

    # 상대 진영에 도착하지 못하는 경우
    if maps[R-1][C-1]:
        return -1
    else:
        return maps[R-1][C-1]

Maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]]

print(solution(Maps))