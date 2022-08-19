def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


n = int(input())
print("zoj" if n%2 !=0 and is_prime(n) else "fard")


# from sympy import isprime
# n = int(input())
# print("zoj" if n%2 !=0 and isprime(n) else "fard")