n = int(input())

# 정사각형 형태의 지도 정보
pos = [[i for i in map(int,input())] for _ in range(n)]

inner_cnt = 0
def dfs(r,c):
    # 범위 내에 존재하는지 확인
    if not ((r in range(n)) and (c in range(n))):
        return False

    """
    DFS는 '재귀'하므로 한 단지 내에 속하는 집의 개수를 새는 변수인
    inner_cnt는 함수 외부에서 초기화해줘야 한다.
    """
    global inner_cnt

    # 현재 노드 방문 처리 (pos 그 자체를 visited 배열로도 사용)
    if pos[r][c] == 1:
        pos[r][c] = 0
        inner_cnt += 1  # 한 단지 내 속하는 집 개수 count

        dfs(r-1,c)  # 상
        dfs(r+1,c)  # 하
        dfs(r,c-1)  # 좌
        dfs(r,c+1)  # 우

        return inner_cnt
    else:
        return False

cnt = 0  # 총 단지 수
result = list()  # 각 단지 내 집의 개수를 저장할 배열
for i in range(n):
    for j in range(n):
        temp_result = dfs(i,j)  # return 값이 False 혹은 정수 이므로 따로 받아야 한다.
        if temp_result:
            inner_cnt = 0  # 한 단지 내에 대한 순회가 끝났으므로 초기화
            cnt += 1
            result.append(temp_result)

print(cnt)
for elem in sorted(result):
    print(elem)