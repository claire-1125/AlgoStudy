# 보급품 수, 신입사원 수, 가방당 최대 무게
n, k, m = map(int, input().split())

# 각 보급품당 무게, 가치
supplies_list = [(map(int, input().split())) for _ in range(n)]
supplies_list_ = supplies_list.copy()

# 가치합 경우의 수 리스트
value_ = []

# 가치 합의 최댓값? 최대 무게 내로 물건 여러 개 담을 수 있다.
for bag in range(k):
    temp_weight, temp_value = 0, 0
    for i in range(n):
        while temp_weight <= m:
            temp_weight += supplies_list[i][0]
            temp_value += supplies_list[i][1]
        




