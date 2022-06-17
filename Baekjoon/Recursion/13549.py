# https://www.acmicpc.net/problem/13549

def f(n, k):
    if n >= k:
        return n-k
    elif k == 1:
        return 1
    elif k % 2:
        return min(f(n, k-1), f(n, k+1))+1
    else:
        return min(k-n, f(n, k//2))


N, K = map(int, input().split())
print(f(N, K))

