"""
hour: range(n+1)에서 3이 포함된 숫자 추출
minute: range(60)에서 3이 포함된 숫자 추출
second: range(60)에서 3이 포함된 숫자 추출

* hour, minute, second의 조합(product)을 이용한다.

Q. 3이 포함되었다는 걸 어떻게 알 수 있을까?
- str로 변환해서 멤버 연산자 이용
"""

from itertools import product

def solution(n):
    cnt = 0

    h = list(range(n+1))
    m = list(range(60))
    s = list(range(60))

    candidates = list(product(h,m,s))
    # [(0, 0, 0), (0, 0, 1), (0, 0, 2), ...]

    for elem in candidates:
        if "3" in f"{elem[0]}{elem[1]}{elem[2]}":
            cnt += 1

    return cnt


N = int(input())

print(solution(N))
