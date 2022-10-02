import random
import string
n = int(input())
while True:
    s = ''.join(random.choices(string.ascii_lowercase, k = n ))
    if s[0]=='q':
        print(s)
        break