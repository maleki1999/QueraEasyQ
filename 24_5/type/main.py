from itertools import groupby
def compress(s):
    groups = groupby(s)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    return "".join(f"{label}{count}" if count>1 else f"{label}" for label, count in result )

def extend(s):
    a = s
    for i in range(len(s)):
        if s[i].isdigit():
            a = a.replace(s[i],s[i-1]*(int(s[i])-1),1)
    return a


n = int(input())
contents = [[input(),input()] for _ in range(n)]

for c in contents:
    if c[0] == '1':
        print(compress(c[1]))
    elif c[0]=='2' :
        print(extend(c[1]))
        
# پس از صرف زمان بسیااااار زیاد موفق به کسب نمره کامل این سوال نشدم