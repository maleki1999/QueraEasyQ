numbers = []
for i in range(2):
    numbers.append(input()[::-1])
    
if int(numbers[0])==int(numbers[1]):
    print(numbers[0][::-1]+" = "+numbers[1][::-1])
else:
    print(numbers[1-numbers.index(max(numbers))][::-1]+" < "+numbers[numbers.index(max(numbers))][::-1])