n = int(input())

for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*i)

# 또 다른 정답
# for i in range(n):
#     for j in range(n-(i+1)):
#         print(' ',end='')
#     for k in range(i+1):
#         print('*',end='')
#     print()