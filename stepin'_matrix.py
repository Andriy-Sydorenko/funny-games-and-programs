#спочатку вводиться розмір квадратної матриці, потім сама матриця, потім ступінь, до якого треба піднести
"""
Формат вводу:
3
1 2 3
4 5 6
7 8 9
2


or


5
1 2 1 1 2
3 3 3 3 3
1 2 1 1 2
3 3 3 3 3
1 2 1 1 2
3

"""

from copy import deepcopy


def mult_matr(a, b):
    ra = len(a)
    ca = len(a[0])
    rb = len(b)
    cb = len(b[0])
    if ca == rb:
        r = [[0 for _ in range(cb)] for _ in range(ra)]
        for row in range(ra):
            for col in range(cb):
                for j in range(ca):
                    r[row][col] += a[row][j] * b[j][col]
        return r
    else:
        return None


def pow_matr(a, n):
    if len(a) != len(a[0]):
        return None
    else:
        p = deepcopy(a)
        for i in range(n - 1):
            p = mult_matr(p, a)
        return p


n = int(input())
r = []
for i in range(n):
    r.append(list(map(int, input().split(' '))))

k = int(input())
res = pow_matr(r, k)
for i in res:
    print(*i)