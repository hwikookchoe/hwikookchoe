import sys

for t in range(int(sys.stdin.readline())):
    N, P = map(int, sys.stdin.readline().split())
    A = [[0]]+[[*map(int, sys.stdin.readline().split())] for _ in [0]*N]
    R = [[0, 0]]
    for n in range(1, N+1):
        T = max(A[n])-min(A[n])
        T1 = min(R[-1][1]+abs(min(A[n-1])-min(A[n]))+T, R[-1][0]+abs(max(A[n-1])-min(A[n]))+T)
        T2 = min(R[-1][0]+abs(max(A[n-1])-max(A[n]))+T, R[-1][1]+abs(min(A[n-1])-max(A[n]))+T)
        R.append([T1, T2])
    print(f'Case #{t+1}: {min(R[-1])}')
