# 나무의 수, 가져가려는 나무의 길이
n, m = map(int,input().split())

# 주어진 나무들 높이
trees = list(map(int,input().split()))

left, right = 1, max(trees)

while left <= right:
    middle = (left + right) // 2

    result = 0  # 가져갈 나무 길이
    for tree in trees:
        temp = tree - middle
        if temp > 0:
            result += temp


    if result < m:
        right = middle - 1
    else:
        left = middle + 1

print(right)