"""
- 8*8 정원
- L자 형태로 이동
  1) 수평 2칸 + 수직 1칸
  2) 수직 2칸 + 수평 1칸
- 정원 밖으로 나갈 수 없다.
- 나이트가 이동할 수 있는 경우의 수?

- 시작 위치 "a1" : "(column)(row)"
  - column : [a,b,c,d,e,f,g,h] → 내부적으로는 숫자로 변환해서 다루자
  - row : [1,2,3,4,5,6,7,8]
  

"""


def solution(status):
    columnDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}
    column = list(range(1,9))
    row = list(range(1,9))


    # 시작 위치 (변환 완료)
    nowRow = int(status[1])
    nowCol = columnDict[status[0]]


    # 움직임 정의 (총 8가지)
    dr = [-1,+1,-1,+1,+2,+2,-2,-2]
    dc = [-2,-2,+2,+2,-1,+1,-1,+1]

    cnt = 0

    for i in range(8):
        tempRow = nowRow + dr[i]
        tempCol = nowCol + dc[i]
        
        # 정원 내인지 확인
        if not (tempRow in row and tempCol in column):
            continue

        # 문제 없으면 카운팅
        cnt += 1

    return cnt


Status = input()
print(solution(Status))