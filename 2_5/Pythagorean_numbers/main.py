contents = []
count = 0
while count<3: 
    contents.append(int(input()))
    count+=1
max_list = contents.pop(contents.index(max(contents)))
sum_list =0 
for n in contents:
    sum_list+=n**2 
print("YES" if max_list**2 == sum_list else "NO" )