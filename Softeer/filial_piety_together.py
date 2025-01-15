# 문제 링크: https://softeer.ai/practice/7727

# n*n 크기의 땅, m명
# 땅의 각 칸당 수확 가능한 열매수
# 인접 노드: 상하좌우 → 1초에 한 칸씩 이동
# 열매를 수확하는 데 걸리는 시간은 없다. (0초)
# 이미 방문한 곳을 갈 수는 있으나 수확은 안 됨. (이동시간만 고려하기)
# m명의 친구들이 3초 동안(=3번 이동) '최대로' 얻을 수 있는 열매 수확량 총합?

# DFS/BFS?

# 동시 출발 아님??????????
# 한 순간에는 한 명만 이동하는 것 같다.
# 한 친구 다 이동한 뒤에 그 다음 친구 가는 방식

# 다른 사람 풀이: https://velog.io/@lookin_min/Softeer-%ED%95%A8%EA%BB%98%ED%95%98%EB%8A%94-%ED%9A%A8%EB%8F%84Python


n,m = map(int, input().split())
orchard = [list(map(int, input().split())) for _ in range(n)]
start_pos = [list(map(int, input().split())) for _ in range(m)]
start_pos = [(elem[0]-1, elem[1]-1) for elem in start_pos]


# 방문여부 리스트
visited = [[0]*n for _ in range(n)]


# DFS
def dfs(r,c,path,route):
    # 모든 가능한 경로 다 저장했는지 확인하기
    

    # 현재 노드를 경로에 저장
    path.append((dr,dc))

    # 인접한 노드 임시로 좌표 만들기
    dr, dc = [-1,+1,0,0], [0,0,-1,+1]

    for i in range(len(dr)):
        new_r, new_c = r+dr[i], c+dc[i] 

        # 인접한 노드가 밭 범위 내에 존재하는지 확인
        if not (new_r in range(n) and new_c in range(n)):
            continue

        path.append((new_r,new_c))
        dfs(new_r, new_c, path, route)

    # 현재 경로 저장
        

for person in start_pos:
    for i in range(3):
        dfs(person[0], person[1])


# 가능한 모든 경로 조합에서 최대값 찾기
# 친구 순서 고려하기 (누가 먼저 이동할지)



