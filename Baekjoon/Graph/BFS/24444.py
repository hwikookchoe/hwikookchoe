# https://www.acmicpc.net/problem/24444

import sys
from collections import deque
I = lambda:map(int, sys.stdin.readline().split())
N, M, S = I()
G = [[] for _ in [0]*(N+1)]
for _ in [0]*M:
    u, v = I()
    G[u].append(v)
    G[v].append(u)
G = [sorted(g) for g in G]
V = [1]*(N+1)
R = [0]*(N+1)
V[S] = 0
R[S] = 1
i = 2
Q = deque([S])
while Q:
    T = Q.popleft()
    for X in G[T]:
        if V[X]:
            V[X] = 0
            R[X] = i
            i += 1
            Q.append(X)
print(*R[1:], sep='\n')
