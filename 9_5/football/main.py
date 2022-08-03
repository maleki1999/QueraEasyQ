n = input()
contents  = [input().split() for _ in range(int(n))]
result = []
for game in contents:
    a ,b, c ,d =[int(i) for i in game]
    if a+c > b+d:
        result.append("perspolis")
    elif a+c < b+d:
        result.append("esteghlal")
    else:
        if b<c :
            result.append("perspolis")
        elif b>c : 
            result.append("esteghlal")
        else :
            result.append("penalty")
print(*result , sep='\n')