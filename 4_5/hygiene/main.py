inputs = []
for i in range(2):
    inputs.append(int(input()))
if inputs[1]==0:
    print("20")
elif inputs[1]==7:
    print(inputs[0])
else:
    print(inputs[0]-inputs[1] if inputs[0]-inputs[1]>=0 else "0")