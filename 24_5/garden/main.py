n , m = [int(i) for i in input().split()]
months = [input() for _ in range(m)]
count = [0]*n

for month in months:
    for j in range(n):
        if month[j]=='W':
            count[j] += 1
            
for i in range(len(count)):
    count[i]='B' if count[i] % 2 == 0 else 'F'
    
print(''.join(count))