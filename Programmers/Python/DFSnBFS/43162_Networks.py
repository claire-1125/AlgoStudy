from collections import deque

# 하나의 네트워크에 대해서만 순회 진행
def bfs(n,computers,visited, computer):
    # 초기 세팅
    queue = deque([computer])
    visited[computer] = 1

    while queue:
        now = queue.popleft()
        visited[now] = 1

        for i in range(n):
            if now != i and computers[now][i]:
                if not visited[i]:
                    queue.append(i)


def solution(n, computers):
    answer = 0  # 네트워크 개수 counting

    # 방문 여부 확인
    visited = [0 for _ in range(n)]

    # 각 컴퓨터(노드)에 대해서 순회: 즉, 네트워크 별로 BFS 진행
    for computer in range(n):
        if not visited[computer]:
            bfs(n, computers, visited, computer)
            answer += 1

    return answer

# 예상 출력: 2
N = 3
Computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

# 예상 출력: 1
# N = 3
# Computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution(N,Computers))