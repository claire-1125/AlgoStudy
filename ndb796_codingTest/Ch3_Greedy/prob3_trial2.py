from collections import deque

num_list = deque([int(elem) for elem in input()])

while len(num_list) >= 2:
    first, second = num_list.popleft(), num_list.popleft()
    num_list.append(max(first + second, first * second))

print(num_list.pop())