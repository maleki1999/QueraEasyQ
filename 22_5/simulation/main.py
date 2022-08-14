n = int(input())
expressions = [input() for _ in range(n)]
for exp in expressions:
    
    if ':=' in exp:
        exec(exp.replace(':=','='))
        
    elif 'print' in exp:
        exp = exp.split()
        exec(f'{exp[0]}({exp[1]})')