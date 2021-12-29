"""
그냥 바로 print(sys.stdin.readline())로 하면
컴퓨터 입장에서 입력이 언제까지인지를 몰라서 끝날수가 없다!

입력 자체가 한 번에 여러 줄!
"""

while True:
    try:
        print(input())
    except EOFError:
        break

