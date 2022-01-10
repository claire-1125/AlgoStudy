"""
여기서의 '인접' 노드 : 상하좌우
범위 안의 위치인지도 확인해야 한다.
BFS이므로 재귀 사용하지 않는다!
"""

from collections import deque

def bfs(r,c):
    if graph[r][c] == 0:
        graph[r][c] = 1
    deq = deque([(r,c)])

    # 왜 자꾸 여기로 오지..????
    print("initial state:", deq)

    # 순서대로 상,하,좌,우
    adjacent_r = [-1,+1,0,0]
    adjacent_c = [0,0,-1,+1]

    while deq:
        v = deq.popleft()
        for i in range(4):
            r,c = v[0] + adjacent_r[i], v[1] + adjacent_c[i]
            if not ((r in range(n)) and (c in range(m))):
                return False
            elif graph[r][c] == 0:
                deq.append((r,c))
                graph[r][c] = 1

    return True

# n * m 크기의 얼음틀
n,m = map(int,input().split())

# [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
graph = [list(map(int,input())) for _ in range(n)]

# 만들 수 있는 아이스크림 수
cnt = 0

for i in range(n):
    for j in range(m):
        if bfs(i,j):
            cnt += 1

print(cnt)