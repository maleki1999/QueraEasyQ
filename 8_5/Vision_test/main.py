inputs = []
counter = 0
for i in range(3):
    inputs.append(input())
for x, y in zip(inputs[1],inputs[2]):
        if x != y:
            counter+=1
print(counter)