from math import gcd
def cal_lcm(list):
    lcm = list[0]
    for i in list[1:]:
        lcm = int(lcm*i/gcd(lcm, i))
    return lcm

n = int(input())
numbers = [int(input()) for i in range(n)]
print((cal_lcm(numbers)+1)%30)