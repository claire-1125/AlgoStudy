n = int(input())

for i in range(n,0,-1):
    print(" "*(n-i),end="")
    print("*"*i)

# 또 다른 정답
# for row in range(n,0,-1):
#     for bnk in range(n-row):
#         print(' ',end='')
#     for star in range(row):
#         print('*',end='')
#     print()