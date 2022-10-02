import numpy
s = input()
m = min(s)
string = numpy.array(list(s))
indices = numpy.where(string == m)[0]
choice = s[indices[0]:]+s[:indices[0]]
for i in indices[1:]:
    if s[i:]+s[:i] < choice:
        choice = s[i:]+s[:i]
print(choice)