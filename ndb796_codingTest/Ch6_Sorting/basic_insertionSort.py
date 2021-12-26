"""
<삽입정렬>
LOO(left out of order) 밀어내는 정렬
복잡도 : O(n^2)
LOO 하나가 아니고 '모든' LOO를 밀어내야 한다는 게 핵심
"""

"""
[순회 시 필요한 변수 2개]
- 전체를 순회하며 기준이 되는 i
- 기준 i에서 왼편에 존재하는 원소들 j : i에서부터 '왼쪽방향'으로 순회하는 것이 포인트!
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):  # scan 범위 : 리스트 전체
    for j in range(i, 0, -1): # LOO(left out of order) 확인
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break  # inner for문 탈출

print(array)