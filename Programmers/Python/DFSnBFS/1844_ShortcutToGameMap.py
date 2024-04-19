from collections import deque

def solution(maps):
    R, C = len(maps), len(maps[0])

    # 상하좌우 움직임
    dr = [-1, +1, 0, 0]
    dc = [0, 0, -1, +1]

    # 초기 세팅
    queue = deque([(0,0)])  # queue에 넣기

    # 큐가 비기 전까지 계속 실행
    while queue:
        # 큐에서 꺼낸다.
        row, column = queue.popleft()

        # 현재 꺼낸 것의 인접한 것에 대해
        for i in range(4):
            # 인접한 것의 좌표
            now_row, now_column = row + dr[i], column + dc[i]

            # 예외처리: 지도 범위 내인가?
            if not ((now_row in range(R)) and (now_column in range(C))):
                continue

            # 예외처리: 벽인가?
            if not maps[now_row][now_column]:
                continue

            # 길인 지점에서는 방문한 곳은 1보다 큰 수, 미방문 지점은 1이다.
            # 만약 if maps[now_row][now_column]:이라고 작성하면
            # 방문한 곳도 다시 방문해서 무한반복에 빠진다.
            if maps[now_row][now_column] == 1:
                # 방문했다고 처리
                maps[now_row][now_column] = maps[row][column] + 1

                # queue에 추가
                queue.append((now_row, now_column))


    # 상대 진영에 도착하지 못하는 경우
    if maps[R-1][C-1] == 1:
        return -1
    else:
        return maps[R-1][C-1]


Maps = [[1,0,1,1,1],
        [1,0,1,0,1],
        [1,0,1,1,1],
        [1,1,1,0,1],
        [0,0,0,0,1]]

print(solution(Maps))