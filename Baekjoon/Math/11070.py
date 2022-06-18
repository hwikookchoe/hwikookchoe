# https://www.acmicpc.net/problem/11070

import sys
I = sys.stdin.readline

for _ in [0]*int(I()):
    N, M = map(int, I().split())
    R = [[0, 0] for _ in [0]*(N+1)]
    for _ in [0]*M:
        a, b, p, q = map(int, I().split())
        R[a][0] += p
        R[a][1] += q
        R[b][0] += q
        R[b][1] += p
    R = [0 if s**2+a**2 == 0 else (s**2)*1000//(s**2+a**2) for s, a in R[1:]]
    sys.stdout.write(f'{max(R)}\n{min(R)}\n')
