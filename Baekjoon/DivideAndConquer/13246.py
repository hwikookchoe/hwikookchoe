# https://www.acmicpc.net/problem/13246

def mat_add(x, y):
    return [[(x[a][b]+y[a][b]) % M for b in range(N)] for a in range(N)]


def mat_sub(x, y):
    return [[(x[a][b]-y[a][b]) % M for b in range(N)] for a in range(N)]


def mat_mul(x, y):
    z = [[0]*N for _ in [0]*N]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                z[i][k] += x[i][j]*y[j][k]
                z[i][k] %= M
    return z


def mat_pow(X, n):
    if n == 1:
        return X
    elif n % 2:
        return mat_mul(X, mat_pow(X, n-1))
    else:
        t = mat_pow(X, n//2)
        return mat_mul(t, t)


def solution(X, n):
    if n == 1:
        return mat_add(I, X)
    elif n % 2:
        return mat_mul(mat_add(I, X), solution(mat_pow(X, 2), n//2))
    else:return mat_add(solution(X, n-1), mat_pow(X, n))


M = 1000
N,B = map(int, input().split())
A = [[*map(int, input().split())] for _ in [0]*N]
I = [[+(i == j) for j in range(N)] for i in range(N)]
R = mat_sub(solution(A, B), I)
for n in range(N):
    print(*R[n])
