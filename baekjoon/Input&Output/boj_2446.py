"""
[별] 9 7 5 3 1 3 5 7 9
[공백] 0 1 2 3 4 3 2 1 0
"""
n = int(input())

# decreasing part
for i in range(n,0,-1):
    print(" "*(n-i) + "*"*(2*i-1))

# increasing part
for j in range(2,n+1):
    print(" "*(n-j) + "*"*(2*j-1))

