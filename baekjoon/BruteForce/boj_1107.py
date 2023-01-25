target_channel = int(input())  # 이동하려는 채널
# 고장난 버튼 개수와 그 버튼 목록 입력받기
if int(input()) != 0:
    broken_btn = set(map(int,input().split()))
else:
    broken_btn = set()

# 사용할 수 있는 리모컨 버튼
remote_btn = list(set(range(10)) - broken_btn)

current_channel = 100  # 현재 채널

answer = abs(current_channel - target_channel)

"""
<1000001의 의미>
max(N) = 500000

이동하려는 채널의 범위는 500000 이하지만 채널 자체는 무한대이다.

target과 가장 가까운 숫자를 찾을 때, target보다 작은 값은 물론이고 
target보다 큰 값도 찾아줘야 하고 이는 500000 이상도 가능하다.
"""

for i in range(1000001):
    for elem in list(map(int,str(i))):  # 3456 → '3456' → [3,4,5,6]
        if elem not in remote_btn:
            break
    else:
        answer = min(answer,len(str(i))+abs(i-target_channel))

print(answer)