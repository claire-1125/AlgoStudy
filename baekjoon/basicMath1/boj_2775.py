t = int(input())

# [(1,3),(2,3)]
living_pos = [tuple((int(input()),int(input()))) for _ in range(t)]

# 0층 거주하는 사람들 설정
# [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],[]]
apartment = [[i for i in range(1,15)]]

# 1층부터는 공식 적용
for i in range(1,15):
    apartment.append([])
    for j in range(1,15):
        apartment[i].append(sum(apartment[i-1][:j]))

# 출력
for elem in living_pos:
    print(apartment[elem[0]][elem[1]-1])