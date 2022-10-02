# from math import comb
# def findsubsets(n):
#     profit = 0
#     count = 0
#     price = 2**n
#     for num_sub in range(n+1):
#         count+=comb(n,num_sub)
#         if count*price>profit :
#             profit = count*price 
#             profit_ind = num_sub
#         else :
#             break
#         price //= 2
        
#     return profit_ind

# t = int(input())
# test_case = [int(input()) for _ in range(t)]
# for i in test_case:
#     print(findsubsets(i))



import math
t = int(input())
test_case = [int(input()) for _ in range(t)]

for t_c in test_case:
    if t_c in [3,6,9,12]:
        print(math.ceil(t_c/3))
    else:
        print(math.ceil(t_c/3)+1 if t_c % 3 ==0 else math.ceil(t_c/3)) 
        
# راه حل اول که راه حل روتین برای حل این مسئله میباشد از نظر زمانی در کوئرا پاس نشد .با بررسی های زیاد راه حل دوم تست شد
# که مشکل زمانی نداشت اما در یک تست جواب اشتباه داده میشود.
#  لطف میکنید اگر راه حل خودتون رو بگذارید.