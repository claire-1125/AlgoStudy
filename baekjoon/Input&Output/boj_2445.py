"""
최대 2*n개의 별

[공백]
8
6
4
2
0
2
4
6
8
"""

n = int(input())

# increasing part
for i in range(1,n+1):
    print("*"*i + " "*(2*(n-i)) + "*"*i)

# decreasing part
for i in range(n-1,0,-1):
    print("*"*i + " "*(2*(n-i)) + "*"*i)