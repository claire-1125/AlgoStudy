cnt = 0

def dfs(r, c):
    global cnt

    # 예외처리
    if r < 0 or r >= n or c < 0 or c >= n:
        return False

    # 괴물이 없는 곳이 1이고 이곳을 지나갈 수 있으므로
    if graph[r][c] == 1:
        graph[r][c] = 0

        if r == 0 and c == 0:
            cnt += 1
            dfs(r + 1, c)
            dfs(r, c + 1)

        elif r == n - 1 and c == m - 1:
            cnt += 1
        else:
            cnt += 1

            # dfs이므로 재귀!
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            # cnt += 1

    return cnt


# n*m 차원 받기
n, m = map(int, input().split())

# 미로 정보 입력 받기
graph = [list(map(int, input())) for _ in range(n)]

print(dfs(0, 0))