days = []
for i in range(6):
    if i%2 !=0:
        days.extend(input().split())
    else:
        input()
print(7-len(set(days)))