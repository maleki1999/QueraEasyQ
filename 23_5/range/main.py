n = int(input())
contents = [input() for _ in range(n)]
ranges = []

for r in contents:
    a , b = [int(i) for i in r.split()]
    ranges.extend(list(range(a,b)))
    
given_range = list(range(int(input()),int(input())+1))

    
print("true" if all(elem in ranges for elem in given_range) else "false")