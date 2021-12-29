"""
테스트 케이스 개수가 가변적이라는 게 포인트!

<알고리즘>
입력이 들어오면 계산, 입력이 더이상 들어오지 않으면 종료
"""

while True:
    try:
        print(sum([elem for elem in map(int, input().split())]))
    except:
        break
