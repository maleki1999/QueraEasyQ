contents = []
while True: 
    n = input()
    if n!="0":
        contents.append(n)
    else:
        break
contents.reverse()
for item in contents: print(item)