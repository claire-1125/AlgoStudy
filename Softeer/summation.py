result = [sum(map(int,input().split())) for _ in range(int(input()))]

for i in range(len(result)):
    print(f'Case #{i+1}: {result[i]}')