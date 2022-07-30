import numpy as np
numbers = [int(i) for i in input().split()]
correct = [1,1,2,2,2,8]
subtracted_array = np.subtract(np.array(correct) , np.array(numbers))
print(*subtracted_array)