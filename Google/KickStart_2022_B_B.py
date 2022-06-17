import sys


def find_factor(n):
    factor = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            factor.update([i, n//i])
    return factor


for t in range(int(sys.stdin.readline())):
    C = 0
    for a in find_factor(int(sys.stdin.readline())):
        if str(a) == str(a)[::-1]:
            C += 1
    print(f'Case #{t+1}: {C}')
