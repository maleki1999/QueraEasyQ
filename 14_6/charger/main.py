n,x,y = [int(i) for i in input().split()]
charge = [int(i) for i in input().split()]
dis = 0
m = charge.pop(charge.index(min(charge)))
for ch in charge:
    dis += 100-ch
print("YES" if (m//x)*y >= dis else "NO")