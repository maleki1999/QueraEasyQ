n = int(input())
divisor = []
for i in range(1,n):
    if n%i==0:
        divisor.append(i)
print("YES" if sum(divisor)==n else "NO")