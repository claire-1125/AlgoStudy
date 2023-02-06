# name = "JEROEN"  # 좌우이동횟수 5번
# name = "JAN" # 좌우이동횟수 1번
name = "JAZ" # 좌우이동횟수 1번

# <아이디어>
# 딕셔너리에 각 문자의 양수 인덱스, 음수 인덱스 튜플로 저장해서 비교?

# 26자 (인덱스 ; 0~25)
alphabets = ['A','B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S',
             'T','U','V','W','X','Y','Z']
# 각 문자의 음수 인덱스
minus_index = [alphabets.index(elem) - len(alphabets) for elem in alphabets]

# 조작 횟수
cnt = 0

for elem in name:
    # <좌우이동>
    # 지금 문자가 첫번째가 아닐 것
    # 현재 문자가 A가 아닌 경우
    # 이 두가지가 동시 성립해야 카운팅
    if name.index(elem) != 0 and elem != 'A':
        cnt += 1

    # <상하이동>
    # 현 문자의 양수 인덱스
    plus = abs(alphabets.index(elem))
    # 현 문자의 음수 인덱스
    minus = abs(minus_index[alphabets.index(elem)])
    # 둘 중 최소 횟수로 카운팅
    cnt += min(plus,minus)


print(cnt)