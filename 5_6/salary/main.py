MOD = (10**9)+7
def fast_power(base, power):
    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base) % MOD
        
        # Divide the power by 2
        power = power // 2
        # Multiply base to itself
        base = (base * base) % MOD

    return result

n,q = [int(i) for i in input().split()]
salaries = sum([int(i) for i in input().split()])
questions = [int(input()) for _ in range(q)]
answers = [salaries*fast_power(2,i-1-n)%((10**9)+7) for i in questions]
print(*answers,sep='\n')