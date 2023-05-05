# 문제 링크: https://softeer.ai/practice/info.do?idx=1&eid=389

_, NumUnit = map(int,input().split())
students = list(map(int, input().split()))
result = []

for _ in range(NumUnit):
    l, r = map(int,input().split())
    evalResult = sum(students[l - 1:r]) / len(students[l - 1:r])
    # 소숫점 셋째자리에서 반올림
    # 자리공간 무조건 채워서 출력 i.e.) 50.0(X) 50.00(O)
    result.append(f"{round(evalResult,2):.2f}")

for elem in result:
    print(elem)