from math import pow

a, p = map(int,input().split())
d = [0] * 30
d[0] = a

for i in range(1,30):
    temp_result = 0
    for elem in str(d[i-1]):
        temp_result += pow(int(elem),p)
    d[i] = int(temp_result)
    continue

