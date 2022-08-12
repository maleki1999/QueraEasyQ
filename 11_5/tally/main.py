import math
n,m,a,b = [int(input()) for _ in range(4)]
print(1 if a==n or b==m else math.ceil(min(n,m)/max(a,b)))