a , b , l = [int(item) for item in input().split()]
last_time = 0
for i in range(l):
    if i%2==0:
        last_time+=a
    else:
        last_time+=b
print(last_time)