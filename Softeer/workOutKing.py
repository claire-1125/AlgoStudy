# 자신이 최고라고 생각하는 회원 수 카운팅
howMany = 0

# 회원 수, 친분관계 수
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


for member in range(1, NumMembers+1):
    # 독고다이
    if not adjacentList[member]:
        howMany += 1
    else:
        # 내가 친구들보다 무게를 더 잘 치는가?
        # 같은 경우는 문제 조건에서 언급을 안 했다...
        tempStrengthCompare = []
        for friend in adjacentList[member]:
            tempStrengthCompare.append(strengthPerMember[friend-1])
        if strengthPerMember[member-1] > max(tempStrengthCompare):
            howMany += 1

print(howMany)
