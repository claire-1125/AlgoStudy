change = []

# 입력 받기: 숫자를 화면에 표현하는 문제이므로 str로 취급 (연산X)
# change = [['1','2'],['9881','10724']]
for _ in range(int(input())):
    change.append(list(map(str,input().split())))


"""
 -2
|1 |3
 -4
|5 |7
 -6

0(10): 000 0000(2)
1(10): 100 0100(2)
2(10): 011 1110(2)
3(10): 110 1110(2)
4(10): 100 1101(2)
5(10): 110 1011(2)
6(10): 111 1011(2)
7(10): 100 0111(2)
8(10): 111 1111(2)
9(10): 110 1111(2)
"""

# 0~9를 bit로써 정의 (실제 이진수가 아니라 각 형광등에 넘버링해서 그걸 이진수처럼 표현함.)
lights = {
    '0':"1110111", '1':"1000100", '2':"0111110",
    '3':"1101110", '4':"1001101", '5':"1101011",
    '6':"1111011", '7':"1000111", '8':"1111111",
    '9':"1101111"
}

result = []

for elem in change:
    cnt = 0  # 토글 스위칭 횟수 카운팅
    a,b = elem[0], elem[1]
    len_a, len_b = len(a), len(b)
    len_diff = abs(len_a - len_b)

    if len_a > len_b:
        for i in a[:len_diff]:
            # bit 표현 내 1의 개수 카운팅
            cnt += lights[i].count("1")
        # 나머지 자리에 대해 교환
        for a_, b_ in zip(a[len_diff:], b):
            for a__, b__ in zip(lights[a],lights[b]):
                if a__ != b__:
                    cnt += 1

    elif len_a < len_b:
        for i in b[:len_diff]:
            cnt += lights[i].count("1")
        # 나머지 자리에 대한 교환
        for a_, b_ in zip(a, b[len_diff:]):
            for a__, b__ in zip(lights[a],lights[b]):
                if a__ != b__:
                    cnt += 1
    else:
        for a_, b_ in zip(a, b):
            for a__, b__ in zip(lights[a],lights[b]):
                if a__ != b__:
                    cnt += 1


    result.append(cnt)


# 결과 출력
for elem in result:
    print(elem)