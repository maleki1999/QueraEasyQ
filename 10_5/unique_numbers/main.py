def cal_xor(numbers):
    xor =0 
    for item in numbers:
        xor = xor^item
    return xor

input()
numbers = [int(i) for i in input().split()]
unique = [item for item in numbers if numbers.count(item)==1]
print(cal_xor(unique))