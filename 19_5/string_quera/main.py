def s(n):
    if n == 1:
        return 1
    else:
        return (int(s(n-1))*2 + sum(int(d) for d in str(n))) % ((10**9)+7)
n = int(input())
print(s(n))



# def s(n):
#     if n == 1:
#         return "1"
#     else:
#         return s(n-1)+str(n)+s(n-1)
# n = int(input())
# print(sum(int(d) for d in s(n)) % ((10**9)+7))
#این راه حل که راه حل اصلی مسئله است ، از نظر زمانی بهینه نیست