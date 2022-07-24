numbers = str(input()).split()
if int(numbers[0])+int(numbers[1])+int(numbers[2]) == 180 and str(0) not in numbers:
    print("Yes")
else:
    print("No")