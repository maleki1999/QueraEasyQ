number = [int(digit) for digit in input()]
while len(number)>1:
    number = [int(digit) for digit in str(sum(number))]
print(number[0])