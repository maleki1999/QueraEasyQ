import re
def occurrences(text, sub):
    return len(re.findall('(?={0})'.format(re.escape(sub)), text))

string = input()
expressions = []
value = 0

while True:
    expressions.append(input())
    if expressions[-1] == 'Is it right or not?':
        break
        
for exp in expressions:
    exp = exp.split()
    
    if exp[0] == "copy":
        string = f'{exp[1]*int(exp[2])}{string[len(exp[1]*int(exp[2])):]}'
        
    elif exp[0] == "compare":
        if exp[1] == string:
            value+=1
            
    elif exp[0] == "substr":
        if occurrences(string, exp[1]) == int(exp[2]):
            value+=1
            
    elif exp[0] == "attach":
        if string.count(f'{exp[1]}{exp[3]}') == int(exp[2]):
            value+=1
     
    elif exp[0] == "length":
        if len(string) == int(exp[1]):
            value+=1
        
    else:
        print("Eyval" if value >= (len(expressions)-1)/2 else "HeifShod")