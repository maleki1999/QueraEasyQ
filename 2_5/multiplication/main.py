n = int(input())
arr = list(range(1,n+1))
for i in range(1 , n+1):
    print(' '.join(map(str, [element * i for element in arr])))