r , c = [int(item) for item in input().split()]
if c>0 and c<=10 :
    print("Right",10 - r + 1,c)
else :
    print("Left",10 - r + 1,20 - c + 1)