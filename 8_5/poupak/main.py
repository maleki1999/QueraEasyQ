a , b , x = [int(i) for i in input().split()]
divisor_a = []
divisor_b = []
counter = 0
for i in range(1 ,max(a,b)+1):
    if a % i == 0:
        divisor_a.append(i)
    if b % i == 0:
        divisor_b.append(i)
for i in divisor_a:
    for j in divisor_b:
        if i+j <= x:
            counter+=1
print(counter)