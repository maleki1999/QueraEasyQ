n = int(input())
keys = [int (i) for i in input().split()]
status = input().split()
print(*sorted([keys[i] for i in range(len(keys)) if status[i]=='1']))