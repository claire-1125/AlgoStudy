"""
맨 마지막 줄은 따로 출력시키자
"""

n = int(input())

for i in range(1,n+1):
    if i == 1:
        print(" "*(n-i) + "*")
    elif i == n:
        print("*"*(2*i-1))
    else:
        print(" "*(n-i) + "*" + " "*(2*i-3) + "*")
