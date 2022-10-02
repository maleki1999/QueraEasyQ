from collections import Counter

def compressed(s):
    dic = Counter(s)
    comp = sorted(''.join(list(dic.keys())+[str(v) for v in dic.values() if v!=1]))
    if comp == s:
        return comp
    else:
        return compressed(comp)
    
print(''.join(compressed(input())))