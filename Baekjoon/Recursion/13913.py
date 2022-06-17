# https://www.acmicpc.net/problem/13913

def f(n, k):
    if n >= k:
        return n-k, [*range(n, k-1, -1)]
    elif k == 1:
        return 1, [0, 1]
    elif k % 2:
        a = f(n, k-1)
        b = f(n, k+1)
        if a[0] < b[0]:
            return a[0]+1, a[1]+[k]
        else:
            return b[0]+1, b[1]+[k]
    else:
        b = f(n, k//2)
        if k-n < b[0]+1:
            return k-n, [*range(n, k+1)]
        else:
            return b[0]+1, b[1]+[k]


N, K = map(int, input().split())
R = f(N, K)
print(R[0])
print(*R[1])
