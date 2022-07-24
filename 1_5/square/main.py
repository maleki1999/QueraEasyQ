n = int(input())
row_first = ''.join(["*"]*n)
spaces = ' '*(n-2)
row_center = spaces.join(["*","*"])

for i in range(n):
    if i==0 or i==n-1:
        print(row_first)
    else:
        print(row_center)