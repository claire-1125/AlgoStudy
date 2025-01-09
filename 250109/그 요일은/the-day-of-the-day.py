m1, d1, m2, d2 = map(int, input().split())
A = input()

# Write your code here!
days_list = [0,31,29,31,30,31,30,31,31,30,31,30,31]
day_map = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

# 2024년 1월 1일부터의 절대 일수 계산
day1 = sum(days_list[:m1])+d1  # 월요일
day2 = sum(days_list[:m2])+d2

# day2 >= day1은 항상 성립

print(((day2-day1) // 7) + 1)