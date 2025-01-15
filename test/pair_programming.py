# i번째 & n-i+1번째 → 인덱스: i-1 & n-i
# 둘의 퍼포먼스 합계가 일정값 이상
# 직원수가 홀수인 경우 가운데 사람은 페어 대상 아님
# 가능한 페어 수?

# 의문점: 직원마다 모두 퍼포먼스 값이 다른가?
# 문제에서 명시되지는 않았으나, 히든 테케에서 틀렸다 할 것 같다.

num_of_personnel, threshold = map(int, input().split())
personnel_list = list(map(int, input().split()))

pair_cnt = 0


for i in range(num_of_personnel//2):
    if personnel_list[i] + personnel_list[num_of_personnel-i-1] >= threshold:
        pair_cnt += 1

print(pair_cnt)