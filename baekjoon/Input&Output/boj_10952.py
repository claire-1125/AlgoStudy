while True:
    a,b = map(int,input().split())
    if not (a and b):
        break
    else:
        print(a+b)