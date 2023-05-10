# 자신이 최고라고 생각하는 회원 수 카운팅
howMany = 0

# def dfs(graph, node, visited):
#     # 현재 노드 방문
#     visited[node] = 1
#
#     # global howMany
#     # howMany += 1
#
#     # 인접 리스트를 기준으로 재귀적 방문
#     for elem in graph[node]:
#         if not visited[elem]:
#             dfs(graph, elem, visited)

NumMembers, NumIntimacy = map(int, input().split())

# 각 회원별 들 수 있는 역기 무게
# [1, 2, 3, 4, 5]
strengthPerMember = list(map(int,input().split()))


# 친분관계 리스트 (인접 리스트) 구성
# [[],[3],[4,5],[1],[2],[2]]
adjacentList = [[] for _ in range(NumMembers+1)]

for _ in range(NumIntimacy):
    one, two = map(int, input().split())
    adjacentList[one].append(two)
    adjacentList[two].append(one)

# # 각 회원 순회 여부
# Visited = [0]*(NumMembers+1)

# # 얘를 각 그래프마다 호출
# dfs(adjacentList, 1, Visited)


# [[],[2],[1,3],[2,4],[3],[]]
"""
1번, 3번
각 인접 리스트 원소에서 내가 친구들보다 크냐? 여부 확인
"""

for member in range(1,NumMembers+1):
    # 독고다이
    if not adjacentList[member]:
        pass

    # 내가 친구들보다 무게를 더 잘 치는가?
    # 같은 경우는 문제 조건에서 언급을 안 했다...
    if strengthPerMember[member-1] > max(adjacentList[member]):
        pass
        howMany += 1

print(howMany)
