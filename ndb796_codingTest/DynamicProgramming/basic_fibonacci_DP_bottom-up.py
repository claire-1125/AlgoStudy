"""
- 피보나치 수열 : 앞의 두 항의 합으로 이루어진 수열
- 이를 구현하기 위해선... 각 항의 값을 배열에 저장
- 배열의 index는 각 항의 번호(subscript)를 의미함.
"""

# 각 항의 값을 저장하기 위한 배열 (index 0은 사용하지 않는다!)
d = [0] * 101

def fibo(num):
    d[1], d[2] = 1, 1

    for i in range(3,len(d)):
        d[i] = d[i-1] + d[i-2]
    return d[num]

print(fibo(99))