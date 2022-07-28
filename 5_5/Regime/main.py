label = ''.join(sorted(input()))
unallowed = ["RRR","RRYY"]
flag = False
for item in unallowed:
    if item in label or "G" not in label:
        flag = True
        break
print("rahat baash" if flag == False else "nakhor lite")