n = int(input())
list1 = sorted(list(map(int,input().split())))
print(list1[0],list1[n-1])

# min, max, 정렬 안 쓰는 버전
# _ = input()
# numList = list(map(int,input().split()))
#
# cntMin, cntMax = 1000000, -1000000
#
# for elem in numList:
#     if cntMin >= elem:
#         cntMin = elem
#     if cntMax <= elem:
#         cntMax = elem
#
# print(cntMin, cntMax)
