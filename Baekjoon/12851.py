# https://www.acmicpc.net/problem/12851

def f(n, k):
    if n >= k:
        return n-k, 1
    elif k == 1:
        return 1, 1
    elif k % 2:
        a = f(n, k-1)
        b = f(n, k+1)
        if a[0] < b[0]:
            return a[0]+1, a[1]
        elif a[0] > b[0]:
            return b[0]+1, b[1]
        else:
            return a[0]+1, a[1]+b[1]
    else:
        b = f(n, k//2)
        if k-n < b[0]+1:
            return k-n, 1
        elif k-n > b[0]+1:
            return b[0]+1, b[1]
        else:
            return k-n, b[1]+1


N, K = map(int, input().split())
print(*f(N, K))
