"""
입력 예시
5
R R R U D D

출력 예시
3 4
"""

n = int(input())
route = [elem for elem in input().split()]

# 맨 처음 위치: (1,1)
row, column = 1, 1

move = {'L':(0,-1),'R':(0,+1),'U':(-1,0),'D':(+1,0)}

for elem in route:
    # 이동할 좌표 임시로 계산
    temp_r, temp_c = row + move[elem][0], column + move[elem][1]

    # 이동 전 범위 내인지 확인
    if not (temp_r in range(1,n+1) and temp_c in range(1,n+1)):
        continue

    # 문제 없으면 이동
    row, column = temp_r, temp_c

print(row, column)



