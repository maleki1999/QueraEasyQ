n = int(input())
capacity = [int(i) for i in input().split()]
buy = 0
saved = 0
for c in capacity:
    if c < 0:
        saved -= c
    else:
        if saved < c :
            buy += c - saved
            saved = 0
        else :
            saved -= c
print(buy)