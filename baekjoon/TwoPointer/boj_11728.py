n,m = map(int,input().split())

a = list(elem for elem in map(int,input().split()))
b = list(elem for elem in map(int,input().split()))

a.sort(reverse=True)  # O(NlogN)
b.sort(reverse=True)

result = []

# 각 리스트가 비었는지 여부 체크
while a and b:
    if a[-1] > b[-1]:
        result.append(b.pop())  # 둘 다 O(1)
    elif a[-1] < b[-1]:
        result.append(a.pop())  # 둘 다 O(1)
    else:
        result.extend((a.pop(),b.pop()))  # O(N)


## 둘 중 하나 이상이 빈 상태
# a가 빈 상태
if not a:
    result.extend(sorted(b))  # O(NlogN) / O(N)

# b가 빈 상태
if not b:
    result.extend(sorted(a))

for elem in result:
    print(elem,end=" ")
# print(*result)