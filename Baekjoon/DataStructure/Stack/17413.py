# https://www.acmicpc.net/problem/17413

S = []
R = ''
flag = 0
for a in input():
    if a == ' ':
        if flag:
            S.append(a)
        else:
            R += ''.join(S[::-1])
            S = []
            R += ' '
    elif a == '<':
        R += ''.join(S[::-1])
        S = []
        S.append(a)
        flag = 1
    elif a == '>':
        R += ''.join(S)+a
        S = []
        flag = 0
    else:
        S.append(a)
if S:
    R += ''.join(S[::-1])
print(R)
