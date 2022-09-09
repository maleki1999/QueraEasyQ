n,k = [int(i) for i in input().split()]
times = [input().split() for _ in range(n)]
states = {}
for time in times:
    key = ','.join(time)
    try:
        states[key] += 1
    except:
        states[key] = 1
for v in states.values():
    if v>k :
        print("NO")
        break
else:
    print("YES")