# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 
# 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.

# hour: 0~n
# minute: 0~59
# second: 0~59

# 전체 조합 - 3이 하나도 안 들어간 경우 (차집합)

import re

n = int(input())

hour_, minute_, second_ = list(range(n+1)), list(range(60)), list(range(60))

# 3이 안 들어간 경우: str 만들고 3 존재하나 찾기
hour_= [str(elem) for elem in hour_]
minute_ = [str(elem) for elem in minute_]
second_= [str(elem) for elem in second_]

hour_not = [elem for elem in hour_ if not re.search('3', elem)]
minute_not = [elem for elem in minute_ if not re.search('3', elem)]
second_not = [elem for elem in second_ if not re.search('3', elem)]


# 전체 경우의 수
whole = len(hour_) * len(minute_) * len(second_)


# 3이 안 들어간 경우의 수
not_3 = len(hour_not) * len(minute_not) * len(second_not)

print(whole - not_3)


