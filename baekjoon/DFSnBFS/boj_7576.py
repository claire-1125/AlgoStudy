from collections import deque

# m : 가로의 크기, n : 세로의 크기
m,n = map(int,input().split())

# 각 토마토들의 정보
tomatoes = [[elem for elem in map(int,input().split())] for _ in range(n)]

def bfs(r,c):
    dayCnt = 0  # 일수 count

    # 초기 설정 → 변경 필요....
    # if tomatoes[r][c] == 1:
    #     tomatoes[r][c] = -1
    queue = deque([(r,c)])
    print("initial queue:",queue)

    while queue:
        v = queue.popleft()
        print("now here:",v)

        # 상,하,좌,우
        adjacent_r = [-1,+1,0,0]
        adjacent_c = [0,0,-1,+1]

        for i in range(4):
            r,c = v[0] + adjacent_r[i], v[1] + adjacent_c[i]
            print("adjacent:","(",r,",",c,")")

            # 범위 내에 존재하는지 확인
            if not ((r in range(n)) and (c in range(m))):
                # return False
                continue

            if tomatoes[r][c] == 0:  # 근처에 있고 아직 익지 않은 상태라면
                queue.append((r,c))
                tomatoes[r][c] = 1

        print("after adding adjacent nodes:",queue)
        # 날짜 수 세는 순간을 변경해야 할 것 같다....
        dayCnt += 1  # 한 level이 깊어질 때 count + 1
        print("day:",dayCnt)

    return dayCnt


# 토마토 상자의 모든 위치를 순회
for i in range(n):
    for j in range(m):
        # 1인 지역에서 순회 시작!
        if tomatoes[i][j] == 1:
            print("=================================")
            print("start with (",i,",",j,")")
            # 시작은 제대로 한다.
            result = bfs(i,j)

print("FINAL:",result)