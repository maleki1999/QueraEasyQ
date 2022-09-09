n,X = [int(i) for i in input().split()]
prices = [int(i) for i in input().split()]
prices.sort()
counter = 1
temp = prices[0]
for price in prices[1:]:
    if price + temp <= X:
        counter += 1
        temp = price
    else:
        break
print(counter)