def check_answer(correct , n_q):
    status = []
    dic = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4
    }
    
    for i in range(n_q):
        answer_sheet = input()
        if '#' in answer_sheet:   
            status.append('T' if answer_sheet.count('#')==1 and answer_sheet.index('#') == dic[correct[i]]-1 else 'F')
    return 3*status.count('T')-status.count('F')

n_q , a , n_sheet = [input() for _ in range(3)]
grades = []
for _ in range(int(n_sheet)): 
    grades.append(check_answer(a ,int(n_q)))
print(*grades , sep='\n')