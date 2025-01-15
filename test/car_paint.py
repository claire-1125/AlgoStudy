# 

# 도장 공정의 총 횟수?

_, paint_cnt = map(int, input().split())
car_or_not = list(map(int, input().split()))

cnt = 0

for _ in range(paint_cnt):
    start, end = map(int, input().split())
    cnt += sum(car_or_not[start-1:end])

print(cnt)

