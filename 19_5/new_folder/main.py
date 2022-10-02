n = int(input())
names = [input() for _ in range(n)]
freq = {}
for i in names: freq[i]=1 

for i in range(len(names)):
    if names[i] in names[:i]:
        freq[names[i]]+=1
        names[i] = f"{names[i]} ({freq[names[i]]-1})"
    temp = "', '".join(sorted(names[:i+1]))
    print(f"'{temp}'")