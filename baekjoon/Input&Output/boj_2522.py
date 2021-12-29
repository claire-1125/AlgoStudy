"""
최대 별 3개
"""

n = int(input())

# increasing part
for i in range(1,n+1):
    print(" "*(n-i) + "*"*i)

# decreasing part
for j in range(n-1,0,-1):
    print(" " *(n-j) + "*"*j)