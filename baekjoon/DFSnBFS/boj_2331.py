# 문제 상에서 원하는 수열 항 구하기
def next_num(number):
    return sum(list(int(elem) ** p for elem in str(number)))

def dfs(node, visited, cnt):
    # 이미 방문한 노드인 경우 (여기서 순회 종료!)
    # 0 : False, 자연수 : True

    if visited[node]:
        return visited[node] - 1  # 현재를 재외한 누적 길이

    # 아직 방문하지 않았다면
    visited[node] = cnt
    next_number = next_num(node)
    cnt += 1
    return dfs(next_number,visited,cnt)


a, p = map(int,input().split())

# flag 변수 역할도 하면서 누적 길이를 구하는 배열
# 나올 수 있는 가장 큰 수가 9^5+9^5+9^5+9^5=236196 이므로
visited = [0] * 250000
cnt = 1
print(dfs(a,visited,cnt))