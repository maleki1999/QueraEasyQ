n = int(input())
names = [input() for _ in range(n)]
participants = {}
for item in names : participants[item] = 0
    
for i in range(n):
    giver = input()
    price , number = [int(i) for i in input().split()]
    
    if number!=0 :
       
        value_gift = price//number
        for num in range(number):
            participants[input()]+=value_gift
        participants[giver]+=(price%number)-price
        
    else:
        participants[giver]+=price
    
for k,v in participants.items():
    print(k,v)