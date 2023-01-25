# (1월 기준) 각 index가 7로 나눈 나머지를 의미한다.
dayList = ['SUN','MON','TUE','WED','THU','FRI','SAT']

# 각 달마다 끝나는 날짜를 적어놓았다.
endNumList = [31,28,31,30,31,30,31,31,30,31,30,31]

# 7로 나눈 나머지
# 31 = 7 * 4 ... 3
# 30 = 7 * 4 ... 2
# 28 = 7 * 4 ... 0

# 이전 달의 시작 요일로부터 얼마나 밀려 시작하는가?
# 이는 이전 달의 날짜수에 의해 결정된다.
here = ['x',3,0,3,2,3,2,3,3,2,3,2]

# 각 달마다 시작하는 요일?
startDayList = ['MON','THU','THU','SUN','TUE','FRI','SUN','WED','SAT','']

# sequential하게 각 달의 시작요일을 계산하는 함수
# 이런 순환이 가변적으로 증가하는 리스트에는 적용이 안 되었던 걸로 기억나는데...;;
for i in range(12):
    startDayList.append(dayList[dayList.index(startDayList[i]) + here[i+1]])
    print(f"present index : {i}")

print(startDayList)

# def solution(day, he):
#     for elem in he:
#         elem

# 각 달의 시작요일을 알게된 이후
# 입력으로 들어온 달에 따라 정답을 출력시킨다.

# 입력 : 3 14, 출력 : WED
