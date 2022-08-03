def check_answer(correct , answer_sheet):
    if '#' not in answer_sheet:
        return 'N'
    elif answer_sheet.count('#')==1 and answer_sheet.index('#') == correct-1:
        return 'T'
    else : return 'F'
    
contents = [input() for _ in range(3)]
dic = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4
}
status = []
grades = []
for i in range(int(contents[2])):
    for j in range(int(contents[0])):
        status.append(check_answer(dic[contents[1][j]],input())) 
        
    grades.append(3*status.count('T')-status.count('F'))
    status = []
print(*grades , sep='\n')