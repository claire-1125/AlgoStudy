"""
<선택정렬>
맨 앞의 수와 최소값을 서로 change
복잡도 : O(n^2)
max(), min() 함수를 쓰며 동시에 swap(정확히는 unpacking)할 수는 없다.
따라서 최소값(최대값)을 순회하며 직접 구해야 한다.
최소값을 기준으로 진행할 경우 앞에서부터 freeze된다.
실제로 원소 위치를 바꿔야 한다. 그렇다면 index로 접근해야 한다!
"""

"""
[필요한 순회 변수 2개]
- 전체를 순회하는 i (각 순회당 맨 왼쪽(오른쪽) 값이 된다.)
- i를 제외한 나머지 범위에서 최소값/최대값을 찾는 j
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    temp_min = i
    for j in range(i+1,len(array)):
        if array[temp_min] > array[j]:
            array[temp_min], array[j] = array[j], array[temp_min]

print(array)
