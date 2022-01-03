"""
<할 수 있는 연산 세 가지>
- (3의 배수일 경우) 3으로 나누기
- (2의 배수일 경우) 2로 나누기
- 1을 빼기

<알고리즘>
빠르게 숫자를 작게 만드는 것이 핵심!
즉, 현재 수 X와 가장 근접한 2의 배수 혹은 3의 배수로 만든 뒤 2 혹은 3으로 나눈다.

<의문점>
- 2의 배수기도 하고 3의 배수기도 한 경우는 어떻게 할 것인가? (e.g. 6)
- 현재 수가 2/3으로 나눠도 되지만 일단 여기서 바로 나누지 않고 -1을 몇 번해서 그 뒤에
나누는 게 더 횟수를 줄일 수 있는 경우는 어떻게 할 것인가? (e.g. 10)
"""

n = int(input())
cnt = 0

while n > 1:
    # if n % 2 == 0 or n % 3 == 0:
    if n % 2 == 0:
        n //= 2
        print("first, n:",n)
        cnt += 1
    elif n % 3 == 0:
        n //= 3
        print("second, n:",n)
        cnt += 1
    elif n % 2 == 0 and n % 3 == 0:
        n //= 3
        print("third, n:",n)
        cnt += 1
    else:
        n -= 1
        print("fourth, n:",n)
        cnt += 1

print("result:",cnt)