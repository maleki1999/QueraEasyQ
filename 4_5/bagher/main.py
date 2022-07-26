index = []
for i in range(5):
    s = input()
    if "MOLANA" in s or "HAFEZ" in s:
        index.append(i+1)
print(' '.join(str(i) for i in index) if len(index)!=0 else 'NOT FOUND!')