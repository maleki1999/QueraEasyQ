n = int(input())
numbers = [int(i) for i in input().split()]
sort_numbers = sorted(numbers)
final = []
for i in range(len(numbers)):
    if i%2 == 0:
        final.append(sort_numbers[-1])
        sort_numbers.pop(-1)
    else:
        final.append(sort_numbers[0])
        sort_numbers.pop(0)
print(*final)